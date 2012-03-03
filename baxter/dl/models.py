"""
  Structures and logic used to extract article [meta]data from an online news source
"""

from django.db import models
from datetime import datetime
import urllib2
from BeautifulSoup import BeautifulSoup
#from django.core import serializers
import simplejson as json

# registers parser for a given source
class Source(models.Model):
  url_base = models.URLField() # base url for the news source
  name = models.CharField(max_length = 250) # name of the news source
  

# series of extraction steps associated with a parser
class ExtractCmd(models.Model):
  source = models.ForeignKey(Source) # parser relation
  order = models.IntegerField() # used to sequence extraction commands
  data = models.CharField(max_length = 250) # describes kind of data being extracted
  tag = models.CharField(max_length = 50) # html tag to target
  attribute = models.CharField(max_length = 250) # attribute type and name
  action  = models.CharField(max_length = 50) # soup action (findall, extract, etc)
  

# base class for obtaining stories from news sources
class Story(models.Model):
  url = models.URLField()
  timestamp = models.DateTimeField(default=datetime.now())
  title = models.CharField(max_length = 250)
  source = models.CharField(max_length = 50)
  html = models.TextField()
  body = models.TextField()

  def untag(self, item, tag, recursive = False):
    tags = item.findAll(tag, recursive=recursive)
    for t in tags:
      t.replaceWith(t.string)

  # remove tags and normalize whitespace
  # takes a list of html snippets, returns a block of text
  def compact(self, items):
    output = []
    for item in items:
      text = ''.join(item.findAll(text=True))
      text = ' '.join(text.split())
      output.append(text)
    return ''.join(output)

  def remove_all(self, item, tag):
    for t in item.findAll(tag):
      t.extract()

  # fixes broken html and returns soup
  def simmer(self, html):
    clean = BeautifulSoup(html, convertEntities=BeautifulSoup.HTML_ENTITIES).prettify()
    return BeautifulSoup(clean)

  # downloads the story from source
  def get(self):
    if None != self.url:
      u = urllib2.urlopen(self.url)      
      self.html = u.read()
      self.save()
      
  # extracts story text + metadata and saves to db
  def process(self):
    soup = self.simmer(self.html)
    self.timestamp = self.get_timestamp(soup)
    self.title = self.get_title(soup)
    self.body = self.get_body(soup)
    self.save()

  def get_timestamp(self, clean):
    return datetime.now()
  def get_title(self, clean):
    return ''
  def get_body(self, clean):
    return ''


"""
  parser specific to the WSJ source
"""
class WSJ(Story):
  class Meta:
    proxy = True

  def process(self):
    self.source = 'Wall Street Journal'
    super(WSJ, self).process()

  def get_timestamp(self, soup):
    text = self.compact(soup.findAll('li', attrs={'class': 'dateStamp'}))
    text = datetime.strptime(text, '%B %d, %Y')
    return text

  def get_title(self, soup):
    text = soup.findAll('div', attrs={'class': 'articleHeadlineBox headlineType-newswire'})
    text = text[0].findAll('h1')
    return self.compact(text)

  def get_body(self, soup):
    text = soup.findAll('div', attrs={'class': 'articlePage'})
    return self.compact(text)


"""
  parser specific to the Philly source
"""
class Philly(Story):
  class Meta:
    proxy = True

  def process(self):
    self.source = 'Philly'
    super(Philly, self).process()

  def get_title(self, soup):
    text = soup.findAll('h1', attrs={'class': 'entry-title'})
    return self.compact(text)

  def get_body(self, soup):
    text = soup.findAll('div', attrs={'class': 'body-content'})
    return self.compact(text)


"""
  parser specific to the AP source
"""
class AP(Story):
  class Meta:
    proxy = True

  def process(self):
    self.source = 'AP'
    super(AP, self).process()

  def get_timestamp(self, soup):
    text = self.compact(soup.findAll('span', attrs={'class': 'updated dtstamp'}))
    text = datetime.strptime(text, '%b. %d, %Y %I:%M %p ET')
    return text

  def get_title(self, soup):
    text = soup.findAll('h1', attrs={'class': 'entry-title'})
    return self.compact(text)

  def get_body(self, soup):
    text = soup.findAll('p', attrs={'class': 'ap_para entry-content'})
    return self.compact(text)


"""
  parser specific to the FoxBusiness source
"""
class FoxBusiness(Story):
  class Meta:
    proxy = True

  def process(self):
    self.source = 'FoxBusiness'
    super(FoxBusiness, self).process()

  def get_timestamp(self, soup):
    text = self.compact(soup.findAll('p', attrs={'class': 'published updated dtstamp'}))
    text = datetime.strptime(text, 'Published %B %d, %Y')
    return text

  def get_title(self, soup):
    text = soup.findAll('h1', attrs={'class': 'entry-title'})
    return self.compact(text)

  def get_body(self, soup):
    text = soup.findAll('div', attrs={'class': 'article-text KonaBody'})
    return self.compact(text)


"""
  parser specific to the Examiner source
"""
class Examiner(Story):
  class Meta:
    proxy = True

  def process(self):
    self.source = 'Examiner'
    super(Examiner, self).process()

  def get_timestamp(self, soup):
    text = self.compact(soup.findAll('span', attrs={'datatype': 'xsd:dateTime'}))
    text = datetime.strptime(text, '%B %d, %Y')
    return text

  def get_title(self, soup):
    text = soup.findAll('h1', attrs={'class': 'entry-title'})
    return self.compact(text)

  def get_body(self, soup):
    text = soup.findAll('div', attrs={'class': 'field-item even'})
    return self.compact(text)


"""
  parser specific to the CSMonitor source
"""
class CSMonitor(Story):
  class Meta:
    proxy = True

  def process(self):
    self.source = 'CSMonitor'
    super(CSMonitor, self).process()

  def get_title(self, soup):
    text = soup.findAll('h1', attrs={'class': 'head'})
    return self.compact(text)

  def get_body(self, soup):
    text = soup.findAll('div', attrs={'class': 'sBody p402_premium'})
    text = text[0].findAll('p')
    return self.compact(text)


"""
  parser specific to the NPR source
"""
class NPR(Story):
  class Meta:
    proxy = True

  def process(self):
    self.source = 'NPR'
    super(NPR, self).process()

  def get_timestamp(self, soup):
    text = self.compact(soup.findAll('span', attrs={'class': 'date'}))
    text = datetime.strptime(text, '%B %d, %YLast updated: %I:%M %p ET')
    return text

  def get_title(self, soup):
    text = soup.findAll('div', attrs={'class': 'storytitle'})
    text = text[0].findAll('h1')
    return self.compact(text)

  def get_body(self, soup):
    text = soup.findAll('div', attrs={'id': 'storytext'})
    return self.compact(text)


"""
  parser specific to the Euronews source
"""
class Euronews(Story):
  class Meta:
    proxy = True

  def process(self):
    self.source = 'Euronews'
    super(Euronews, self).process()

  def get_title(self, soup):
    text = soup.findAll('div', attrs={'id': 'title'})
    text = text[0].findAll('h1')
    return self.compact(text)

  def get_body(self, soup):
    text = soup.findAll('div', attrs={'id': 'article-text'})
    text = text[0].findAll('p')
    return self.compact(text)


"""
  parser specific to the BBC source
"""
class BBC(Story):
  class Meta:
    proxy = True

  def process(self):
    self.source = 'BBC'
    super(BBC, self).process()

  def get_timestamp(self, soup):
    text = self.compact(soup.findAll('span', attrs={'class': 'date'}))
    text += ' ' + self.compact(soup.findAll('span', attrs={'class': 'time'}))
    text = datetime.strptime(text, '%d %B %Y %H:%M ET')
    return text

  def get_title(self, soup):
    text = soup.findAll('h1', attrs={'class': 'story-header'})
    return self.compact(text)

  def get_body(self, soup):
    text = soup.findAll('div', attrs={'class': 'story-body'})
    return self.compact(text)


"""
  parser specific to the UPI source
"""
class UPI(Story):
  class Meta:
    proxy = True

  def process(self):
    self.source = 'UPI'
    super(UPI, self).process()

  def get_title(self, soup):
    text = soup.findAll('div', attrs={'class': 'hl'})
    return self.compact(text)

  def get_body(self, soup):
    text = soup.findAll('div', attrs={'id': 'sv'})
    text = text[0].findAll('p')
    return self.compact(text)


"""
  parser specific to the NationalPost source
"""
class NationalPost(Story):
  class Meta:
    proxy = True

  def process(self):
    self.source = 'NationalPost'
    super(NationalPost, self).process()

  def get_title(self, soup):
    text = soup.findAll('h1', attrs={'class': 'npStoryTitle'})
    return self.compact(text)

  def get_body(self, soup):
    text = soup.findAll('div', attrs={'class': 'npBlock npPostContent'})
    text = text[0].findAll('p')
    return self.compact(text)


"""
  parser specific to the AlJazeera source
"""
class AlJazeera(Story):
  class Meta:
    proxy = True

  def process(self):
    self.source = 'AlJazeera'
    super(AlJazeera, self).process()

  def get_timestamp(self, soup):
    text = self.compact(soup.findAll('span', attrs={'id': 'ctl00_cphBody_lblDate'}))
    text = datetime.strptime(text, '%d %b %Y %H:%M')
    return text

  def get_title(self, soup):
    text = soup.findAll('span', attrs={'id': 'DetailedTitle'})
    return self.compact(text)

  def get_body(self, soup):
    text = soup.findAll('td', attrs={'class': 'DetailedSummary'})
    return self.compact(text)



"""
  parser specific to the AsiaOne source
"""
class AsiaOne(Story):
  class Meta:
    proxy = True

  def process(self):
    self.source = 'AsiaOne'
    super(AsiaOne, self).process()

  def get_title(self, soup):
    text = soup.findAll('div', attrs={'id': 'art_title'})
    return self.compact(text)

  def get_body(self, soup):
    text = soup.findAll('div', attrs={'class': 'clear_lft'})
    text = text[0].findAll('p')
    return self.compact(text)



"""
  parser specific to the WorldBulletin source
"""
class WorldBulletin(Story):
  class Meta:
    proxy = True

  def process(self):
    self.source = 'WorldBulletin'
    super(WorldBulletin, self).process()

  def get_title(self, soup):
    text = soup.findAll('div', attrs={'class': 'baslikbuyuk'})
    return self.compact(text)

  def get_body(self, soup):
    text = soup.findAll('div', attrs={'class': 'vucut'})
    return self.compact(text)


"""
  parser specific to the Telegraph source
"""
class Telegraph(Story):
  class Meta:
    proxy = True

  def process(self):
    self.source = 'Telegraph'
    super(Telegraph, self).process()

  def get_timestamp(self, soup):
    text = self.compact(soup.findAll('p', attrs={'class': 'publishedDate'}))
    text = datetime.strptime(text, '%I:%M%p GMT %d %b %Y')
    return text

  def get_title(self, soup):
    text = soup.findAll('div', attrs={'class': 'storyHead'})
    text = text[0].findAll('h1')
    return self.compact(text)

  def get_body(self, soup):
    byline = soup.findAll('div', attrs={'class': 'bylineComments'})
    byline[0].extract()
    text = soup.findAll('div', attrs={'class': 'story'})
    text = text[0].findAll('p')
    return self.compact(text)



"""
  parser specific to the Gizmodo source
"""
class Gizmodo(Story):
  class Meta:
    proxy = True

  def process(self):
    self.source = 'Gizmodo'
    super(Gizmodo, self).process()

  def get_title(self, soup):
    text = soup.findAll('h1', attrs={'class': 'headline'})
    return self.compact(text)

  def get_body(self, soup):
    text = soup.findAll('div', attrs={'class': 'post-body'})
    return self.compact(text)



"""
  parser specific to the NYPost source
"""
class NYPost(Story):
  class Meta:
    proxy = True

  def process(self):
    self.source = 'NYPost'
    super(NYPost, self).process()

  def get_title(self, soup):
    text = soup.findAll('div', attrs={'id': 'story'})
    text = text[0].findAll('h1')
    return self.compact(text)

  def get_body(self, soup):
    text = soup.findAll('div', attrs={'class': 'story_body'})
    text = text[0].findAll('p')
    return self.compact(text)



"""
  parser specific to the FoxNews source
"""
class FoxNews(Story):
  class Meta:
    proxy = True

  def process(self):
    self.source = 'FoxNews'
    super(FoxNews, self).process()

  def get_timestamp(self, soup):
    text = self.compact(soup.findAll('p', attrs={'class': 'published updated dtstamp'}))
    text = datetime.strptime(text, 'Published %B %d, %Y')
    return text

  def get_title(self, soup):
    text = soup.findAll('h1', attrs={'id': 'article-title'})
    return self.compact(text)

  def get_body(self, soup):
    text = soup.findAll('div', attrs={'class': 'entry-content KonaBody'})
    return self.compact(text)


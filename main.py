from BeautifulSoup import BeautifulSoup
import urllib2

#nyt = {'url' : 'http://www.nytimes.com/2012/01/16/world/europe/italian-cruise-ship-accident-raises-questions-about-crew-and-captain.html',
#       'body' : 'div class:articleBody',

"""
sample story urls:
ethio:
http://www.chicagotribune.com/news/sns-rt-us-ethiopia-rightstre80g08k-20120116,0,2075304.story
http://old.news.yahoo.com/s/nm/20120117/wl_nm/us_ethiopia_rights
http://www.bbc.co.uk/news/world-africa-16590416
http://www.huffingtonpost.com/2012/01/17/ethiopia-forced-resettlement_n_1210015.html

kodak:
http://www.japantoday.com/category/commentary/view/photo-industry-mourns-kodak
"""


#f = urllib2.urlopen(url)
f = open('ethiopia_bbc.html', 'r')
#f = open('nyt.html', 'r')
html = f.read()

def untag(item, tag, recursive = False):
  tags = item.findAll(tag, recursive=recursive)
  for t in tags:
    t.replaceWith(t.string)

# remove tags and normalize whitespace
# takes a list of html snippets, returns a block of text
def compact(items):
  output = []
  for item in items:
    text = ''.join(item.findAll(text=True))
    text = ' '.join(text.split())
    output.append(text)
  return ''.join(output)

def remove_all(item, tag):
  for t in item.findAll(tag):
    t.extract()

# fixes broken html and returns soup
def simmer(html):
  clean = BeautifulSoup(html, convertEntities=BeautifulSoup.HTML_ENTITIES).prettify()
  return BeautifulSoup(clean)

def nyt(html):
  soup = simmer(html)
  body = soup.findAll('div', attrs={'class': 'articleBody'})
  return compact(body)

def bbc(html):
  soup = simmer(html)
  body = soup.findAll('div', attrs={'class': 'story-body'})[0]
  for t in body.findAll('script'):
    t.extract()
  for t in body.findAll('link'):
    t.extract()
  for t in body.findAll('meta'):
    t.extract()
  for t in body.findAll('form'):
    t.extract()
  for t in body.findAll('param'):
    t.extract()
  for t in body.findAll('div', attrs={'id': 'page-bookmark-links-head'}):
    t.extract()
  return body
#    for t in item.findAll('div', attrs={'class': 'sidebar'}):
#      t.extract()
#    for t in item.findAll('span', attrs={'class': 'photo'}):
#      t.extract()
#    for t in item.findAll('blockquote', attrs={'class': 'pullq'}):
#      t.extract()
#  return compact(body)

def cbc(html):
  soup = simmer(html)
  body = soup.findAll('div', attrs={'id': 'storybody'})
  for item in body:
    for t in item.findAll('div', attrs={'class': 'sidebar'}):
      t.extract()
    for t in item.findAll('span', attrs={'class': 'photo'}):
      t.extract()
    for t in item.findAll('blockquote', attrs={'class': 'pullq'}):
      t.extract()
    for t in item.findAll('script'):
      t.extract()
  return compact(body)

def telegraph(html):
  soup = simmer(html)
  body = soup.findAll('div', attrs={'id': 'tmglBody'})
  return body
  for item in body:
    remove_all(item, 'script')
    remove_all(item, 'style')
    for t in item.findAll('div', attrs={'id': 'oneHalf'}):
      t.extract()
    for t in item.findAll('div', attrs={'id': 'tmg-related-links'}):
      t.extract()
    for t in item.findAll('div', attrs={'id': 'storyFunc'}):
      t.extract()
  return compact(body)

#print telegraph(html)
#print nyt(html)
#print cbc(html)
#print BeautifulSoup(html, convertEntities=BeautifulSoup.HTML_ENTITIES).prettify()
print bbc(html)

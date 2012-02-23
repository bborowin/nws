import django
import django.core.management
import settings
django.core.management.setup_environ(settings)
from baxter.dl.models import Story, WSJ, Philly, AP, FoxBusiness, Examiner, CSMonitor, NPR, Euronews, BBC, UPI, NationalPost
from baxter.dl.models import Telegraph, AlJazeera, AsiaOne, WorldBulletin, Gizmodo, NYPost, FoxNews

stories = []

# infant tylenol
urls = ['http://online.wsj.com/article/SB10001424052970204792404577229072114500132.html?mod=europe_home',
        'http://www.philly.com/philly/business/breaking/20120217_ap_jjconsumerhealthsegmentrecallsinfanttylenol.html?c=r',
        'http://www.philly.com/philly/business/20120218_Infants__Tylenol_recalled_by_J_J.html',
        'http://hosted2.ap.org/APDEFAULT/bbd825583c8542898e6fa7d440b9febc/Article_2012-02-17-US-Johnson-and-Johnson-Infant-Tylenol-Recall/id-1eeeade97a164e04bbe1241425f0f97e',
        'http://www.foxbusiness.com/news/2012/02/17/wsj-bloghealth-jj-recall-watch-mcneil-pulls-liquid-infant-tylenol-on-dosing/',
        'http://www.examiner.com/family-parenting-in-st-louis/recall-alert-infants-tylenol',
        'http://www.csmonitor.com/Business/Latest-News-Wires/2012/0217/Infant-Tylenol-recall-new-setback-for-Johnson-Johnson']
stories.append(urls)

# syria funeral protests
urls = ['http://hosted2.ap.org/APDEFAULT/cae69a7523db45408eeb2b3a98c0c9c5/Article_2012-02-18-ML-Syria/id-abe62b669f394ebab1a571e1f22b7648',
        'http://www.npr.org/2012/02/18/147092364/syrian-forces-fire-on-funeral-1-reported-killed?ft=1&f=1001',
        'http://news.nationalpost.com/2012/02/18/iran-warships-enter-mediterranean-as-others-warn-of-middle-east-nuclear-arms-race/',
        'http://www.bbc.co.uk/news/world-middle-east-17085226',
        'http://www.upi.com/Top_News/World-News/2012/02/18/Syrian-forces-open-fire-on-funeral-march/UPI-47671329603686/']
stories.append(urls)

urls = ['http://news.nationalpost.com/2012/02/18/iran-warships-enter-mediterranean-as-others-warn-of-middle-east-nuclear-arms-race/',
        'http://www.aljazeera.com/news/middleeast/2012/02/2012218143339683553.html',
        'http://news.asiaone.com/News/Latest%2BNews/World/Story/A1Story20120218-328766.html',
        'http://www.worldbulletin.net/?aType=haber&ArticleID=85968']
stories.append(urls)

# snowtrapped swede
urls = ['http://www.bbc.co.uk/news/world-europe-17088173',
        'http://www.telegraph.co.uk/news/worldnews/europe/sweden/9093760/Man-who-survived-two-months-in-snowbound-car-had-lived-in-forest-since-last-summer.html',
        'http://gizmodo.com/5886507/how-a-man-survived-without-food-for-two-months-in-a-snow%20buried-car',
        'http://www.nypost.com/p/news/international/swedish_snow_survived_hibernating_WgQ44x01bG69Jjw0BlTteK?CMP=OTC-rss&FEEDNAME=',
        'http://www.foxnews.com/world/2012/02/20/swedish-man-survives-two-months-in-sub-zero-temperatures-by-hibernating-in-car/#ixzz1mtruzMKy?test=latestnews']
stories.append(urls)

# argentina train crash
urls = ['http://www.cnbc.com/id/46482274?__source=RSS*tag*&par=RSS',
        'http://www.latimes.com/news/la-wono-argentina-train-m,0,2154760.story?track=rss&utm_source=feedburner&utm_medium=feed&utm_campaign=Feed%3A+latimes%2Fnews+%28L.A.+Times+-+Top+News%29',
        'http://www.usatoday.com/news/world/story/2012-02-22/argentina-train-accident/53208110/1']
stories.append(urls)


# google smartglasses
urls = ['http://abcnews.go.com/blogs/technology/2012/02/google-glasses-coming-to-an-eyewear-stand-near-you/',
        'http://www.washingtonpost.com/business/technology/would-you-buy-googles-glasses/2012/02/22/gIQAm0cTTR_story.html?wprss=',
        'http://www.latimes.com/business/technology/la-fi-tn-google-x-smart-glasses-heads-up-display-augmented-reality-rumor-20120222,0,653228.story?track=rss&utm_source=feedburner&utm_medium=feed&utm_campaign=Feed%3A+latimes%2Ftechnology+%28L.A.+Times+-+Technology+News%29',
        'http://content.usatoday.com/communities/technologylive/post/2012/02/google-glasses-new-york-times/1?csp=34tech&utm_source=feedburner&utm_medium=feed&utm_campaign=Feed%3A+usatoday-TechTopStories+%28Tech+-+Top+Stories%29#.T0VZ1Gzbdw8',
        'http://www.foxnews.com/scitech/2012/02/22/google-to-offer-terminator-style-smartphone-glasses-later-this-year/']
stories.append(urls)


sources = { 'http://online.wsj.com' : WSJ,
            'http://www.philly.com' : Philly,
            'http://hosted2.ap.org' : AP,
            'http://www.foxbusiness.com' : FoxBusiness,
            'http://www.examiner.com' : Examiner,
            'http://www.csmonitor.com' : CSMonitor,
            'http://www.npr.org' : NPR,
            'http://www.euronews.net' : Euronews,
            'http://www.bbc.co.uk' : BBC,
            'http://news.nationalpost.com' : NationalPost,
            'http://www.aljazeera.com' : AlJazeera,
            'http://news.asiaone.com' : AsiaOne,
            'http://www.worldbulletin.net' : WorldBulletin,
            'http://www.telegraph.co.uk' : Telegraph,
            'http://gizmodo.com' : Gizmodo,
            'http://www.nypost.com' : NYPost,
            'http://www.foxnews.com' : FoxNews,
            'http://www.upi.com' : UPI
          }

for urls in stories:
  for url in urls:
    print url,
    t = None
    for key in sources:
      if key in url:
        if key in sources:
          t = sources[key]
          print t
    if None == t:
      t = Story
    try:
      s = t.objects.get(url = url)
      print "found cached",
    except t.DoesNotExist:
      print "downloading",
      s = t(url = url)
      s.get()
    print 'html length %db' % len(s.html)
    s.process()


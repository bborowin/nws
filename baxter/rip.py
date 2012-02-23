import re
import sys, json
import nltk
from string import find
import django
import django.core.management
import settings
django.core.management.setup_environ(settings)
from baxter.dl.models import Story

def subsequence(feed, first, second):
  print first, second
  one = feed[first]
  two = feed[second]
  two = ' '.join(two)
  i = 0
  j = 0
  previdx = 0
  while i < len(one):
    sub = ' '.join(one[i:j])
    psub = ''
    while sub in two and j < len(one):
      if len(psub) < len(sub):
        psub = sub
        #print '--', psub
      sub = ' '.join(one[i:j])
      j += 1
    if len(psub) > 0:
      j -= 1
      if j - i > 2:
        #print '(%d,%d)' % (i,j), psub
        print psub, '<|>',
    i = j
  print

#indices = [i for i, x in enumerate(two) if x == token]
          
# makeVectors: list to n-tuples
# http://code.activestate.com/lists/python-tutor/74382/
def mv(length, listname):
  vectors = (listname[i:i+length] for i in range(len(listname)-length+1))
  result = []
  for v in vectors:
    result.append(v)
  return result


feed = []
#stories = Story.objects.all()
stories = Story.objects.filter(id__gt=4)
for s in stories:
  print '%s (%s) "%s"' % (s.source, s.timestamp, s.title)
  article = s.body.lower().strip()
  for bad in ['\'', '\'s', '.', ',', '"', ':', ';', '-', '&']:
    article = " ".join(article.replace(bad,' ').split())
  #regex = re.compile(' (a|as|at|in|is|of|on|or|to|and|for|the|if) ')
  #l = 0
  #while l != len(article):
  #  l = len(article)
  #  article = regex.sub(' ', article, count=0)
  tokens = nltk.word_tokenize(article)
  tuples = {}
  for size in range(1,25):
    tuples[size] = mv(size, tokens)
    #print 'added %d %d-tuples' % (len(tuples[size]), size)
  feed.append(tuples)
print

# take tuples that overlap by n-1 elements and fold them into unique arrays
def fold_tuples(tuples):
  segments = []
  segment = tuples[0]
  for i in range(len(tuples)-1):
    count = 0
    for j in range(len(tuples[i])-1):
      if tuples[i][j+1] == tuples[i+1][j]:
        count += 1
    # check if consecutive tuples overlap
    if count < len(tuples[i]) - 1:
      # nope -- dump the segment so far, start a new one
      segments.append(segment)
      #print ' '.join(segment)
      segment = tuples[i+1]
    else:
      # yes -- append the end of the last tuple to the segment
      segment.append(tuples[i+1][-1])
  if len(segment) > 0:
    segments.append(segment)
    #print ' '.join(segment)
  return segments

size = 4
for i in range(0, len(feed)):
  for j in range(i+1, len(feed)):
    print ' << comparing %s and %s >>' % (stories[i].source, stories[j].source)
    count = 0
    common = []
    for s in feed[i][size]:
      for t in feed[j][size]:
        if s == t:
          common.append(s)
          count += 1
    if count > 0:
      for s in fold_tuples(common):
        print ' '.join(s)
      print

#for s in fold_tuples(feed[2][5]):
#  print ' '.join(s)

"""
at improving the experience of
improving the experience of users
the experience of users have
experience of users have backfired
of users have backfired at
users have backfired at times
mcneil has been making to
"""

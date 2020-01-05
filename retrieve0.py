"""retrieve0.py
 python retrieve0.py md,slp1,deva testin.txt testout.txt

"""
import re,codecs,sys
import urllib

class Key(object):
 def __init__(self,line):
  self.key = line.rstrip('\r\n')
  self.raw = None  # result from Cologne api
  self.txt = None  # conversion to convenient form

 def lookup(self,url,tranin,tranout):
  # dictionary of GET parameters
  key = self.key
  #paramd = {'key':key,'tranin':tranin,'tranout':tranout} 
  paramd = {'key':key,'filterin':tranin,'filter':tranout} 
  # convert for adding to url
  params = urllib.urlencode(paramd)
  url_full = "%s?%s" %(url,params)
  # access the url
  f = urllib.urlopen(url_full)
  self.raw = f.read()
  print "url_full=",url_full
  print "result=",self.raw
  f.close()

 def raw2txt(self):
  x = self.raw.decode('utf-8')
  lines = x.splitlines()
  y = '<br>'.join(lines)
  self.txt = y

 def write(self,f):
  # convert raw txt to desired txt, in self.txt field
  self.raw2txt()
  # key, text as two tab-delimited fields
  f.write("%s\t%s\n" %(self.key,self.txt))

def read_keys(filein):
 with codecs.open(filein,"r","utf-8") as f:
  keys = [Key(x) for x in f if not x.startswith(';')]
 return keys

def getword_url(dictcode):
 # dictyear has all dictionary codes, with the 'year'.
 # This 'year' is required to locate the files
 # This is a Python dictionary data structure, quite like a PHP associative array
 dictyear={"ACC":"2014" , "AE":"2014" , "AP":"2014" , "AP90":"2014",
       "BEN":"2014" , "BHS":"2014" , "BOP":"2014" , "BOR":"2014",
       "BUR":"2013" , "CAE":"2014" , "CCS":"2014" , "GRA":"2014",
       "GST":"2014" , "IEG":"2014" , "INM":"2013" , "KRM":"2014",
       "MCI":"2014" , "MD":"2014" , "MW":"2014" , "MW72":"2014",
       "MWE":"2013" , "PD":"2014" , "PE":"2014" , "PGN":"2014",
       "PUI":"2014" , "PWG":"2013" , "PW":"2014" , "SCH":"2014",
       "SHS":"2014" , "SKD":"2013" , "SNP":"2014" , "STC":"2013",
       "VCP":"2013" , "VEI":"2014" , "WIL":"2014" , "YAT":"2014"}
 dictup = dictcode.upper()  # all caps for use with dictyear
 year = dictyear[dictup]    # program failure if unknown dictionary
 url = "http://www.sanskrit-lexicon.uni-koeln.de/scans/%sScan/%s/web/webtc/getword.php"%(dictup,year)
 return url

if __name__ == "__main__":
 parms = sys.argv[1]
 filein = sys.argv[2]
 fileout = sys.argv[3]
 dictcode,tranin,tranout = parms.split(',')
 keys = read_keys(filein)
 url = getword_url(dictcode)

 for key in keys:
  key.lookup(url,tranin,tranout)

 with codecs.open(fileout,"w","utf-8") as f:
  for key in keys:
   key.write(f)

 

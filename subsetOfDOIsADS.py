import requests
import json
import csv
import pandas as pd
import sys
import requests.packages.urllib3
import urllib
import time

requests.packages.urllib3.disable_warnings()

devkey = (open('dev_key.txt','r')).read()

doi = ["10.1006/jmsp.1993.1185", "10.1006/jmsp.1993.1174", "10.1006/jmsp.1993.1199", "10.1006/jmsp.1993.1039", "10.1006/jmsp.1993.1184", "10.1006/jmsp.1993.1245", "10.1006/jmsp.1993.1192", "10.1006/jmsp.1993.1009", "10.1016/0022-2852(92)90028-M", "10.1016/0022-2852(92)90217-C"]

citeCount = []
pubDate = []

for i in range(0, len(doi)):
    print "Record num: ", i
    aDOI = doi[i]
    #must encode doi string for url and suggested to include in quotes
    url = 'https://api.adsabs.harvard.edu/v1/search/query/?q=doi:'+'"'+urllib.quote_plus(aDOI)+'"'+'&fl=citation_count,pubdate'
    #print url
    
    #required by the API
    headers = {'Authorization': 'Bearer '+devkey}
    content = requests.get(url, headers=headers)
    try:
        results = content.json()
        k = results['response']['docs'][0]
        print results
        
        pDate = k['pubdate']
        citation = k['citation_count']

    except:
        pDate = "Record Not in ADS"
        citation = "['error code: '",sys.exc_info()[0],"]"
            
    citeCount.append(citation)
    pubDate.append(pDate)
    
    time.sleep(.1)
print citeCount
print pubDate

df1 = pd.DataFrame({"DOI" : doi,
    "Citation" : citeCount,
    "PubDate" : pubDate})

df1.to_csv(path_or_buf= "trial.csv", encoding="utf-8")


# encoding: utf-8
import scraperwiki
import urlparse
import lxml.html


# create a new function, which gets passed a variable we're going to call 'url'
def scrape_dof(url):
    html = scraperwiki.scrape(url)
    
    root = lxml.html.fromstring(html)
    
    #line below selects all <div class="notice-search-item">
    rows = root.cssselect("div.notice-search-item")
    
    for row in rows:
        # Set up our data record - we'll need it later
        record = {}
       
        #n = 0
        #for a in row.cssselect("a"):
        #    print(n)
        #    print(a.get('href'))
        #    n = n+1
        
        link = row.cssselect("a")
        link1 = link[0].get('href')
        
        dofref = element[6].text_content()
        title = element[1].text_content()
        element = row.cssselect("div")
        klient = element[3].text_content()
        kgtype = element[4].text_content()
        kgdato = element[7].text_content()
        
        record['DofRef'] = dofref
        record['Title'] = title
        record['Klient'] = klient
        record['Kungj_type'] = kgtype
        record['Kungj_dato'] = kgdato
        record['Link'] = link1
       
        
        # Finally, save the record to the datastore - 'Name' is our unique key
        scraperwiki.sqlite.save(["Dofref"], record)
        
#doflist = ['www.doffin.no/Notice?query=&PageNumber=1&PageSize=20&OrderingType=0&OrderingDirection=1&NoticeType=3&IncludeExpired=false']
doflist = ['www.doffin.no/Notice?&OrderingType=0&OrderingDirection=1&IsAdvancedSearch=false&IncludeExpired=false&Cpvs=09200000+35110000+44610000+45220000+45230000+51200000+51100000+51800000+71300000+71530000+76000000']
for url in doflist:
    fullurl = 'http://'+url
    print 'scraping ', fullurl
    scrape_dof(fullurl)
    print 'and done'

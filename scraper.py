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
       
        n = 0
        for a in row.cssselect("a"):
            print(n)
            print(a::attr(href))
            n = n+1
            
        element = row.cssselect("div")
        title = element[1].text_content()
        klient = element[3].text_content()
        kgtype = element[4].text_content()
        dofref = element[6].text_content()
        kgdato = element[7].text_content()
        
        record['DofRef'] = dofref
        record['Title'] = title
        record['Klient'] = klient
        record['Kungj_type'] = kgtype
        record['Kungj_dato'] = kgdato
       
        
        # Finally, save the record to the datastore - 'Name' is our unique key
        scraperwiki.sqlite.save(["Dofref"], record)
        
doflist = ['www.doffin.no/Notice?query=&PageNumber=1&PageSize=20&OrderingType=0&OrderingDirection=1&RegionId=&CountyId=&MunicipalityId=&IsAdvancedSearch=false&location=&NoticeType=3&PublicationType=&IncludeExpired=false&Cpvs=&EpsReferenceNr=&DeadlineFromDate=&DeadlineToDate=&PublishedFromDate=&PublishedToDate=']
for url in doflist:
    fullurl = 'http://'+url
    print 'scraping ', fullurl
    scrape_dof(fullurl)
    print 'and done'

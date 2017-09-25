# encoding: utf-8
import scraperwiki
import urlparse
import lxml.html

# create a new function, which gets passed a variable we're going to call 'url'
def scrape_dof(url):
    html = scraperwiki.scrape(url)
    
    #print html
    root = lxml.html.fromstring(html)
    #print root.find_class("div.notice-search-item")
        
    #line below selects all <div class="notice-search-item">
    rows = root.cssselect("div.notice-search-item")
    for row in rows:
        #print(row.text_content().encode("utf-8"))
        #print(row.classes())
        # Set up our data record - we'll need it later
        record = {}
        a = row.cssselect("a") #grab all <a> tags within our <div>
        title = a[0].text
        
        for div in row.cssselect("div"):
            print(div.text_content()encode("utf-8"))        
        
        
        record['Title'] = title
        #record['Link'] = link
        #record['Reference'] = ref
        #record['Company'] = company
        
        # Finally, save the record to the datastore - 'Name' is our unique key
        scraperwiki.sqlite.save(["Title"], record)
        
doflist = ['www.doffin.no/Notice?query=&PageNumber=1&PageSize=30&OrderingType=0&OrderingDirection=1&RegionId=&CountyId=&MunicipalityId=&IsAdvancedSearch=false&location=&NoticeType=3&PublicationType=&IncludeExpired=false&Cpvs=&EpsReferenceNr=&DeadlineFromDate=&DeadlineToDate=&PublishedFromDate=&PublishedToDate=']
for url in doflist:
    fullurl = 'http://'+url
    print 'scraping ', fullurl
    scrape_dof(fullurl)

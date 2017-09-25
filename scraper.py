import scraperwiki
import urlparse
import lxml.html

# create a new function, which gets passed a variable we're going to call 'url'
def scrape_dof(url):
    html = scraperwiki.scrape(url)
    #print html
    root = lxml.html.fromstring(html)
    #line below selects all <div class="notice-search-item">
    rows = root.cssselect("div.notice-search-item")
    for row in rows:
        #print row
        # Set up our data record - we'll need it later
        record = {}
        a = row.cssselect("a") #grab all <a> tags within our <div>
        title = a[0].text
        #company = a[1].text
        
        #repeat process for <span class="right-col"> 
        item_right = row.cssselect("div.right-col")
        ref = item_right[0].text
        #date = item_right[1].text
        
        #record['URL'] = url
        record['Title'] = title
        record['Reference'] = ref
        #record['Company'] = company
        
        print record, '------------'
        # Finally, save the record to the datastore - 'Name' is our unique key
        scraperwiki.sqlite.save(["Title"], record)
        
doflist = ['www.doffin.no/Notice?query=&PageNumber=1&PageSize=10&OrderingType=0&OrderingDirection=1&RegionId=&CountyId=&MunicipalityId=&IsAdvancedSearch=false&location=&NoticeType=3&PublicationType=&IncludeExpired=false&Cpvs=&EpsReferenceNr=&DeadlineFromDate=&DeadlineToDate=&PublishedFromDate=&PublishedToDate=']
for url in doflist:
    fullurl = 'http://'+url
    print 'scraping ', fullurl
    scrape_dof(fullurl)

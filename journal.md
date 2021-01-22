####Dev Journal
**01-22-2021**
- the app does not scrape jobs when deployed on web-server(heroku) 
    - it still works on localhost
    - it works first time I opened the app after deploy, but the second time I access, it does not work when I access next time.
    - it prints out default 25 results thereafter.. 
- what could possibly went wrong:
    - cache
    - whenever it wakes up from (there's new visit in the website), scraper does not work? 
    

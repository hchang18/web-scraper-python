<h4>Dev Journal</h4>

**01-22-2021**

- The app does not scrape jobs when deployed on web-server(heroku) 
    - it still works on localhost
    - it works first time I opened the app after deploy, but the second time I access, it does not work when I access next time.
    - it prints out default 25 results thereafter.. 

- What could possibly went wrong:
    - cache
    - whenever it wakes up from (there's new visit in the website), scraper does not work? 

**01-23-2021**

- Fixed the problem that job scrapper does not work on web-server by **deactivating threaded option** in main function (app.py) 
- Check again to see if it continues to work okay  

**01-24-2021**
- The problem happened again last night
- Tried this morning again and it worked fine.. suspect that the problem relates to restarting (or awaking) of app 

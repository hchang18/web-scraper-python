"""
Scrap the job information in the portland (indeed, stackoverflow)
- https://www.indeed.com/jobs?q=python&l=PORTLAND&radius=50

libraries:
- requests
- beautifulsoup: very useful to extract information from html
"""
from indeed import get_jobs as get_indeed_jobs
from stackoverflow import get_jobs as get_so_jobs
from save import save_to_file
# Todo list: linkedin jobs webscrapper

indeed_jobs = get_indeed_jobs()
stackoverflow_jobs = get_so_jobs()
jobs = indeed_jobs + stackoverflow_jobs
save_to_file(jobs)




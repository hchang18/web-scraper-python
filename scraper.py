"""
Scrap the job information in the portland (indeed, stackoverflow)
- https://www.indeed.com/jobs?q=python&l=PORTLAND&radius=50

libraries:
- requests
- beautifulsoup: very useful to extract information from html
"""
from indeed import get_jobs as get_indeed_jobs
from stackoverflow import get_jobs as get_so_jobs
# # Todo list: linkedin jobs webscrapper


def get_jobs(word):
    indeed_jobs = get_indeed_jobs(word)
    stackoverflow_jobs = get_so_jobs(word)
    # add any other job search site
    jobs = indeed_jobs + stackoverflow_jobs
    return jobs


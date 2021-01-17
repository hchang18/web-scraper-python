"""
Scrap the job information in the portland (indeed, stackoverflow)
- https://www.indeed.com/jobs?q=python&l=PORTLAND&radius=50

libraries:
- requests
- beautifulsoup: very useful to extract information from html
"""
from indeed import get_jobs as get_indeed_jobs

indeed_jobs = get_indeed_jobs()

print(indeed_jobs)




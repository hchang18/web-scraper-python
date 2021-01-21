"""
step 1: get the page
step 2: make the requests
step 3: extract the jobs
"""

import requests
from bs4 import BeautifulSoup


def get_last_page(url):
    result = requests.get(url)
    soup = BeautifulSoup(result.text, "html.parser")
    pages = soup.find("div", {"class": "s-pagination"})
    # when there is no pagination (so few number of jobs)
    if pages:
        pages = pages.find_all("a")
        last_page = pages[-2].get_text().strip()  # cut it before the last pagination
    else:
        last_page = "1"
    return int(last_page)


def extract_job(html):
    title = html.find("h2").find("a")["title"]
    company, location = html.find(
        "h3"
    ).find_all(
        "span", recursive=False
    )   # recursive flat prevents you from going deep
    company = company.get_text(strip=True)
    location = location.get_text(strip=True)
    job_id = html["data-jobid"]
    return {
        'title': title,
        'company': company,
        'location': location,
        'link': f"https://stackoverflow.com/jobs/{job_id}"
    }


def extract_jobs(last_page, url):
    jobs = []
    for page in range(last_page):
        print(f"Scrapping stackoverflow page {page}")
        result = requests.get(f"{url}&pg={page+1}")
        soup = BeautifulSoup(result.text, "html.parser")
        results = soup.find_all("div", {"class": "-job"})
        for result in results:
            job = extract_job(result)
            jobs.append(job)
    return jobs


def get_jobs(word):
    QUALITY = word
    LOCATION = "PORTLAND"
    RADIUS = "20"
    REMOTE = "false"  # if you want to find remote jobs, append "&r=true" at the end
    url = f"https://stackoverflow.com/jobs?q={QUALITY}&l={LOCATION}&d={RADIUS}"
    last_page = get_last_page(url)
    jobs = extract_jobs(last_page, url)
    return jobs

import requests
from bs4 import BeautifulSoup

def get_last_page(url):
    result = requests.get(url)
    soup = BeautifulSoup(result.text, "html.parser")
    pagination = soup.find("div", {"class": "pagination"})
    links = pagination.find_all('a')    # find all the anchor
    pages = []
    for link in links[:-1]:
        pages.append(int(link.find("span").string))
    max_page = pages[-1]
    return max_page


def extract_job(html):
    title = html.find("h2", {"class": "title"}).find("a")["title"]
    company = html.find("span", {"class": "company"})
    company_anchor = company.find("a")
    # tip: some company has link ("a"), some company does not..
    if company:
        if company.find("a") is not None:
            company = company_anchor.string.strip()
        else:
            company = company.string.strip()
    else:
        company = None
    # tip: when there are None data in place where location should be
    # look at a line above or below.. instead of <span>, we found <div>
    # location = html.find("span", {"class": "location"})
    location = html.find("div", {"class": "recJobLoc"})["data-rc-loc"]
    job_id = html["data-jk"]
    return {
        'title': title,
        'company': company,
        'location': location,
        'link': f"https://www.indeed.com/viewjob?jk={job_id}"
    }


def extract_jobs(last_page, url, limit):
    jobs = []
    for page in range(last_page):
        print(f"Scrapping indeed page {page}")
        result = requests.get(f"{url}&start={page*limit}")
        soup = BeautifulSoup(result.text, "html.parser")
        results = soup.find_all("div", {"class": "jobsearch-SerpJobCard"})
        for result in results:
            job = extract_job(result)
            jobs.append(job)
    return jobs


def get_jobs(word):
    limit = 10
    LOCATION = "PORTLAND"
    RADIUS = "50"
    QUALITY = word
    url = f"https://www.indeed.com/jobs?q={QUALITY}&l={LOCATION}&radius={50}&limit={limit}"
    last_page = get_last_page(url)
    jobs = extract_jobs(last_page, url, limit)
    return jobs


import csv


def save_to_file(jobs):
    file = open("jobs.csv", mode="w")
    writer = csv.writer(file)
    writer.writerow([key for key in jobs[0].keys()])    # title, company, location, link
    for job in jobs:
        writer.writerow(list(job.values()))
    return
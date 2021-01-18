from flask import Flask, render_template, request, redirect, send_file
from scrapper import get_jobs
from save import save_to_file

app = Flask("SuperScrapper")

# database to store jobs
# should be outside the route
db = {}

@app.route("/")
def home():
    return render_template("search.html")


@app.route("/report")
def report():
    # query arguments
    word = request.args.get('word')
    if word:
        word = word.lower()
        existingJobs = db.get(word)
        if existingJobs:
            jobs = existingJobs
        else:
            jobs = get_jobs(word)
            db[word] = jobs
    else:
        # we don't want anyone to access /report without any word
        # better redirect it to home
        return redirect("/")
    return render_template("report.html",
                           searchingBy=word,
                           resultsNumber=len(jobs),
                           jobs=jobs)


@app.route("/export")
def export():
    try:
        word = request.args.get('word')
        if not word:
            raise Exception()
        word = word.lower()
        jobs = db.get(word)
        if not jobs:
            raise Exception()
        save_to_file(jobs)
        return send_file("jobs.csv")
    except:
        # consequence of an error
        return redirect("/")


# decorator below looks for function right under to execute
# @app.route("/contact")
# def contact_me():
#     return "Contact me!"


# dynamic url
# @app.route("/<username>")
# def potato(username):
#     return f"Hello {username} how are you doing? "


app.run(host="0.0.0.0")

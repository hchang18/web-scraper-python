from flask import Flask, render_template, request, redirect, send_file
from scraper import get_jobs
from save import save_to_file

app = Flask(__name__)

# database to store jobs
# should be outside the route
db = {}


@app.route("/")
def home():
    return render_template("index.html")


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
        print("Download it...")
        word = request.args.get('word')
        if not word:
            raise Exception()
        word = word.lower()
        print("word: ", word)
        jobs = db.get(word)
        print("Job: ", jobs)
        if not jobs:
            raise Exception()
        save_to_file(jobs)
        print("saved the file...")
        return send_file("jobs.csv")
    except:
        # consequence of an error
        print("There is an error downloading")
        return redirect("/")


# decorator below looks for function right under to execute
# @app.route("/contact")
# def contact_me():
#     return "Contact me!"


# dynamic url
# @app.route("/<username>")
# def potato(username):
#     return f"Hello {username} how are you doing? "

if __name__ == '__main__':
    # Threaded option to enable multiple instances for
    # multiple user access support
    app.run(port=5000)

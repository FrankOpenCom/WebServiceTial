from flask import Flask, request, redirect, url_for

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def submisstion():
    if request.method == "GET":
        return app.send_static_file('submit_topic.html')
    else:
        if request.method == "POST":
            print(request.form)
            return redirect(url_for('submit_done'))

@app.route('/submit_done')
def submit_done():
   return app.send_static_file('submit_done.html')

app.run()
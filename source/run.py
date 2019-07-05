from flask import Flask, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def submisstion():
    if request.method == "GET":
        return app.send_static_file('home.html')
    else:
        if request.method == "POST":
            print(request.form)
            return ""


app.run()
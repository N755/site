from flask import Flask, render_template, request 

app = Flask(__name__)

@app.route("/mypage/me")
def about_me():
    return render_template('about_me.html')

@app.route("/mypage/contact")
def contact():
    return render_template('contact.html')


if __name__ == '__main__':
    app.run(debug=True)
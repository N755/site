from flask import Flask, render_template, request 

app = Flask(__name__)

@app.route("/mypage/me")
def about_me():
    return render_template('about_me.html')

@app.route("/mypage/contact")
def contact():
    return render_template('contact.html')

@app.route('/mypage/contact', methods=['GET', 'POST'])
def display_data():
    if request.method == 'POST':
        data = request.form
        print(data)
    return render_template('contact.html')
    


if __name__ == '__main__':
    app.run(debug=True)
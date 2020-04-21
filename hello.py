from flask import Flask, render_template, request, redirect
import csv

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)


def write_database(data):
    with open('./database/mydata.csv', 'a', newline="") as f:
        Email = data['email']
        Subject = data['subject']
        Message = data['message']
        writer = csv.writer(f, delimiter=',',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
        writer.writerow([Email, Subject, Message])


@app.route('/submit_form', methods=['GET', 'POST'])
def submit_form():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            print(data)
            write_database(data)
            return redirect('./thankyou.html')
        except:
            return 'Not Submitted'
    else:
        return 'something went wrong'

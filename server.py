from flask import Flask, render_template, request, redirect, json
import os
import csv
app = Flask(__name__)

@app.route('/<string:page_name>')
def my_home(page_name):
    return render_template(page_name)

@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        # Get the form data
        name = request.form['name']
        email = request.form['email']
        subject = request.form['subject']
        message = request.form['message']

        # Write the data to the text file
        with open("database.txt", "w") as f:
            f.write(f" Name: {name}, Email: {email},Subject:{subject},Message:{message}\n")

        # Write the data to csv file

        with open('some.csv', 'w', newline='') as f:
            fieldnames = ['Name', 'Email', 'Subject', 'Message']
            writer = csv.DictWriter(f, fieldnames=fieldnames, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL, escapechar='\\', lineterminator='\n')
            if f.tell() == 0:
                writer.writeheader()
            writer.writerow({'Name': name, 'Email': email, 'Subject': subject, 'Message': message})


        return redirect("/thankyou.html", code=302)
    else:
        return "Something went wrong. Please try again."
    return "Form submitted.. hoooray."

#
# @app.route('/submit_form', methods=['POST', 'GET'])
# def write_to_csv():
#     if request.method == 'POST':
#         with open("submissions.csv", 'w', newline='') as f:
#             fieldnames = ['email', 'subject', 'message']
#             writer = csv.DictWriter(f, fieldnames=fieldnames)
#
#
#             writer.writerow([
#                 request.form['email'],
#                 request.form['subject'],
#                 request.form['message']
#             ])
#
#         return "Data saved successfully."
#     else:
#         return "Something went wrong. Please try again."

if __name__ == '__main__':
    #app.run(host='127.0.0.1', port=8080, debug=True, load_dotenv=True) you may not need this on non local machines
    app.run()

from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        if request.form.get('action1') == 'Open Project':
            print("Hello im value 1")
        elif  request.form.get('action2') == 'Create Project':
            print("Hello im value 2")
        else:
            pass # unknown
    elif request.method == 'GET':
        return render_template('main_page.html')
    
    return render_template("main_page.html")

if __name__ == "__main__":
    app.run()



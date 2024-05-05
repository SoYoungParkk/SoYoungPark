from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/hotplaces', methods=['POST'])
def hotplaces():
    if request.method == 'POST':
        location = request.form['location']
        return f"입력받은 지역: {location}"

if __name__ == '__main__':
    app.run(debug=True)

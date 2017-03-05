from flask import Flask, render_template, request
import weather
app = Flask(__name__)

@app.route("/")
def index():
    name = request.values.get('name')
    address = request.values.get('address')
    forecast = weather.get_weather(address)
    return render_template('index.html', name=name, forecast=forecast)

@app.route("/about")
def about():
    return render_template('about.html')

if __name__ == "__main__":
    app.run()
from flask import Flask, render_template, request
from crop_recommendation import recommend_crop
from utils.weather import get_weather

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    recommendation = None
    error = None

    if request.method == "POST":
        try:
            N = int(request.form['N'])
            P = int(request.form['P'])
            K = int(request.form['K'])
            ph = float(request.form['ph'])
            rainfall = float(request.form['rainfall'])
            city = request.form['city'].strip()

            temp, humidity = get_weather(city)
            if temp is None or humidity is None:
                error = "Could not fetch weather data for the specified city."
            else:
                recommendation = recommend_crop(N, P, K, temp, humidity, ph, rainfall)

        except Exception as e:
            error = "Invalid input or error processing the request."

    return render_template("index.html", recommendation=recommendation, error=error)

if __name__ == "__main__":
    app.run(debug=True)

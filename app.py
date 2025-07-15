from flask import Flask, render_template, request

app = Flask(__name__)

def calculate_transport_emissions(km_per_week, fuel_efficiency):
    return (km_per_week / fuel_efficiency) * 52 * 2.31

def calculate_electricity_emissions(kwh_per_month):
    return kwh_per_month * 12 * 0.92

def calculate_waste_emissions(waste_kg_per_week):
    return waste_kg_per_week * 52 * 0.45

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        try:
            km_per_week = float(request.form["km_per_week"])
            fuel_efficiency = float(request.form["fuel_efficiency"])
            kwh_per_month = float(request.form["kwh_per_month"])
            waste_kg_per_week = float(request.form["waste_kg_per_week"])

            transport = calculate_transport_emissions(km_per_week, fuel_efficiency)
            electricity = calculate_electricity_emissions(kwh_per_month)
            waste = calculate_waste_emissions(waste_kg_per_week)
            total = transport + electricity + waste

            return render_template("result.html", transport=transport, electricity=electricity, waste=waste, total=total)
        except ValueError:
            return "Please enter valid numbers."

    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)

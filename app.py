from flask import Flask, render_template, request
import pandas as pd
import joblib

app = Flask(__name__)

# Load model & scaler
model = joblib.load("model.pkl")
scaler = joblib.load("scaler.pkl")

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    option = request.form.get("option")

    if option == "manual":
        # Get values from form
        recency = float(request.form["recency"])
        frequency = float(request.form["frequency"])
        monetary = float(request.form["monetary"])

        # Scale and predict
        data = scaler.transform([[recency, frequency, monetary]])
        cluster = model.predict(data)[0]

        return render_template("result.html", cluster=cluster,
                               values=[recency, frequency, monetary])

    elif option == "csv":
        file = request.files["file"]
        if file.filename == "":
            return "No file uploaded"

        df = pd.read_csv(file)

        # Scale and predict
        X_scaled = scaler.transform(df[["Recency", "Frequency", "Monetary"]])
        df["Cluster"] = model.predict(X_scaled)

        # Save result
        df.to_csv("uploaded_results.csv", index=False)

        return render_template("result.html", table=df.head().to_html(classes="table table-striped"),
                               cluster=None)

    return "Invalid Option"

if __name__ == "__main__":
    app.run(debug=True)

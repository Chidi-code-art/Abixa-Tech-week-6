Customer Segmentation Web App

A Flask-based web application for customer segmentation using RFM (Recency, Frequency, Monetary) analysis.
The app leverages a pre-trained clustering model (model.pkl) and a data scaler (scaler.pkl) to categorize customers into meaningful segments.

🚀 Features

Manual Input Prediction: Enter Recency, Frequency, and Monetary values to get a predicted cluster.

Batch Prediction via CSV: Upload a dataset with customer RFM values, and the app will assign clusters for all customers.

Interactive Web Interface: Simple UI built with Flask templates for easy interaction.

Pre-trained Model: Uses a trained machine learning model (model.pkl) with a corresponding scaler (scaler.pkl).

📂 Repository Structure
├── app.py                  # Main Flask application
├── requirements.txt        # Python dependencies
├── model.pkl               # Pre-trained clustering model
├── scaler.pkl              # Pre-trained scaler for input normalization
├── customer_segments.csv   # Example dataset with segment information
├── transactions.csv        # Raw transaction dataset (sample)
├── Untitled.ipynb          # Jupyter notebook for model training/analysis
└── templates/              # HTML templates (index.html, result.html)

⚙️ Installation

Clone the repository:

git clone https://github.com/your-username/customer-segmentation-app.git
cd customer-segmentation-app


Create and activate a virtual environment (optional but recommended):

python -m venv venv
source venv/bin/activate   # On Mac/Linux
venv\Scripts\activate      # On Windows


Install dependencies:

pip install -r requirements.txt

▶️ Usage

Start the Flask app:

python app.py


Open the app in your browser:

http://127.0.0.1:5000


Options:

Manual Mode: Enter values for Recency, Frequency, and Monetary to predict a single cluster.

CSV Mode: Upload a CSV file containing columns: Recency, Frequency, Monetary. The app will generate predictions and save results as uploaded_results.csv.

📊 Example Input (CSV)
Recency,Frequency,Monetary
10,5,200
30,2,50
5,10,500


Output file will include a Cluster column with predicted segment labels.

📖 Model Training

The model (model.pkl) and scaler (scaler.pkl) were generated using the Untitled.ipynb notebook.
They were trained on transactional data (transactions.csv) and segmented customers via clustering on RFM metrics.

🛠️ Tech Stack

Backend: Flask

Machine Learning: scikit-learn

Data Handling: pandas, joblib

🤝 Contributing

Contributions are welcome!
Feel free to submit issues or pull requests for improvements.

📜 License

This project is licensed under the MIT License.

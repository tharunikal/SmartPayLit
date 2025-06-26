from flask import Flask, jsonify
import pandas as pd
from detect_anomalies import detect_anomalies
from router import reroute_transaction

app = Flask(__name__)

@app.route('/')
def process_transactions():
    df = pd.read_csv('transactions.csv')
    df = detect_anomalies(df)
    df['final_gateway'] = df.apply(reroute_transaction, axis=1)
    summary = {
        "total": len(df),
        "anomalies_detected": int(df['anomaly'].sum()),
        "rerouted": int((df['gateway'] != df['final_gateway']).sum())
    }
    return jsonify(summary)

if __name__ == '__main__':
    app.run(debug=True)

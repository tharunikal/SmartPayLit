def reroute_transaction(row):
    if row['anomaly']:
        # Simple fallback logic
        fallback_map = {'A': 'B', 'B': 'C', 'C': 'A'}
        return fallback_map.get(row['gateway'], 'A')
    else:
        return row['gateway']

import pandas as pd
from flask import Flask, jsonify

app = Flask(__name__)

csv_file = 'prompts.csv' 

def extract_prompt(csv_file, role):
    df = pd.read_csv(csv_file)

    for index, row in df.iterrows():
        if row["act"] == role:
            return {"title": row["act"], "description": row["prompt"]}

def extract(csv_file):
    df = pd.read_csv(csv_file)
    dict_prompts = {}

    for index, row in df.iterrows():
        dict_prompts[row["act"]] = row["prompt"]

    return dict_prompts
 


@app.route('/roles/all', methods=['GET'])
def all_roles():
    data = extract(csv_file)
    if data:
        return jsonify(data), 200
    else:
        return jsonify({"error": "Data not found"}), 404



@app.route('/roles', methods=['GET'])
def get_data(role):
    data = extract_prompt(csv_file, role)
    if data:
        return jsonify(data), 200
    else:
        return jsonify({"error": "Data not found"}), 404




if __name__ == '__main__':
    app.run(debug=True)

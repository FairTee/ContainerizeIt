#!/usr/bin/python3

import requests
from flask import jsonify

def fetch_data_from_api(url):
    try:
        response = requests.get(url)
        data = response.json()
        return jsonify(data), 200
    except requests.exceptions.RequestException as e:
        return jsonify({"error": f"Failed to fetch data from API: {str(e)}"}), 500

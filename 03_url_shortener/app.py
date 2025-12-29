from flask import Flask, request, redirect, jsonify
import string
import random
import json
import os

app = Flask(__name__)

DATA_FILE = "urls.json"

# Dosya yoksa oluştur
if not os.path.exists(DATA_FILE):
    with open(DATA_FILE, "w") as f:
        json.dump({}, f)

def load_urls():
    with open(DATA_FILE, "r") as f:
        return json.load(f)

def save_urls(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=4)

def generate_short_code(length=6):
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for _ in range(length))

@app.route("/shorten", methods=["POST"])
def shorten_url():
    data = request.json
    long_url = data.get("url")

    if not long_url:
        return jsonify({"error": "URL missing"}), 400

    urls = load_urls()
    short_code = generate_short_code()

    urls[short_code] = long_url
    save_urls(urls)

    return jsonify({
        "short_url": f"http://127.0.0.1:5000/{short_code}"
    })

@app.route("/<short_code>")
def redirect_url(short_code):
    urls = load_urls()
    long_url = urls.get(short_code)

    if long_url:
        return redirect(long_url)
    return jsonify({"error": "URL not found"}), 404

if __name__ == "__main__":
    app.run(debug=True)

from flask import Flask, jsonify
import subprocess

app = Flask(__name__)

@app.route('/start-server', methods=['GET'])
def start_server():
    try:
        # ✅ Runs main.py in the background
        subprocess.Popen(["python3", "main.py"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        return jsonify({"message": "Aternos server is starting!"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

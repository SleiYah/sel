from flask import Flask, jsonify
import subprocess
import os

app = Flask(__name__)

@app.route('/start-server', methods=['GET'])
def start_server():
    try:
        # ✅ Ensure Chrome & ChromeDriver are installed before running `main.py`
        install_chrome()

        # ✅ Run `main.py` in the background
        subprocess.Popen(["python3", "main.py"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        return jsonify({"message": "Aternos server is starting!"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def install_chrome():
    """✅ Installs Chrome & ChromeDriver if not installed"""
    if not os.path.exists("/usr/bin/google-chrome"):
        print("🔧 Installing Chrome & ChromeDriver...")
        os.system("sudo apt update && sudo apt install -y google-chrome-stable")
        os.system("sudo apt install -y chromedriver")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

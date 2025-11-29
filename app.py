from flask import Flask, request
import requests

app = Flask(__name__)

# Google Apps Script WebApp URL
GOOGLE_URL = "https://script.google.com/macros/s/AKfycbyxlsF4wXk1OXDcY6tQNQMRDUXkcVD-u-4hJHjp86cN9IsDquuNSB0g1Y3DusjM_EvS/exec"

@app.route("/relay", methods=["POST"])
def relay():
    try:
        payload = request.data

        # LOG incoming JSON to Render logs
        print("=== Incoming payload ===")
        print(payload.decode())

        headers = {'Content-Type': 'application/json'}
        response = requests.post(GOOGLE_URL, data=payload, headers=headers, timeout=10)

        return response.text
    except Exception as e:
        print("Relay error:", str(e))
        return f"Error: {str(e)}", 500



if __name__ == "__main__":
    # Render requires host 0.0.0.0 and port 8080
    app.run(host="0.0.0.0", port=8080)

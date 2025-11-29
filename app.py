from flask import Flask, request
import requests

app = Flask(__name__)

# Google Apps Script WebApp URL
GOOGLE_URL = "https://script.google.com/macros/s/AKfycbyxlsF4wXk1OXDcY6tQNQMRDUXkcVD-u-4hJHjp86cN9IsDquuNSB0g1Y3DusjM_EvS/exec"

@app.route("/relay", methods=["POST"])
def relay():
    try:
        # Read raw JSON payload from SIM900
        payload = request.data.decode("utf-8")  # decode bytes to string

        # Log the payload to Render console
        print(f"[SIM900 Payload Received]: {payload}")

        # Forward the payload to Google Apps Script
        headers = {'Content-Type': 'application/json'}
        response = requests.post(GOOGLE_URL, data=payload, headers=headers, timeout=10)

        # Log Google Script response
        print(f"[Google Script Response]: {response.text}")

        # Return the Google Script response back to SIM900
        return response.text
    except Exception as e:
        print(f"[Error]: {str(e)}")
        return f"Error: {str(e)}", 500


if __name__ == "__main__":
    # Render requires host 0.0.0.0 and port 8080
    app.run(host="0.0.0.0", port=8080)

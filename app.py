from flask import Flask, request
import requests

app = Flask(__name__)

# Your Google Apps Script WebApp URL
GOOGLE_URL = "https://script.google.com/macros/s/AKfycbyxlsF4wXk1OXDcY6tQNQMRDUXkcVD-u-4hJHjp86cN9IsDquuNSB0g1Y3DusjM_EvS/exec"

@app.route("/relay", methods=["POST"])
def relay():
    try:
        # Read raw JSON payload from SIM900
        payload = request.data

        # Forward the payload to Google Apps Script
        headers = {'Content-Type': 'application/json'}
        response = requests.post(GOOGLE_URL, data=payload, headers=headers, timeout=10)

        # Return the Google Script response back to SIM900
        return response.text
    except Exception as e:
        return f"Error: {str(e)}", 500

if __name__ == "__main__":
    # Render requires 0.0.0.0 host
    app.run(host="0.0.0.0", port=8080)

// // Receives POST from SIM900 and forwards to Google Apps Script

// $google_url = "https://script.google.com/macros/s/YOUR_SCRIPT_ID/exec";

// $input = file_get_contents("php://input");

// $ch = curl_init($google_url);
// curl_setopt($ch, CURLOPT_POST, 1);
// curl_setopt($ch, CURLOPT_POSTFIELDS, $input);
// curl_setopt($ch, CURLOPT_HTTPHEADER, array('Content-Type: application/json'));
// curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);

// $response = curl_exec($ch);
// curl_close($ch);

// echo $response;
// ?>

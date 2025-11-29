<?php
// Receives POST from SIM900 and forwards to Google Apps Script

$google_url = "https://script.google.com/macros/s/YOUR_SCRIPT_ID/exec";

$input = file_get_contents("php://input");

$ch = curl_init($google_url);
curl_setopt($ch, CURLOPT_POST, 1);
curl_setopt($ch, CURLOPT_POSTFIELDS, $input);
curl_setopt($ch, CURLOPT_HTTPHEADER, array('Content-Type: application/json'));
curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);

$response = curl_exec($ch);
curl_close($ch);

echo $response;
?>

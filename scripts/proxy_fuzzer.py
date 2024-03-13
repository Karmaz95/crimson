import ssl
import os
import subprocess
from flask import Flask, request, Response

app = Flask(__name__)

# Global variable to keep track of used payloads
used_payloads = set()

# Define the route for receiving GET requests to /fuzz_radamsa
@app.route('/fuzz_radamsa', methods=['GET', 'POST', 'DELETE', 'PATCH'])
def fuzz_radamsa():
    # Read the base payload from the file payload.bin
    with open('payload.bin', 'rb') as f:
        base_payload = f.read()

    # Generate a fuzzed payload using Radamsa
    fuzzed_payload = generate_fuzzed_payload(base_payload)

    # Return the fuzzed payload as the response
    return Response(fuzzed_payload, mimetype='text/plain')

# Define the route for receiving GET requests to /fuzz_wordlist
@app.route('/fuzz_wordlist', methods=['GET', 'POST', 'DELETE', 'PATCH'])
def fuzz_wordlist():
    # Read payloads from payloads.txt if not all payloads have been used
    if len(used_payloads) < count_lines_in_file('payloads.txt'):
        payload = get_next_payload_from_wordlist()
        used_payloads.add(payload)
        return Response(payload, mimetype='text/plain')
    else:
        return "ALL PAYLOADS SENT"

# Function to generate a fuzzed payload using Radamsa
def generate_fuzzed_payload(base_payload):
    # Call Radamsa to generate a fuzzed payload
    radamsa_process = subprocess.Popen(['radamsa'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    radamsa_output, radamsa_error = radamsa_process.communicate(input=base_payload)

    # Check for any errors
    if radamsa_error:
        print("Radamsa error:", radamsa_error.decode())
        return "Error occurred while fuzzing payload"

    # Return the fuzzed payload
    return radamsa_output.decode()

# Function to get the next payload from the wordlist
def get_next_payload_from_wordlist():
    with open('payloads.txt', 'r') as f:
        for line in f:
            payload = line.strip()
            if payload not in used_payloads:
                return payload
    return ""

# Function to count lines in a file
def count_lines_in_file(filename):
    with open(filename, 'r') as f:
        return sum(1 for _ in f)

if __name__ == '__main__':
    # Set up SSL context with certificate and private key
    ssl_context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
    ssl_context.load_cert_chain(certfile='/etc/letsencrypt/live/MY_COLAB/fullchain.pem', keyfile='/etc/letsencrypt/live/MY_COLAB/privkey.pem')

    # Run the Flask app with SSL support using the created SSL context
    app.run(ssl_context=ssl_context, host='0.0.0.0', port=443, debug=True)

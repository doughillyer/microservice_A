# Author: Doug Hillyer
# Date: 8-8-2024
# Course: CS361 - Software Engineering
# Assignment: Microservice A - Newsletter Sign-Up

# Description:
# This microservice allows users to manage their subscription to a newsletter. 
# Users can add their email address to the newsletter list or remove it if they 
# no longer wish to receive emails. The email addresses are stored in a text 
# file to ensure persistence.

# Usage:
# - The service listens on port 5556 for incoming requests.
# - It expects a JSON object with two fields: 'action' (add/remove) and 'email' (the user's email address).
# - It responds with a confirmation message indicating the success or failure of the requested action.

# Requirements:
# - Python 3.x
# - ZeroMQ library (pyzmq)

import zmq
import os
import json

NEWSLETTER_FILE = "newsletter_list.txt"

# Function to load the newsletter list
def load_newsletter_list():
    if os.path.exists(NEWSLETTER_FILE):
        with open(NEWSLETTER_FILE, "r") as f:
            return json.load(f)
    else:
        return []

# Function to save the newsletter list
def save_newsletter_list(newsletter_list):
    with open(NEWSLETTER_FILE, "w") as f:
        json.dump(newsletter_list, f)

# Set up the ZeroMQ context and REP socket
context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:5556")  # Use a different port than the login service

print("Newsletter service is running...")

while True:
    # Wait for a request from the client
    message = socket.recv_json()
    print(f"Received request: {message}")

    action = message.get("action")
    email = message.get("email")

    response = {}

    newsletter_list = load_newsletter_list()

    if action == "add":
        if email not in newsletter_list:
            newsletter_list.append(email)
            save_newsletter_list(newsletter_list)
            response["status"] = "success"
            response["message"] = "Email added to the newsletter."
        else:
            response["status"] = "exists"
            response["message"] = "Email already in the newsletter."
    elif action == "remove":
        if email in newsletter_list:
            newsletter_list.remove(email)
            save_newsletter_list(newsletter_list)
            response["status"] = "success"
            response["message"] = "Email removed from the newsletter."
        else:
            response["status"] = "not_found"
            response["message"] = "Email not found in the newsletter."

    # Send the response back to the client
    socket.send_json(response)

# Author: Doug Hillyer
# Date: 8-8-2024
# Course: CS361 - Software Engineering
# Assignment: Microservice A - Newsletter Sign-Up CLI

# Description:
# This command-line interface (CLI) program allows users to interact with the 
# Newsletter Sign-Up microservice. Users can add their email to the newsletter 
# list or remove it from the list. The program provides clear instructions and 
# feedback based on the user's actions.

# Usage:
# - The user is prompted to select an action: add, remove, or exit.
# - After selecting an action, the user is prompted to enter their email address.
# - The program sends the request to the microservice and displays the response message.

# Requirements:
# - Python 3.x
# - ZeroMQ library (pyzmq)
# - The Newsletter Sign-Up microservice must be running on localhost:5556.

import zmq

def manage_newsletter(action, email):
    context = zmq.Context()
    socket = context.socket(zmq.REQ)
    socket.connect("tcp://localhost:5556")  # Connect to the newsletter service

    request = {
        "action": action,
        "email": email
    }

    # Send the request to the microservice
    socket.send_json(request)

    # Receive the response from the microservice
    response = socket.recv_json()
    print(response["message"])

    context.term()

def print_instructions():
    print("Welcome to the Newsletter Signup!")
    print("You can use this tool to manage your subscription to our newsletter.")
    print("Please follow the instructions below:")
    print("1. To add your email to the newsletter list, type: add")
    print("2. To remove your email from the newsletter list, type: remove")
    print("3. To exit the program, type: exit")
    print()

def main():
    print_instructions()

    while True:
        action = input("Enter your action (add/remove/exit): ").strip().lower()

        if action == "exit":
            print("Goodbye!")
            break
        elif action not in ["add", "remove"]:
            print("Invalid action. Please try again.")
            continue

        email = input("Enter your email address: ").strip()

        manage_newsletter(action, email)

if __name__ == "__main__":
    main()

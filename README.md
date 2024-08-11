# Newsletter Sign-Up Microservice and CLI

## Overview

This project consists of a microservice (`newsletter_service.py`) and a command-line interface (CLI) program (`newsletter_cli.py`) that allows users to manage their subscription to a newsletter. Users can add or remove their email addresses from the newsletter list, which is stored in a text file for persistence.

## Microservice: `newsletter_service.py`

### Description

The `newsletter_service.py` microservice handles requests to add or remove email addresses from a newsletter subscription list. The service listens on a specified port and interacts with a text file that stores the list of subscribed email addresses.

### Features

- **Add Email:** Users can add their email address to the subscription list.
- **Remove Email:** Users can remove their email address from the subscription list.
- **Persistent Storage:** The list of email addresses is stored in a text file to ensure data persistence across sessions.

### Requirements

- Python 3.x
- ZeroMQ library (`pyzmq`)

### Usage

1. **Running the Microservice:** 
   - Ensure you have Python 3.x and the ZeroMQ library installed.
   - Run the microservice using the command: `python newsletter_service.py`.
   - The service will start listening on port `5556` for incoming requests.

2. **Request Format:**
   - The service expects a JSON object with the following format:
     ```json
     {
       "action": "add" | "remove",
       "email": "user@example.com"
     }
     ```
   - The `action` field specifies whether the email should be added or removed from the list.
   - The `email` field contains the user's email address.

3. **Response:**
   - The service responds with a confirmation message indicating the success or failure of the action.

### Example
```python
{
  "action": "add",
  "email": "example@example.com"
}

# Libs
import random
import time
from datetime import datetime
import requests
import logging
import json

# Setup logging for docker contaier
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Open config
def open_config():
    with open('config.json', 'r') as file:
        return json.load(file)

    
# Send Message
def send_message(channel_id, message, oauth):
    # Set url
    url = f"https://discord.com/api/v9/channels/{channel_id}/messages"
    # Auth
    headers = {
        'Authorization': oauth,
        'Content-Type': 'application/json'
    }
    # Message
    payload = {
        'content': message
    }
    # Send request
    response = requests.post(url, json=payload, headers=headers)
    # Return status code
    return(response.status_code)


# Roll trough all messages and send
def roll_messages():
    for entry in config:
        if entry["enable"]:  # Check if enabled
            # Set all varibles
            auth = entry['auth']
            channel = entry['channel']
            message = entry['message']
            wait = entry['wait']
            # Send the message
            r = send_message(channel, message, auth)
            # Check for succes
            if {r == 200}:
                logger.info("succes")
                logger.info(f"Send message {message} in channel_id {channel}")
            else:
                logger.error("An error has happend. Error code:")
                logger.error(r)
            # Wait for delay
            logger.info(f"waiting {wait} seconds")
            time.sleep(wait)


# Main stuff
if __name__ == "__main__":
    # Loading config
    global config
    logger.info("Loading config")
    config = open_config()
    logger.info("Loaded config")
    # Rolling messages on start
    roll_messages()

    # Main loop
    while True:
        # Generate random number in minutes.
        # CHANGE THIS TO CHANGE DELAY BETWEEN MESSAGES
        wait_time = random.randint(60, 160) * 60
       
        # You can also set this to be persistent. Just uncomment the line below
        #wait_time = 1

        # Log time
        logger.info(f"Waiting for {wait_time // 60} minutes...")

        # Wait time
        time.sleep(wait_time)

        # Roll trough messages
        roll_messages()
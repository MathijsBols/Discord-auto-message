
# Discord auto message

This is a project i made to automatically send discord message. I made this because there werent realy any projects that could send multiple messages in multiple channels!


## Deployment - Docker

Run the docker image from my docker page!


  [Docker Image](https://github.com/MathijsBols/Discord-auto-message) 
  from dockerhub

  ## Deployment - Python

Install dependencies

```bash 
pip install requests logging
```

Run python script
```bash 
python messages.py
```



## Configuration

To set up the automated messaging, use the following JSON structure in your configuration file:

```json
[
    {
        "enable": true,
        "auth": "PUT DISCORD TOKEN HERE",
        "channel": "PUT CHANNEL ID HERE",
        "message": "PUT MESSAGE HERE",
        "wait": 5
    },
    {
        "enable": true,
        "auth": "PUT DISCORD TOKEN HERE",
        "channel": "PUT CHANNEL ID HERE",
        "message": "PUT MESSAGE HERE",
        "wait": 5
    }
]
```
You are able to put in as many sections as wanted
## Authors

- [@MathijsBols](https://github.com/MathijsBols)


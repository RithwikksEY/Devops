from fastapi import FastAPI
import os
import socket
import time
import datetime

app = FastAPI()
START_TIME = time.time()

@app.get("/health")
def health():
    return {"status": "healthy"}

@app.get("/info")
def info():
    return {
        "app": os.getenv("APP_NAME", "cloud-native-devops"),
        "env": os.getenv("ENV", "dev"),
        "host": socket.gethostname(),
        "uptime_seconds": int(time.time() - START_TIME)
    }

@app.get("/time")
def current_time():
    return {
        "utc_time": datetime.datetime.utcnow().isoformat() + "Z"
    }

@app.get("/config")
def config():
    return {
        "app_name": os.getenv("APP_NAME", "Use-case-demo"),
        "environment": os.getenv("ENV", "Cloud")
    }

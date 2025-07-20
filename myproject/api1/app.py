from flask import Flask, request
import requests
import time
import uuid
from logger_config import get_logger

app = Flask(__name__)
logger = get_logger("API1")

@app.route('/api1')
def api1_handler():
    user_id = 1
    req_id = str(uuid.uuid4())
    start_time = time.time()

    logger.info("Received request",
        extra={"source": "API1", "user_id": user_id, "req_id": req_id, "status": 0, "duration": 0})

    try:
        res = requests.get("http://api2:5001/api2", params={"req_id": req_id})
        duration = int((time.time() - start_time) * 1000)

        logger.info(f"Got response from API2: {res.text}",
            extra={"source": "API1", "user_id": user_id, "req_id": req_id, "status": res.status_code, "duration": duration})

        return f"API1 -> API2 says: {res.text}"

    except Exception as e:
        duration = int((time.time() - start_time) * 1000)
        logger.error(f"Error calling API2: {e}",
            extra={"source": "API1", "user_id": user_id, "req_id": req_id, "status": 500, "duration": duration})
        return "Internal Server Error", 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

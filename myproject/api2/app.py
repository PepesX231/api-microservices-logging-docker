from flask import Flask, request
import time
from logger_config import get_logger

app = Flask(__name__)
logger = get_logger("API2")

@app.route('/api2')
def api2_handler():
    user_id = 1
    req_id = request.args.get("req_id", "unknown")
    start_time = time.time()

    duration = int((time.time() - start_time) * 1000)
    logger.info("API2 received request",
        extra={"source": "API2", "user_id": user_id, "req_id": req_id, "status": 200, "duration": duration})

    return "Hello from API2"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)


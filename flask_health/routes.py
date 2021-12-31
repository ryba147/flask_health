import time
from datetime import datetime, timedelta

from flask import Blueprint, jsonify, g, request

from flask_health.logging import logger

common_bp = Blueprint('common_bp', __name__)


# 1. Separate for each Blueprint ?
# 2. Log the name of a Blueprint request was made from ?
# 3. Import created object or make a logger factory ?
#  3.1. def createLogger(name): return getLogger(name) ? singleton ?
@common_bp.before_app_request
def before_app_request():
    g.REQUEST_START_TIME = time.perf_counter()


@common_bp.after_app_request
def after_app_request(response):
    elapsed_time = time.perf_counter() - g.REQUEST_START_TIME
    now = datetime.now()
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")

    logger.info('[{}] "{} {}?{}" finished with status code {}. Time elapsed: {}'.format(dt_string,
                                                                                        request.method,
                                                                                        request.path,
                                                                                        request.query_string.decode('utf-8'),
                                                                                        response.status_code,
                                                                                        timedelta(seconds=elapsed_time)))
    return response


@common_bp.route('/')
def home():
    response = {"status": "ok"}
    return jsonify(response)

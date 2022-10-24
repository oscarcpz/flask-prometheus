#!/usr/bin/env python
# -*- coding: utf-8 -*-
from datetime import datetime

from flask import Flask, request, jsonify, render_template
from loguru import logger
from prometheus_flask_exporter import PrometheusMetrics

from configurations.constants import DATE_FORMAT_LOG
from configurations.logger import LOG
from configurations.server import SERVER
from utilities.flask_helper import access

app = Flask(__name__)
metrics = PrometheusMetrics(app)

metrics.info('app_info', 'Flask Prometheus Example', version='1.0.0')


@app.route("/", methods=['GET', 'POST'])
def root():
    access(request)
    return jsonify(
        message=datetime.now().strftime(DATE_FORMAT_LOG)
    )


@app.get("/greetings/<string:name>", defaults={'response_format': 'html'})
@app.get("/greetings/<string:name>/<string:response_format>")
@metrics.counter('invocation_by_response_format', 'Number of invocations by response format',
                 labels={'item_format': lambda: request.view_args['response_format']})
@metrics.summary('requests_by_status', 'Request latencies by status',
                 labels={'status': lambda r: r.status_code})
def hi(name: str, response_format: str):
    access(request)
    if 'html' in response_format:
        info = dict()
        info['name'] = name
        info['time'] = datetime.now().strftime(DATE_FORMAT_LOG)
        return render_template('greetings.html', info=info)
    else:
        return jsonify(message=f"Hi {name}", time=datetime.now().strftime(DATE_FORMAT_LOG))


if __name__ == '__main__':
    logger.remove()  # eliminamos el log por defecto
    logger.configure(**LOG)
    app.run(**SERVER)


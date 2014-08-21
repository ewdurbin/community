
import json
import logging
import os

import requests

from flask import Flask
from flask import jsonify

logger = logging.StreamHandler()

APP = Flask(__name__)

DEPENDENCIES_STRING = os.getenv('COMMUNITY_MEMBERS', '')
DEPENDENCIES = {}

for dependency in DEPENDENCIES_STRING.split('|'):
    name, health_url = dependency.split(',')
    DEPENDENCIES[name] = health_url


def get_status(dependency_status_url):
    url = '/'.join([dependency_status_url, 'status'])
    r = requests.get(url, timeout=1)
    return (r.status_code, r.json())


def get_details(dependency_status_url):
    url = '/'.join([dependency_status_url, 'details'])
    r = requests.get(url, timeout=1)
    return (r.status_code, r.json())


def compute_status():
    status_codes = []
    for name, health_url in DEPENDENCIES.items():
        status_codes.append(get_status(health_url)[0])
    if max(status_codes) == 500:
        return 'UNHEALTHY'
    return 'HEALTHY'


def compute_details():
    status_codes = []
    details = {}
    services = {}
    for name, health_url in DEPENDENCIES.items():
        status_code, info = get_details(health_url)
        status_codes.append(status_code)
        details[name] = info['details']
        services[name] = info['services']
    if max(status_codes) == 500:
        return 'UNHEALTHY', details, services
    return 'HEALTHY', details, services


@APP.route('/', methods=['GET'])
def root_route():
    body = {"title": "community server"}
    return jsonify(body)


@APP.route('/health/status')
def health_status_route():
    body = {"status": compute_status()}
    return json.dumps(body).replace(' ', '')


@APP.route('/health/details')
def health_details_route():
    status, details, services = compute_details()
    body = {"status": status, "services": services, "details": details}
    return jsonify(body)


if __name__ == "__main__":
    APP.run(debug=True)

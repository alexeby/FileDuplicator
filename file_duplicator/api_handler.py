import requests
import logging

logger = logging.getLogger(__name__)


def get_api_data(api_endpoint: str):
    try:
        r = requests.get(api_endpoint, timeout=5)
        return r.json()['results']
    except requests.exceptions.Timeout:
        logger.exception(requests.exceptions)

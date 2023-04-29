import requests

BASE_URL = 'http://localhost:5000/'


def get_form():
    return requests.get(BASE_URL)


def post_form(height=None, width=None, matrix_data=None):
    post_data = {'height': height, 'width': width, 'matrix_data': matrix_data}
    return requests.post(BASE_URL, data=post_data)

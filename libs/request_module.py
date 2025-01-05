import urequests as request
import ujson
import json



def send_post_request(headers, body, url):
    headers = headers
    body = body
    json_file = json.dumps(body)
    res = request.post (url = url, json = json_file, headers = headers)
    return res
    
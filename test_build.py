from flask import Flask, render_template, send_from_directory, request
import os
import json

app = Flask(__name__)


def split_url(path):
    parts_of_path = path.split('/')
    # get the file
    requested_file = parts_of_path[len(parts_of_path)-1]
    # get everything but the requested file
    parts_of_path.remove(requested_file)
    folder = '/'.join(parts_of_path)
    return [folder, requested_file]

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    if path == '' or path == '/':
        requested_file = 'index.html'
    else:
        requested_file = split_url(path)[1]

    folder = split_url(path)[0]
    return send_from_directory(f'build/{folder}', requested_file)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5001, debug=True)

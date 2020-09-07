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


def template_exists(path):
    if path == '' or path == '/':
        if os.path.exists('./templates/pages/index.html'):
            return './pages/index.html'
    else:
        if os.path.exists('./templates/pages/' + path):
            return './pages/' + path
    return False


@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    # check if there is a template for the request
    template = template_exists(path)
    if template != False:
        return render_template(template)
    else:
        if path == '' or path == '/':
            requested_file = 'index.html'
        else:
            requested_file = split_url(path)[1]

        folder = split_url(path)[0]
        return send_from_directory(folder, requested_file)


@app.route('/blog.html')
def blog():
    posts = []
    for post in os.listdir('./blog/posts/'):
        with open('./blog/posts/'+post) as json_file:
            post_json = json.load(json_file)
            posts.append(post_json)
    return render_template('./pages/blog.html',
                           posts=posts)


@app.route('/blog/<post>')
def blog_post(post):
    # remove .html and add .json
    post = post[:-5] + '.json'
    with open('./blog/posts/'+post) as json_file:
        post_json = json.load(json_file)
    return render_template('./pages/post.html',
                           post=post_json)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)

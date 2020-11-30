# -*- coding: utf-8 -*-

from flask import Flask

flask_app = Flask(__name__)


@flask_app.route('/')
def hello_world():
    return 'Hello Flask!'


@flask_app.route('/hello')
def hello():
    return 'Hello, World'


@flask_app.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    return 'User %s' % username


@flask_app.route('/post/<int:post_id>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return 'Post %d' % post_id


if __name__ == '__main__':
    '''Boot the micro-service'''
    flask_app.run(host='localhost', port=8080, debug=True)

# Copyright 2018 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import datetime

from flask import *
from flask.helpers import url_for
from google.auth.transport import requests
from google.cloud import datastore, storage
import google.oauth2.id_token

datastore_client = datastore.Client()
datastore_storage = storage.Client()

app = Flask(__name__)

# def store_time(email, dt):
#     entity = datastore.Entity(key=datastore_client.key('User', email, 'visit'))
#     entity.update({
#         'timestamp': dt
#     })

#     datastore_client.put(entity)


#     return times
# [END gae_python3_datastore_store_and_fetch_user_times]
# [END gae_python38_datastore_store_and_fetch_user_times]

app.secret_key = "0123456789"
# bucket = storage.get_bucket("s3793263-storage")

def check_login(user, password):
    query = datastore_client.query(kind = "user")
    a = query.add_filter("id", "=", user)
    a = query.add_filter("password", "=", password)
    return len(list(a.fetch()))

@app.route('/post_message')
def post_message():
    return render_template('message_post.html')

@app.route('/posted_message', methods = ['POST'])
def posted_message():
    if request.method == 'POST':
        return "posted"




@app.route('/upload', methods = ['POST'])
def upload_file():
   if request.method == 'POST':
      f = request.files['file']
      f.save(f.filename)
      return 'file uploaded successfully'

@app.route('/logout')
def logout():
    session.pop('id', None)  
    return render_template('login.html')


@app.route('/register')
def register():
    return render_template('register.html')

@app.route('/back')
def back():
    return render_template('forum.html')

@app.route('/register_user', methods = ['POST'])
def register_user():
    if request.method == 'POST':
        id = request.form['id']
        username = request.form['user']
        password = request.form['password']
        result = insert_new_user(id, username, password)
        if (result != "success"):
            return render_template('register.html', invalid = result)
        else:
            return render_template('login.html')

def insert_new_user(id, username, password):
    query1 = datastore_client.query(kind = "user")
    query2 = datastore_client.query(kind = "user")
    a = query1.add_filter("id", "=", id)
    b = query2.add_filter("user_name", "=", username)
    result1 = list(a.fetch())
    result2 = list(b.fetch())
    length1 = len(result1)
    length2 = len(result2)
    if (length1 == 0 and length2 == 0):
        entity = datastore.Entity(key = datastore_client.key('user'))
        entity.update({
            'id' : id,
            'user_name' : username,
            'password' : password
        })
        datastore_client.put(entity)
        return "success"
    elif (length1 > 0 and result1[0]["id"] == id ):
        return "id already exists"
    elif (length2 > 0 and result2[0]["user_name"] == username):
        return "username already exists"


@app.route('/login', methods = ['POST'])
def login():
    if request.method == 'POST':
        username = request.form['user']
        password = request.form['password']
        result = check_login(username,password)
        if (result == 0):
            return render_template('login.html', invalid = "ID or password is invalid")
        else:
            session['user'] = username
            app.logger.info(session['user'])
            return render_template('forum.html')

#starting point of the application
@app.route('/')
def root():

    # if id_token:
    #     try:
    #         # Verify the token against the Firebase Auth API. This example
    #         # verifies the token on each page load. For improved performance,
    #         # some applications may wish to cache results in an encrypted
    #         # session store (see for instance
    #         # http://flask.pocoo.org/docs/1.0/quickstart/#sessions).
    #         claims = google.oauth2.id_token.verify_firebase_token(
    #             id_token, firebase_request_adapter)

    #         store_time(claims['email'], datetime.datetime.now())
    #         times = fetch_times(claims['email'], 10)

    #     except ValueError as exc:
    #         # This will be raised if the token is expired or any other
    #         # verification checks fail.
    #         error_message = str(exc)

    return render_template('login.html')



if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)

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


from flask import *
import datetime
from flask.helpers import url_for
from google.auth.transport import requests
from google.cloud import datastore, storage
from google.cloud.storage import client

datastore_client = datastore.Client()
datastore_storage = storage.Client()

app = Flask(__name__)

app.secret_key = "0123456789"

def check_login(user, password):
    query = datastore_client.query(kind = "user")
    a = query.add_filter("id", "=", user)
    a = query.add_filter("password", "=", password)
    result_list = list(a.fetch())
    if (len(result_list) > 0):
        session['username'] = result_list[0]['user_name']
        session['image'] = result_list[0]['image']
        session['password'] = result_list[0]['password']
    return len(result_list)

@app.route('/check_password', methods = ['POST'])
def check_password(): 
    if request.method == 'POST':
        id = session['username']
        currentPassword = request.form['currentPassword']
        newpassword = request.form['newPassword']
        result = check_db(id, currentPassword, newpassword)
    if result:
        session.clear() 
        return render_template('login.html')
    else:
        return render_template('edit_password.html', user_name =  session['username'], image = session['image'], invalid = "The old password is incorrect")

def check_db(id, currentPassword, newpassword):
    query = datastore_client.query(kind = "user")
    a = query.add_filter("user_name", "=", id)
    a = query.add_filter("password", "=", currentPassword)
    if(len(list(a.fetch())) > 0):
        query = datastore_client.query(kind = "user")
        a = query.add_filter("user_name", "=", id)
        a = query.add_filter("password", "=", currentPassword)
        result = list(a.fetch())
        id = result[0].id
        query = datastore_client.key('user', id)
        user = datastore_client.get(query)
        user["password"] = newpassword
        temp = datastore_client.put(user)
        return True
    else:
        return False
    


@app.route('/user_post_area')
def user_post_area(): 
    return render_template('user_post_area.html', user_name =  session['username'], image = session['image'])


@app.route('/post_message')
def post_message():
    return render_template('message_post.html', user_name =  session['username'], image = session['image'])

@app.route('/edit_a_post', methods = ['POST'])
def edit_a_post():
    if request.method == 'POST':
        subject = request.form.get('post_subject')
        message = request.form.get('post_message')
        image = request.form.get('post_image')
        session['post_subject'] = subject
        session['post_message'] = message
    return render_template('edit_a_post.html', imagePreview2 = image, post_subject = subject, post_message = message, user_name =  session['username'], image = session['image'])

@app.route('/update_post', methods = ['POST'])
def update_post():
    if request.method == 'POST':
        subject = request.form['subject']
        message = request.form['message']
        file = request.files.get('upload')
        app.logger.info(subject)
        app.logger.info(message)
        bucket = datastore_storage.get_bucket("s3793263-storage")
        blob = bucket.blob(file.filename)
        blob.upload_from_string(
        file.read(),
        content_type = file.content_type
        ) 
        app.logger.info(blob.public_url)
        insert_updated_post(subject,message, blob.public_url)
        result = get_messages()
        return render_template('all_posts.html', user_name =  session['username'], image = session['image'], posts = result)

def insert_updated_post(subject,message, image_url):
    query = datastore_client.query(kind = "posts")
    a = query.add_filter("user_id", "=", session['username'])
    a = query.add_filter("subject", "=", session['post_subject'])
    a = query.add_filter("message", "=", session['post_message'])
    result = list(a.fetch())
    id = result[0].id
    app.logger.info(id)
    complete_key = datastore_client.key("posts", id)

    task = datastore.Entity(key=complete_key)

    task.update(
    {
        "user_id": session['username'],
        "subject": subject,
        "message": message,
        "image": image_url,
        "post_date": datetime.datetime.now()
    }
    )
    datastore_client.put(task)



def insert_post(subject,message, image_url):
    entity = datastore.Entity(key = datastore_client.key('posts')) 
    entity.update({
        'subject' : subject,
        'message' : message,
        'image' : image_url,
        'user_id' : session['username'],
        'post_date' : datetime.datetime.now()
    })
    datastore_client.put(entity)
    return "success"

@app.route('/edit_password')
def edit_password():
    return render_template('edit_password.html', user_name =  session['username'], image = session['image'])

@app.route('/posted_message', methods = ['POST'])
def posted_message():
    if request.method == 'POST':
        subject = request.form['subject']
        message = request.form['message']
        uploaded_file = request.files.get('upload')
        bucket = datastore_storage.get_bucket("s3793263-storage")
        blob = bucket.blob(uploaded_file.filename)
        blob.upload_from_string(
        uploaded_file.read(),
        content_type = uploaded_file.content_type
        ) 
        result = insert_post(subject, message, blob.public_url)
    return "posted"


@app.route('/upload', methods = ['POST'])
def upload_file():
   if request.method == 'POST':
      f = request.files['file']
      f.save(f.filename)
      return 'file uploaded successfully'


@app.route('/logout')
def logout():
    session.clear() 
    # app.logger.info(session['username']) 
    return render_template('login.html')


@app.route('/register')
def register():
    return render_template('register.html')

@app.route('/message_display')
def message_display():
    result = get_messages()
    return render_template('all_posts.html', user_name =  session['username'], image = session['image'], posts = result)

def get_messages():
    query = datastore_client.query(kind = "posts")
    query.order = ["-post_date"]
    result = list(query.fetch(limit=10))
    return result

@app.route('/edit_post')
def edit_post():
    result = get_my_posts(session['username'])
    app.logger.info(result)
    return render_template('edit_post.html', user_name =  session['username'], image = session['image'],posts = result)

def get_my_posts(user):
    query = datastore_client.query(kind = "posts")
    a = query.add_filter("user_id", "=", user)
    result = list(a.fetch())
    return result

@app.route('/back')
def back():
    return render_template('forum.html', user_name =  session['username'], image = session['image'])

@app.route('/register_user', methods = ['POST'])
def register_user():
    if request.method == 'POST':
        id = request.form['id']
        username = request.form['user']
        password = request.form['password']
        uploaded_file = request.files.get('upload')
        bucket = datastore_storage.get_bucket("s3793263-storage")
        blob = bucket.blob(uploaded_file.filename)
        blob.upload_from_string(
        uploaded_file.read(),
        content_type = uploaded_file.content_type
        ) 
        result = insert_new_user(id, username, password, blob.public_url)
        if (result != "success"):
            return render_template('register.html', invalid = result)
        else:
            return render_template('login.html')

def insert_new_user(id, username, password, file_url):
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
            'password' : password,
            'image' : file_url
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
            return render_template('forum.html',user_name =  session['username'], image = session['image'])

#starting point of the application
@app.route('/')
def root():
    return render_template('login.html')



if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)

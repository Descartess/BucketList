""" Views.py """
from flask import render_template, redirect, url_for, request 

from app import APP
from bucketList import Application

BUCKETLIST = Application()

@APP.route('/',methods = ['POST', 'GET'])
def index():
    if request.method == "POST":
        global BUCKETLIST
        login_data = request.form
        BUCKETLIST.signup(login_data['username'], login_data['password'])
        return redirect(url_for('home',username = BUCKETLIST.current_user.username ))
    return render_template("login.html")

@APP.route('/signup')
def signup():
    return render_template("signup.html")

@APP.route('/home/<username>')
def home(username):
    global BUCKETLIST
    return render_template("home.html", data=BUCKETLIST.current_user)
 

@APP.route('/home/create', methods = ["POST","GET"])
def createbucketlist():
    global BUCKETLIST
    if request.method == "POST":
        bucketlist = request.form
        BUCKETLIST.current_user.add_bucketlist(bucketlist['b_listname'],int(bucketlist['completed_by']))
        return redirect(url_for('home',username=BUCKETLIST.current_user.username))
    return render_template("createBucketList.html", data=BUCKETLIST.current_user)

@APP.route('/home/bucketlist/<int:b_id>')
def viewbucketlist(b_id):
    global BUCKETLIST
    user_b_list = BUCKETLIST.current_user.bucket_lists[b_id]
    return render_template("bucketList.html", data=BUCKETLIST.current_user,user_b_list=user_b_list, b_id=b_id)

@APP.route('/home/bucketlist/<int:b_id>/add', methods =  ["POST", "GET"])
def addbucketlistItem(b_id):
    global BUCKETLIST
    if request.method == "POST":
        list_item = request.form
        item = list_item['blist_item']
        user_b_list = BUCKETLIST.current_user.bucket_lists[b_id]
        user_b_list.add_item(item)
        return redirect(url_for('viewbucketlist',b_id = b_id))
    return render_template("createBucketListItem.html", b_id=b_id)




    
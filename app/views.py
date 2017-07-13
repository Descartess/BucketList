""" Views.py """
from flask import render_template, redirect, url_for, request, Blueprint
from bucket_list import Application

app_blueprint = Blueprint('app_blueprint', __name__)



BUCKETLIST = Application()

@app_blueprint.route('/', methods=['POST', 'GET'])
def index():
    """ initial application path """
    if request.method == "POST":
        login_data = request.form
        if BUCKETLIST.signin(login_data['username'], login_data['password']):
            return redirect(url_for('app_blueprint.home',
                                    username=BUCKETLIST.current_user.username))
        return render_template("login.html", error="Invalid Credentials")
    return render_template("login.html")

@app_blueprint.route('/signup', methods=["POST", "GET"])
def signup():
    """ view function to logic in user """
    if request.method == "POST":
        signup_data = request.form
        if signup_data['password'] == signup_data['rpassword']:
            if BUCKETLIST.signup(signup_data['username'], signup_data['password']):
                return redirect(url_for('app_blueprint.home',
                                        username=BUCKETLIST.current_user.username))
            else:
                return render_template("signup.html", error = "User already exists ")
        return render_template("signup.html", error = "Passwords do not match")
    return render_template("signup.html")

@app_blueprint.route('/signout')
def signout():
    """ view function to sign out users"""
    BUCKETLIST.signout()
    return render_template("login.html")

@app_blueprint.route('/home/')
def home():
    """ view function for home page """
    return render_template("home.html", data=BUCKETLIST.current_user)

@app_blueprint.route('/home/create', methods=["POST", "GET"])
def createbucketlist():
    """ create bucket list logic """
    if request.method == "POST":
        bucketlist = request.form
        BUCKETLIST.current_user.add_bucketlist(bucketlist['b_listname'],
                                               int(bucketlist['completed_by']))
        return redirect(url_for('app_blueprint.home', username=BUCKETLIST.current_user.username))
    return render_template("createBucketList.html", data=BUCKETLIST.current_user)

@app_blueprint.route('/home/bucketlist/<int:b_id>')
def viewbucketlist(b_id):
    """ view bucket lists """
    user_b_list = BUCKETLIST.current_user.bucket_lists[b_id]
    return render_template("bucketList.html", data=BUCKETLIST.current_user,
                           user_b_list=user_b_list, b_id=b_id)

@app_blueprint.route('/home/bucketlist/<int:b_id>/add', methods=["POST", "GET"])
def addbucketlistitem(b_id):
    """ add new bucket list item """
    if request.method == "POST":
        list_item = request.form
        item = list_item['blist_item']
        user_b_list = BUCKETLIST.current_user.bucket_lists[b_id]
        user_b_list.add_item(item)
        return redirect(url_for('app_blueprint.viewbucketlist', b_id=b_id))
    return render_template("createBucketListItem.html", b_id=b_id, data=BUCKETLIST.current_user)

@app_blueprint.route('/home/bucketlist/<int:b_id>/del')
def deletebucketlist(b_id):
    """ delete bucket list """
    BUCKETLIST.current_user.delete_bucketlist(b_id)
    return render_template("home.html", data=BUCKETLIST.current_user)

@app_blueprint.route('/home/bucketlist/<int:b_id>/edit', methods=["POST", "GET"])
def editbucketlist(b_id):
    """ edit bucket list """
    if request.method == "POST":
        edit_data = request.form
        BUCKETLIST.current_user.edit_bucketlist(b_id, edit_data["b_listname"],
                                                int(edit_data["completed_by"]))
        return render_template("home.html", data=BUCKETLIST.current_user)
    return render_template("editBucketList.html", data=BUCKETLIST.current_user, b_id=b_id)

@app_blueprint.route('/home/bucketlist/<int:b_id>/item/<int:item_id>')
def deletebucketlistitem(b_id, item_id):
    """ delete bucket list item """
    BUCKETLIST.current_user.bucket_lists[b_id].delete_bucketlistitem(item_id)
    return redirect(url_for('app_blueprint.viewbucketlist', b_id=b_id))

@app_blueprint.route('/home/bucketlist/<int:b_id>/item/<int:item_id>/edit', methods=["POST", "GET"])
def editbucketlistitem(b_id, item_id):
    """
    Edit bucket list items
    """
    if request.method == "POST":
        list_item = BUCKETLIST.current_user.bucket_lists[b_id]
        edit_data = request.form
        list_item.edit_bucketlistitem(item_id, edit_data['blist_item'])
        return redirect(url_for('app_blueprint.viewbucketlist', b_id=b_id))
    return render_template("editBucketListItem.html", b_id=b_id, item_id=item_id,
                           data=BUCKETLIST.current_user)

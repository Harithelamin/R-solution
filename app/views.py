from datetime import datetime
from flask import render_template, request, redirect, url_for, flash, session
from app import app, db
from app.forms import UserForm
from app.models import Faq, User, Topic, Comment

@app.route('/')
def home():
    flash('')
    return render_template('index.html')
#*********************************************
@app.route('/about/')
def about():
    flash('')
    return render_template('about.html')
#*********************************************
@app.route('/newFaq/', methods=['POST', 'GET'])
def newFaq():
    if not session.get('admin'):
        return render_template('login.html')
    if not session.get('logged_in'):
        return render_template('login.html')

    from app.forms import FaqForm
    FaqForm = FaqForm()

    if request.method == 'POST':
        if FaqForm.validate_on_submit():
            question = FaqForm.question.data
            answer = FaqForm.answer.data
            faq = Faq(question, answer)
            db.session.add(faq)
            db.session.commit()

            flash('Faq added')
            return redirect(url_for('FaqsList'))

    flash_errors(FaqForm)
    return render_template('newFaq.html', form=FaqForm)
#********************************************************
@app.route('/FaqsList/')
def FaqsList():
    faqs = db.session.query(Faq).all()
    return render_template('FaqsList.html', faqs=faqs)
#********************************************************
@app.route('/NewTopic/', methods=['POST', 'GET'])
def NewTopic():
    if not session.get('admin'):
        return render_template('login.html')
    if not session.get('logged_in'):
        return render_template('login.html')

    from app.forms import TopicForm
    TopicForm = TopicForm()

    if request.method == 'POST':
        if TopicForm.validate_on_submit():
            topicDate = datetime.now()
            title = TopicForm.title.data
            content = TopicForm.content.data

            topic = Topic(topicDate, title, content)
            db.session.add(topic)
            db.session.commit()

            flash('The New Topic Registered')
            return redirect(url_for('TopicsList'))


    flash_errors(TopicForm)

    return render_template('NewTopic.html', form=TopicForm)
#***************
@app.route('/api/NewComment', methods=['POST'])
def NewComment():
    if not session.get('logged_in'):
        return render_template('login.html')

    topicId = request.form['topicId']
    userId = session["username"]
    comment = request.form['comment']

    comment = Comment(datetime.now(), comment, topicId, userId)
    db.session.add(comment)
    db.session.commit()

    name = session["username"]

    topics = db.session.query(Topic).all()
    comments = {}


    flash('The New Comment Registered')
    return render_template('TopicsList.html', topics=topics, comments=comments, name=name)
#********************************************************
@app.route('/api/CommentsByTopicId/<int:topicId>', methods=['GET'])
def CommentsByTopicId(topicId):
    if not session.get('logged_in'):
        return render_template('login.html')
    name = session["username"]
    topics = db.session.query(Topic).filter(Topic.id == topicId)
    comments = db.session.query(Comment).filter(Comment.topicId == topicId)
    return render_template('TopicsList.html', topics=topics, comments=comments)
#********************************************************
@app.route('/TopicsList/')
def TopicsList():
    if not session.get('logged_in'):
        return render_template('login.html')

    name =session["username"]
    topics = db.session.query(Topic).all()
    comments = {}
    return render_template('TopicsList.html', topics=topics, comments=comments, name=name)
#********************************************************
def flash_errors(form):
    for field, errors in form.errors.items():
        for error in errors:
            flash(u"Error in the %s field - %s" % (
                getattr(form, field).label.text,
                error
            ))
#********************************************************
@app.route('/NewUser', methods=['POST', 'GET'])
def NewUser():
    if not session.get('admin'):
        return render_template('login.html')
    if not session.get('logged_in'):
        return render_template('login.html')

    userForm = UserForm()

    if request.method == 'POST':
        if userForm.validate_on_submit():
            username = userForm.username.data
            email = userForm.email.data
            password = userForm.password.data
            role = userForm.role.data
            user = User(username, email, password, role)
            db.session.add(user)
            db.session.commit()

            flash('The New User Has Registered!')
            return redirect(url_for('UsersList'))

    flash_errors(userForm)
    return render_template('NewUser.html', form=userForm)
#**********************************************************
@app.route('/NewLimitedUser', methods=['POST', 'GET'])
def NewLimitedUser():
    userForm = UserForm()

    if request.method == 'POST':
        if userForm.validate_on_submit():
            username = userForm.username.data
            email = userForm.email.data
            password = userForm.password.data
            role = 'User'
            user = User(username, email, password, role)
            db.session.add(user)
            db.session.commit()

            flash('The New User Has Registered!')
            return redirect(url_for('UsersList'))

    flash_errors(userForm)
    return render_template('NewLimitedUser.html', form=userForm)
#**********************************************************
@app.route('/UsersList')
def UsersList():
    if not session.get('admin'):
        return render_template('login.html')
    if not session.get('logged_in'):
        return render_template('login.html')
    users = db.session.query(User).all()
    return render_template('UsersList.html', users=users)
#**********************************************************
@app.route('/login', methods=['POST', 'GET'])
def do_admin_login():
    session['msg'] = ''
    POST_USERNAME = str(request.form['username'])
    POST_PASSWORD = str(request.form['password'])

    query1 = db.session.query(User).filter(User.username.in_([POST_USERNAME]),
                                          User.password.in_([POST_PASSWORD]),
                                          User.role == "Admin"
                                          )

    query2 = db.session.query(User).filter(User.username.in_([POST_USERNAME]),
                                           User.password.in_([POST_PASSWORD]),
                                           User.role == "User"
                                           )
    result1 = query1.first()
    result2 = query2.first()
    if result1:
        session['logged_in'] = True
        session['username'] = POST_USERNAME
        session['admin'] = True
        flash('Admin User!')

    elif result2:
        session['logged_in'] = True
        session['username'] = POST_USERNAME
        session['admin'] = False
        session['msg'] = 'Hello,', POST_USERNAME
        flash('Limited User!')
    else:
        flash('wrong password!')
        return render_template('login.html', msg=session.get('msg'))

    return TopicsList()

#*********************************************************
@app.route("/logout")
def logout():
    session['logged_in'] = False
    session['username'] = ''
    return home()
#*********************************************************

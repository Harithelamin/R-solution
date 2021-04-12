from app import db
class Faq(db.Model):
    __tablename__ ='faqs'
    id = db.Column(db.Integer, primary_key = True)
    question = db.Column(db.String)
    answer = db.Column(db.String)
    def __init__(self, question, answer):
         self.question = question
         self.answer = answer

    def __repr__(self):
        return '<Faq $r>' % self.question, self.answer

#*******************************************************

class Topic(db.Model):
    __tablename__ ='topics'
    id = db.Column(db.Integer, primary_key = True)
    topicDate = db.Column(db.Date)
    title = db.Column(db.String(10000))
    content = db.Column(db.String(10000))
    def __init__(self, topicDate, title, content):
        self.topicDate = topicDate
        self.title = title
        self.content = content

    def __repr__(self):
        return '<News $r' % self.topicDate, self.title, self.content

#*******************************************************

class Comment(db.Model):
    __tablename__ ='comments'
    id = db.Column(db.Integer, primary_key = True)
    commentDate = db.Column(db.Date)
    comment = db.Column(db.String(10000))

    topicId = db.Column(db.Integer)
    userId = db.Column(db.String(10000))
    def __init__(self, commentDate, comment, topicId, userId):
        self.commentDate = commentDate
        self.comment = comment
        self.topicId = topicId
        self.userId = userId

    def __repr__(self):
        return '<News $r' % self.commentDate, self.comment, self.topicId, self.userId

#*******************************************************

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255))
    email = db.Column(db.String(255), unique=True)
    password = db.Column(db.String(255))
    role = db.Column(db.String(255))

    def __init__(self, username, email, password, role):
        self.username = username
        self.email = email
        self.password = password
        self.role = role

    def __repr__(self):
        return '<User %r>' % self.username, self.email, self.role

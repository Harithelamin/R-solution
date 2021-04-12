DROP TABLE IF EXISTS faqs;
CREATE TABLE faqs
(
  id integer primary key autoincrement,
  question string not null,
  answer string not null
);
DROP TABLE IF EXISTS topics;
CREATE TABLE topics
(
  id integer primary key autoincrement,
  date date not null ,
  title string not null,
  content string not null
);

DROP TABLE IF EXISTS comments;
CREATE TABLE comments
(
  id integer primary key autoincrement,
  commentDate date not null ,
  comment string not null,
  topicId integer not null,
  userId string not null,
  FOREIGN KEY (topicId) REFERENCES topics (id)
  ON UPDATE CASCADE
  ON DELETE CASCADE
);

DROP TABLE IF EXISTS users;
CREATE TABLE users (
  id integer primary key autoincrement,
  username string not null,
  email string not null,
  password string not null,
  role string not null
 );


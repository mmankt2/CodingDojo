CREATE TABLE [IF NOT EXISTS] users(
  id            INT NOT NULL AUTO_INCREMENT,
  password      VARCHAR(255)
  email         VARCHAR(255)
  first_name    VARCHAR(100)
  last_name     VARCHAR(100)
  phone_number  VARCHAR(20)
  created_at    DATETIME,
  updated_at    DATETIME
  PRIMARY KEY (id)
)

CREATE TABLE [IF NOT EXISTS] blogs(
  id            INT NOT NULL AUTO_INCREMENT,
  blog_name     VARCHAR(100),
  created_at    DATETIME,
  updated_at    DATETIME,
  admin_id      INT (foreign key),
  coadmin_id    INT (foreign key),
  PRIMARY KEY (id),
  FOREIGN KEY (admin_id) REFERENCES users(id),
  FOREIGN KEY (coadmin_id) REFERENCES users(id)
)

CREATE TABLE [IF NOT EXISTS] posts(
  id            INT NOT NULL AUTO_INCREMENT,
  created_at    DATETIME,
  updated_at    DATETIME,
  author        INT (foreign key),
  content       TEXT,
  blog_id       INT (foreign key),
  PRIMARY KEY (id),
  FOREIGN KEY (author) REFERENCES users(id),
  FOREIGN KEY (blog_id) REFERENCES blogs(id)
)

CREATE TABLE [IF NOT EXISTS] comments(
  id            INT NOT NULL AUTO_INCREMENT,
  created_at    DATETIME,
  updated_at    DATETIME,
  author        INT (foreign key),
  content       TEXT,
  post_id       INT (foreign key),
  PRIMARY KEY (id),
  FOREIGN KEY (author) REFERENCES users(id)
  FOREIGN KEY (post_id) REFERENCES posts(id)
)

CREATE TABLE [IF NOT EXISTS] histories(
  id            INT NOT NULL AUTO_INCREMENT,
  created_at    DATETIME,
  updated_at    DATETIME,
  user_id       INT (foreign key),
  blog_id       INT (foreign key),
  visit_time    DATETIME,
  visit_length  INT,
  IP_Address    VARCHAR(100),
  PRIMARY KEY (id),
  FOREIGN KEY (user_id) REFERENCES users(id),
  FOREIGN KEY (blog_id) REFERENCES blogs(id)
)

CREATE TABLE [IF NOT EXISTS] attachments(
  id            INT NOT NULL AUTO_INCREMENT,
  created_at    DATETIME,
  updated_at    DATETIME,
  post_id       INT (foreign key),
  attachment_name VARCHAR(100),
  filepath      VARCHAR(255),
  PRIMARY KEY (id),
  FOREIGN KEY (user_id) REFERENCES users(id),
  FOREIGN KEY (post_id) REFERENCES posts(id),
)
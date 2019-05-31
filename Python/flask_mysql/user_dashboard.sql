CREATE TABLE [IF NOT EXISTS] users(
  id            INT NOT NULL AUTO_INCREMENT,
  password      VARCHAR(255),
  email         VARCHAR(255),
  first_name    VARCHAR(100),
  last_name     VARCHAR(100),
  description   VARCHAR(255),
  admin_flag    BOOLEAN,
  created_at    DATETIME,
  updated_at    DATETIME,
  PRIMARY KEY (id)
)

CREATE TABLE [IF NOT EXISTS] messages(
  id            INT NOT NULL AUTO_INCREMENT,
  created_at    DATETIME,
  updated_at    DATETIME,
  author        INT (foreign key),
  content       TEXT,
  profile_id    INT (foreign key),
  PRIMARY KEY (id),
  FOREIGN KEY (author) REFERENCES users(id),
  FOREIGN KEY (profile_id) REFERENCES profiles(id)
)

CREATE TABLE [IF NOT EXISTS] comments(
  id            INT NOT NULL AUTO_INCREMENT,
  created_at    DATETIME,
  updated_at    DATETIME,
  author        INT (foreign key),
  content       TEXT,
  message_id    INT (foreign key),
  PRIMARY KEY (id),
  FOREIGN KEY (author) REFERENCES users(id)
  FOREIGN KEY (message_id) REFERENCES messages(id)
)

CREATE TABLE [IF NOT EXISTS] profiles(
  id            INT NOT NULL AUTO_INCREMENT,
  user_id       INT,
  created_at    DATETIME,
  updated_at    DATETIME,
  PRIMARY KEY (id),
  FOREIGN KEY (user_id) REFERENCES users(id)
)
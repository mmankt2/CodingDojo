CREATE TABLE [IF NOT EXISTS] dojos(
  id            INT NOT NULL AUTO_INCREMENT,
  created_at    DATETIME,
  updated_at    DATETIME
  PRIMARY KEY (id)
)

CREATE TABLE [IF NOT EXISTS] ninjas(
  id            INT NOT NULL AUTO_INCREMENT,
  skill         VARCHAR(100)
  created_at    DATETIME,
  updated_at    DATETIME,
  dojo_id       INT (foreign key)
  PRIMARY KEY (id)
  FOREIGN KEY (dojo_id) REFERENCES dojos(id)
)
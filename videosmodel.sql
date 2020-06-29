CREATE TABLE videos (
  id INT(6) UNSIGNED AUTO_INCREMENT PRIMARY KEY,
  title VARCHAR(500) NOT NULL,
  date VARCHAR(500) NOT NULL,
  slug VARCHAR(500) NOT NULL,
  video_link VARCHAR(3000) NOT NULL,
  reg_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);
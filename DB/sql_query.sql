CREATE TABLE tblUserQuery(txtname varchar(50),txtMobile varchar(10),txtQuery varchar(100));

ALTER TABLE tblUserQuery ADD query_date DATE DEFAULT NOW();
-- ALTER TABLE tblUserQuery ADD query_date DATE DEFAULT CURRENT_TIMESTAMP;
ALTER TABLE tblUserQuery ADD id INT(10) AUTO_INCREMENT PRIMARY KEY;

-- ALTER TABLE tblUserQuery ADD id INTEGER AUTO_INCREMENT PRIMARY KEY;
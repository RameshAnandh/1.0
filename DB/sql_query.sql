CREATE TABLE tblUserQuery(txtname varchar(50),txtMobile varchar(10),txtQuery varchar(100));

ALTER TABLE tblUserQuery ADD query_date DATETIME DEFAULT NOW();
-- ALTER TABLE tblUserQuery ADD query_date DATE DEFAULT CURRENT_TIMESTAMP;
ALTER TABLE tblUserQuery ADD id INT(10) AUTO_INCREMENT PRIMARY KEY;

-- ALTER TABLE tblUserQuery ADD id INTEGER AUTO_INCREMENT PRIMARY KEY;

CREATE TABLE tblUserQuery(txtname varchar(50),txtMobile varchar(10),txtQuery varchar(100),
query_date DATETIME DEFAULT NOW(),id INT(10) AUTO_INCREMENT,
PRIMARY KEY (id)
);

CREATE TABLE tblClientDetails(txtClientname varchar(50),txtMobile1 varchar(10),txtMobile2 varchar(10)
,txtAddress varchar(100),txtEmailID varchar(25),active BOOLEAN);

INSERT INTO tblClientDetails(txtClientname,txtMobile1,txtMobile2,txtAddress,txtEmailID,active)
VALUES('MANO DRIVING SCHOOL','9842124001','9486624001','3,Apollo Colony Extension, Pothigai Nagar,Perumalpuram,Tirunelveli, Tamil Nadu 627007','saran4001@gmail.com',1);


INSERT INTO tblClientDetails(txtClientname,txtMobile1,txtMobile2,txtAddress,txtEmailID,active)
VALUES('TEST DRIVING SCHOOL','98421XXXXX','94866XXXXX','Test Address,Palayamkottai,Tirunelveli, Tamil Nadu 627007','testmail@gmail.com',0);

SELECT * FROM tblClientDetails;

UPDATE tblClientDetails SET active=0 WHERE txtClientname='MANO DRIVING SCHOOL';
UPDATE tblClientDetails SET active=1 WHERE txtClientname='TEST DRIVING SCHOOL';
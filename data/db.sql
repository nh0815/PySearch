CREATE SCHEMA IF NOT EXISTS `test_db`;
CREATE TABLE IF NOT EXISTS `test_db`.`Document` (
  `docid` INT NOT NULL,
  `length` INT NULL,
  `text` TEXT NULL,
  PRIMARY KEY (`docid`));
CREATE TABLE IF NOT EXISTS `test_db`.`Word`(
  `word` varchar(30) NOT NULL,
  `frequency` int(11) DEFAULT NULL,
  PRIMARY KEY (`word`)
);
CREATE TABLE IF NOT EXISTS `Entry` (
  `word` varchar(30) NOT NULL,
  `docid` INT NOT NULL,
  `freq` INT DEFAULT NULL,
  PRIMARY KEY (`word`,`docid`),
  FOREIGN KEY (`word`) REFERENCES `Word` (`word`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  FOREIGN KEY (`docid`) REFERENCES `Document` (`docid`) ON DELETE NO ACTION ON UPDATE NO ACTION
);
SET foreign_key_checks=0;
TRUNCATE TABLE Document;
LOAD DATA INFILE 'docs.txt'
INTO TABLE Document;
TRUNCATE TABLE Word;
LOAD DATA INFILE 'freq.txt'
INTO TABLE Word
FIELDS TERMINATED BY ' ';
TRUNCATE TABLE Entry;
LOAD DATA INFILE 'entries.txt'
INTO TABLE Entry;
SET foreign_key_checks=1;
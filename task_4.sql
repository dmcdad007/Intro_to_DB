Table: Books
Create Table: CREATE TABLE `Books` (
  `book_id` int NOT NULL AUTO_INCREMENT,
  `title` varchar(130) NOT NULL,
  `author_id` int NOT NULL,
  `price` double NOT NULL,
  `publication_date` date DEFAULT NULL,
  PRIMARY KEY (`book_id`),
  KEY `author_id` (`author_id`),
  CONSTRAINT `Books_ibfk_1` FOREIGN KEY (`author_id`) REFERENCES `Authors` (`author_id`) ON UPDATE CASCADE ON DELETE RESTRICT
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4





-- Switch to the alx_book_store database
USE alx_book_store;

-- Display the full description of the table 'books' without using DESCRIBE or EXPLAIN
SHOW CREATE TABLE Books;

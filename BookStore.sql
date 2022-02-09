-- MySQL dump 10.13  Distrib 8.0.27, for macos11 (arm64)
--
-- Host: localhost    Database: BookStore
-- ------------------------------------------------------
-- Server version	8.0.27

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `Books`
--

DROP TABLE IF EXISTS `Books`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Books` (
  `ISBN` varchar(13) NOT NULL,
  `Title` varchar(45) NOT NULL,
  `Author` varchar(128) NOT NULL,
  `Price` decimal(5,2) NOT NULL,
  `Cover` varchar(10) NOT NULL,
  `Publisher` varchar(256) NOT NULL,
  `Pages` int NOT NULL,
  `Language` varchar(45) NOT NULL,
  `Series` varchar(128) DEFAULT NULL,
  `PubDate` date NOT NULL,
  PRIMARY KEY (`ISBN`),
  UNIQUE KEY `ISBN_UNIQUE` (`ISBN`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Books`
--

LOCK TABLES `Books` WRITE;
/*!40000 ALTER TABLE `Books` DISABLE KEYS */;
INSERT INTO `Books` VALUES ('9780752863887','The Bourne Supremacy','Robert Ludlum',29.99,'Hardcover','Orion Publishing Group',688,'English','Jason Bourne #2','2004-02-11'),('9780752864327','The Bourne Identity','Robert Ludlum',29.99,'Hardcover','Orion Publishing Group',566,'English','Jason Bourne #1','2003-03-24'),('9892822901976','The Scent of Oranges','Lynne Danticat',9.99,'Paperback','Sound & Seas Co.',255,'English','Esme\'s Ladies #4','2185-02-08'),('9892822914044','The Seawitch Sings','Lynne Danticat',9.99,'Paperback','Sound & Seas Co.',381,'English','Esme\'s Ladies #1','2181-12-11'),('9892822931577','Saint Esme','Lynne Danticat',9.99,'Paperback','Sound & Seas Co.',336,'English','Esme\'s Ladies #6','2188-04-15'),('9892822958918','Lace and Brandy','Lynne Danticat',9.99,'Paperback','Sound & Seas Co.',380,'English','Esme\'s Ladies #5','2186-07-25'),('9892822966326','Whither Thou Goest','Lynne Danticat',9.99,'Paperback','Sound & Seas Co.',423,'English','Esme\'s Ladies #3','2183-02-14'),('9892822975922','Muddy Waters','Lynne Danticat',9.99,'Paperback','Sound & Seas Co.',362,'English','Esme\'s Ladies #2','2182-03-05'),('9892822997696','Burnished Silver','Lynne Danticat',9.99,'Paperback','Sound & Seas Co.',368,'English','Esme\'s Ladies #7','2191-09-20'),('9892837050072','Heliotrope Pajamas','Malin Wolff',5.99,'Paperback','Cedar House Publishers',16,'English','','2188-06-03'),('9892837050546','Heliotrope Pajamas','Malin Wolff',7.99,'Paperback','Cedar House Publishers',28,'English','','2181-03-06'),('9892837051369','Banana Slug and the Mossy Rock','Malin Wolff',7.99,'Paperback','Cedar House Publishers',15,'English','Banana Slug #3','2188-01-08'),('9892837051529','Banana Slug and the Glass Half Full','Gloria Green',7.99,'Paperback','Cedar House Publishers',20,'English','Banana Slug #1','2187-04-03'),('9892837052052','(im)Mortality','Clifford Wolitzer',11.99,'Paperback','Cedar House Publishers',324,'English','','2192-09-18'),('9892837052229','Adventures of Kaya','Ward Haigh',11.99,'Paperback','Cedar House Publishers',256,'English','','2182-07-23'),('9892837053691','Banana Slug and Xyr Friends','Hillary Barnhardt',7.99,'Paperback','Cedar House Publishers',20,'English','Banana Slug #4','2188-10-14'),('9892837054926','Can I Be Honest?','Charles Fenimore',11.99,'Paperback','Cedar House Publishers',404,'English','','2188-04-24'),('9892837056074','It\'s Never Just a Glass','Leonard Nabokov',11.99,'Paperback','Cedar House Publishers',218,'English','','2186-07-25'),('9892837056333','It\'s Never Just a Glass','Leonard Nabokov',19.99,'Hardcover','Cedar House Publishers',222,'English','','2185-08-09'),('9892837057637','(im)Mortality','Clifford Wolitzer',22.99,'Hardcover','Cedar House Publishers',324,'English','','2191-11-15'),('9892837057750','Banana Slug and the Lost Cow','Hillary Barnhardt',7.99,'Paperback','Cedar House Publishers',22,'English','Banana Slug #2','2187-11-06'),('9892837059662','Heliotrope Pajamas','Malin Wolff',10.99,'Paperback','Cedar House Publishers',31,'English','','2186-05-02'),('9892837059877','Alanna Saves the Day','Bernard Hopf',8.99,'Paperback','Cedar House Publishers',188,'English','','2185-09-22'),('9892865400474','Natural Pamplemousse','Phoebe Brown',15.99,'Paperback','Palimpsest Printing',371,'English','','2180-04-18'),('9892865401273','We\'re Sisters and We Kinda Like Each Other','Patricia Hazzard',16.99,'Paperback','Palimpsest Printing',295,'English','','2183-12-09'),('9892865420175','Inconvenient Confessions: a memoir','Oliver Lowry',29.99,'Hardcover','Palimpsest Printing',337,'English','','2189-06-09'),('9892865426207','Nothing But Capers','Abraham Stackhouse',32.99,'Hardcover','Palimpsest Printing',390,'English','','2180-09-12'),('9892865438996','Who Did You Think You Were Kidding?','Philip Antrim',29.99,'Hardcover','Palimpsest Printing',207,'English','','2192-08-14'),('9892865439887','Land Water Sky Space','Elizabeth Herbach',47.99,'Hardcover','Palimpsest Printing',368,'English','','2191-03-15'),('9892865443709','Don\'t Check your Ego','R.M. Larner',15.99,'Paperback','Palimpsest Printing',480,'English','','2185-03-29'),('9892865450189','Inconvenient Confessions: a memoir','Oliver Lowry',16.99,'Paperback','Palimpsest Printing',385,'English','','2190-07-15'),('9892865457713','Hashtag QuokkaSelfie','Langston Lippman',15.99,'Paperback','Palimpsest Printing',631,'English','','2179-01-12'),('9892865457942','Hashtag QuokkaSelfie','Langston Lippman',26.99,'Hardcover','Palimpsest Printing',640,'English','','2178-09-29'),('9892865460331','The Elephant House','John W. Spanogle',15.99,'Paperback','Palimpsest Printing',598,'English','','2185-01-04'),('9892865465077','Say it with Snap!','John W. Spanogle',15.99,'Paperback','Palimpsest Printing',387,'English','','2192-05-15'),('9892865469303','Natural Pamplemousse','Phoebe Brown',30.99,'Hardcover','Palimpsest Printing',394,'English','','2178-08-18'),('9892865479654','We\'re Sisters and We Kinda Like Each Other','Patricia Hazzard',29.99,'Hardcover','Palimpsest Printing',288,'English','','2182-12-17'),('9892865485730','The Elephant House','John W. Spanogle',23.99,'Hardcover','Palimpsest Printing',598,'English','','2184-01-13'),('9892865494848','Say it with Snap!','John W. Spanogle',23.99,'Hardcover','Palimpsest Printing',400,'English','','2191-03-01'),('9892865498266','Don\'t Check your Ego','R.M. Larner',28.99,'Hardcover','Palimpsest Printing',480,'English','','2183-12-16'),('9892879019914','Post Alley','Burton Malamud',12.99,'Paperback','Palimpsest Printing',356,'English','','2179-09-07'),('9892879036836','The Spark and The Ashes','Ursula Karenine',18.99,'Hardcover','Etaoin Shrdlu Press',340,'English','','2192-07-03'),('9892879045104','Turn Left Til You Get There','Kris Elegant',8.99,'Paperback','Etaoin Shrdlu Press',264,'English','The Aspall Trilogy #1','2179-02-16'),('9892879056384','Thatchwork Cottage','Burton Malamud',27.99,'Hardcover','Etaoin Shrdlu Press',485,'English','','2185-11-15'),('9892879056704','Zero over Twelve','Burton Malamud',8.99,'Paperback','Etaoin Shrdlu Press',338,'English','','2187-11-20'),('9892879076108','Kalakalal Avenue','Elmer Komroff',27.99,'Hardcover','Etaoin Shrdlu Press',432,'English','','2187-05-15'),('9892879138714','The Winchcombe Railway Museum Heist','Carolyn Segal',8.99,'Paperback','Etaoin Shrdlu Press',357,'English','Inspector Ryeslton #2','2185-09-27'),('9892879143794','Quiddity and Quoddity','Jill Hergesheimer',11.99,'Paperback','Etaoin Shrdlu Press',373,'English','','2184-02-29'),('9892879165338','She Also Tottered','Robert Plimpton',21.99,'Hardcover','Etaoin Shrdlu Press',531,'English','','2190-02-16'),('9892879168087','Soft, Pliable Truth','Robert Plimpton',12.99,'Paperback','Etaoin Shrdlu Press',458,'English','','2190-05-18'),('9892879168261','A Horrible Human with the Habits of a Monster','Kenneth Douglas',23.99,'Paperback','Etaoin Shrdlu Press',85,'English','','2189-03-24'),('9892879181277','And I Said Yes','Elmer Komroff',27.99,'Hardcover','Etaoin Shrdlu Press',704,'English','','2179-04-24'),('9892879219918','Kalakalal Avenue','Elmer Komroff',8.99,'Paperback','Etaoin Shrdlu Press',341,'English','','2188-11-25'),('9892879225629','Zero over Twelve','Burton Malamud',20.99,'Hardcover','Etaoin Shrdlu Press',356,'English','','2186-12-12'),('9892879228712','The Thing Is','Gloria Green',8.99,'Paperback','Etaoin Shrdlu Press',452,'English','Meddler Trilogy #1','2179-07-13'),('9892879230159','Can I Be Honest?','Charles Fenimore',18.99,'Hardcover','Etaoin Shrdlu Press',404,'English','','2187-03-06'),('9892879230234','Portmeirion','Bianca Thompson',8.99,'Paperback','Etaoin Shrdlu Press',792,'English','The Mallemaroking Saga #2','2188-10-21'),('9892879268244','The Triscanipt','Ursula Karenine',8.99,'Paperback','Etaoin Shrdlu Press',280,'English','','2188-04-08'),('9892879270780','No More Lightning','Charles Fenimore',23.99,'Paperback','Etaoin Shrdlu Press',192,'English','','2190-10-05'),('9892879305369','Not to Gossip, But','Gloria Green',8.99,'Paperback','Etaoin Shrdlu Press',311,'English','Meddler Trilogy #2','2181-07-26'),('9892879321055','Did You Hear?','Lynne Danticat',8.99,'Paperback','Etaoin Shrdlu Press',390,'English','Meddler Trilogy #3','2183-02-25'),('9892879364854','She Also Tottered','Robert Plimpton',12.99,'Paperback','Etaoin Shrdlu Press',520,'English','','2190-09-14'),('9892879408978','Portmeirion','Bianca Thompson',21.99,'Hardcover','Etaoin Shrdlu Press',656,'English','The Mallemaroking Saga #2','2187-02-20'),('9892879427283','Interrobangs for All','Elmer Komroff',27.99,'Hardcover','Etaoin Shrdlu Press',493,'English','','2182-11-05'),('9892879438418','Quiddity and Quoddity','Jill Hergesheimer',18.99,'Hardcover','Etaoin Shrdlu Press',373,'English','','2183-04-01'),('9892879447304','Dust on the Rim','Kathy Yglesias',8.99,'Paperback','Etaoin Shrdlu Press',575,'English','','2179-01-05'),('9892879456757','Some Eggs or Something?','Lori Kaan',12.99,'Paperback','Etaoin Shrdlu Press',105,'English','','2181-07-03'),('9892879513979','The Triscanipt','Ursula Karenine',21.99,'Hardcover','Etaoin Shrdlu Press',292,'English','','2187-08-28'),('9892879528836','Post Alley','Burton Malamud',27.99,'Hardcover','Palimpsest Printing',384,'English','','2178-09-08'),('9892879557522','Tales of the Compass','Kathy Yglesias',8.99,'Paperback','Etaoin Shrdlu Press',398,'English','','2192-04-03'),('9892879558246','Concerning Prophecy','Grace Harrison',8.99,'Paperback','Etaoin Shrdlu Press',651,'English','','2190-12-21'),('9892879568566','Cimornul','Jill Hergesheimer',21.99,'Hardcover','Etaoin Shrdlu Press',434,'English','','2188-02-19'),('9892879611255','Interrobangs for All','Elmer Komroff',12.99,'Paperback','Etaoin Shrdlu Press',470,'English','','2183-05-27'),('9892879646936','And I Said Yes','Elmer Komroff',12.99,'Paperback','Etaoin Shrdlu Press',645,'English','','2191-08-25'),('9892879678913','Some Eggs or Something?','Lori Kaan',27.99,'Hardcover','Etaoin Shrdlu Press',105,'English','','2180-07-25'),('9892879680893','Ballinby Boys','Arthur McCrumb',21.99,'Hardcover','Etaoin Shrdlu Press',401,'English','','2179-05-18'),('9892879685317','Soft, Pliable Truth','Robert Plimpton',21.99,'Hardcover','Etaoin Shrdlu Press',437,'English','','2189-01-06'),('9892879693596','Concerning Prophecy','Grace Harrison',21.99,'Hardcover','Etaoin Shrdlu Press',706,'English','','2190-03-02'),('9892879698072','9803 North Millworks Road','Carolyn Segal',8.99,'Paperback','Etaoin Shrdlu Press',414,'English','Inspector Ryeslton #1','2182-09-24'),('9892879705978','Turn Left Til You Get There','Kris Elegant',27.99,'Hardcover','Etaoin Shrdlu Press',277,'English','The Aspall Trilogy #1','2178-06-02'),('9892879715656','The Mallemaroking','Bianca Thompson',21.99,'Hardcover','Etaoin Shrdlu Press',819,'English','The Mallemaroking Saga #1','2183-02-25'),('9892879743741','Rystwyth','Bianca Thompson',21.99,'Hardcover','Etaoin Shrdlu Press',1218,'English','The Mallemaroking Saga #3','2192-01-03'),('9892879821258','The Winchcombe Railway Museum Heist','Carolyn Segal',22.99,'Hardcover','Etaoin Shrdlu Press',293,'English','Inspector Ryeslton #2','2184-02-10'),('9892879821975','Thatchwork Cottage','Burton Malamud',12.99,'Paperback','Etaoin Shrdlu Press',469,'English','','2186-12-05'),('9892879823399','Tales of the Compass','Kathy Yglesias',21.99,'Hardcover','Etaoin Shrdlu Press',421,'English','','2191-02-22'),('9892879827496','9803 North Millworks Road','Carolyn Segal',22.99,'Hardcover','Etaoin Shrdlu Press',384,'English','Inspector Ryeslton #1','2181-07-10'),('9892879874599','The Startling End of Mr. Hidhoo','Jonathan Kotzwinkle',23.99,'Paperback','Etaoin Shrdlu Press',88,'English','','2182-12-21'),('9892879910280','The Mallemaroking','Bianca Thompson',12.99,'Paperback','Etaoin Shrdlu Press',784,'English','The Mallemaroking Saga #1','2186-04-14'),('9892879967055','Cimornul','Jill Hergesheimer',8.99,'Paperback','Etaoin Shrdlu Press',381,'English','','2189-03-17');
/*!40000 ALTER TABLE `Books` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Carts`
--

DROP TABLE IF EXISTS `Carts`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Carts` (
  `idCart` int NOT NULL AUTO_INCREMENT,
  `cartISBN` varchar(13) NOT NULL,
  `cartOwner` varchar(45) NOT NULL,
  PRIMARY KEY (`idCart`),
  KEY `fk_cartISBN_idx` (`cartISBN`) /*!80000 INVISIBLE */,
  KEY `fk_cartOwner_idx` (`cartOwner`) /*!80000 INVISIBLE */,
  CONSTRAINT `fk_cISBN` FOREIGN KEY (`cartISBN`) REFERENCES `Books` (`ISBN`),
  CONSTRAINT `fk_cuserName` FOREIGN KEY (`cartOwner`) REFERENCES `Users` (`userName`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=15 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Carts`
--

LOCK TABLES `Carts` WRITE;
/*!40000 ALTER TABLE `Carts` DISABLE KEYS */;
/*!40000 ALTER TABLE `Carts` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Sales`
--

DROP TABLE IF EXISTS `Sales`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Sales` (
  `idSales` int NOT NULL AUTO_INCREMENT,
  `productISBN` varchar(13) NOT NULL,
  `Purchaser` varchar(45) NOT NULL,
  `PurchasedOn` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`idSales`),
  KEY `fk_sISBN_idx` (`productISBN`) /*!80000 INVISIBLE */,
  KEY `fk_suserName_idx` (`Purchaser`) /*!80000 INVISIBLE */,
  CONSTRAINT `fk_sISBN` FOREIGN KEY (`productISBN`) REFERENCES `Books` (`ISBN`),
  CONSTRAINT `fk_suserName` FOREIGN KEY (`Purchaser`) REFERENCES `Users` (`userName`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Sales`
--

LOCK TABLES `Sales` WRITE;
/*!40000 ALTER TABLE `Sales` DISABLE KEYS */;
INSERT INTO `Sales` VALUES (1,'9892822958918','huhridge','2022-01-24 09:37:31'),(2,'9892879558246','huhridge','2022-01-24 09:37:31'),(3,'9892822931577','huhridge','2022-01-24 09:37:31'),(4,'9892837056333','huhridge','2022-01-24 09:37:31'),(5,'9892837050546','huhridge','2022-01-24 09:37:31'),(6,'9892822966326','huhridge','2022-01-24 09:37:31'),(7,'9892822901976','huhridge','2022-01-24 09:37:31'),(8,'9892822931577','huhridge','2022-01-24 09:37:31'),(9,'9780752863887','huhridge','2022-01-24 09:47:32'),(10,'9780752864327','huhridge','2022-01-24 09:47:32'),(11,'9780752863887','huhridge','2022-01-24 09:47:32');
/*!40000 ALTER TABLE `Sales` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Users`
--

DROP TABLE IF EXISTS `Users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Users` (
  `userName` varchar(45) NOT NULL,
  `passWord` varchar(20) NOT NULL,
  `userType` varchar(20) NOT NULL,
  `eMail` varchar(128) NOT NULL,
  `Name` varchar(128) NOT NULL,
  PRIMARY KEY (`userName`),
  UNIQUE KEY `username_UNIQUE` (`userName`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Users`
--

LOCK TABLES `Users` WRITE;
/*!40000 ALTER TABLE `Users` DISABLE KEYS */;
INSERT INTO `Users` VALUES ('huhridge','huhridge','Customer','ridge@huh.com','HuhRidge'),('orion','orion@Hachette','Publisher','orion@hachette.co.uk','Orion Publishing Group');
/*!40000 ALTER TABLE `Users` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Wishlists`
--

DROP TABLE IF EXISTS `Wishlists`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Wishlists` (
  `idWishlists` int NOT NULL AUTO_INCREMENT,
  `wishOwner` varchar(45) NOT NULL,
  `wishBook` varchar(13) NOT NULL,
  PRIMARY KEY (`idWishlists`),
  KEY `fk_wISBN_idx` (`wishBook`) /*!80000 INVISIBLE */,
  KEY `fk_wuserName_idx` (`wishOwner`) /*!80000 INVISIBLE */,
  CONSTRAINT `fk_wISBN` FOREIGN KEY (`wishBook`) REFERENCES `Books` (`ISBN`),
  CONSTRAINT `fk_wuserName` FOREIGN KEY (`wishOwner`) REFERENCES `Users` (`userName`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Wishlists`
--

LOCK TABLES `Wishlists` WRITE;
/*!40000 ALTER TABLE `Wishlists` DISABLE KEYS */;
INSERT INTO `Wishlists` VALUES (9,'huhridge','9892837050546'),(10,'huhridge','9892865420175'),(11,'huhridge','9780752864327');
/*!40000 ALTER TABLE `Wishlists` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-02-09 21:33:21

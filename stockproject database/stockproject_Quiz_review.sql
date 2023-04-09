-- MySQL dump 10.13  Distrib 8.0.27, for macos11 (x86_64)
--
-- Host: localhost    Database: stockproject
-- ------------------------------------------------------
-- Server version	8.0.26

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `Quiz_review`
--

DROP TABLE IF EXISTS `Quiz_review`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Quiz_review` (
  `quiz_review id` int NOT NULL AUTO_INCREMENT,
  `Time` varchar(100) NOT NULL,
  `chapter_id` int NOT NULL,
  `Score` int NOT NULL,
  `AccountId` int NOT NULL,
  PRIMARY KEY (`quiz_review id`),
  KEY `chapter_id_idx` (`chapter_id`),
  KEY `accountid_idx` (`AccountId`)
) ENGINE=InnoDB AUTO_INCREMENT=45 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Quiz_review`
--

LOCK TABLES `Quiz_review` WRITE;
/*!40000 ALTER TABLE `Quiz_review` DISABLE KEYS */;
INSERT INTO `Quiz_review` VALUES (9,'2023-03-20 19:57:10.382196',1,2,1),(10,'2023-03-20 20:00:46.732096',2,1,24),(23,'2023-03-20 20:05:27.721561',2,1,24),(39,'2023-03-23 20:41:56.195605',2,3,24),(40,'2023-03-23 20:45:15.808735',2,3,24),(41,'2023-03-23 21:06',4,0,1),(42,'2023-03-23 21:07:15',4,4,1),(43,'2023-03-24 14:33:18',2,0,1),(44,'2023-03-24 15:12:08',4,0,24);
/*!40000 ALTER TABLE `Quiz_review` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-04-09 14:32:14

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
-- Table structure for table `subchapters`
--

DROP TABLE IF EXISTS `subchapters`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `subchapters` (
  `subchapters_id` int NOT NULL AUTO_INCREMENT,
  `chapters_id` int NOT NULL,
  `subchapterIndex` int NOT NULL,
  `subchapter_name` varchar(45) NOT NULL,
  PRIMARY KEY (`subchapters_id`),
  KEY `chapter_id_idx` (`chapters_id`),
  CONSTRAINT `chapters_id` FOREIGN KEY (`chapters_id`) REFERENCES `chapters` (`chapters id`)
) ENGINE=InnoDB AUTO_INCREMENT=40 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `subchapters`
--

LOCK TABLES `subchapters` WRITE;
/*!40000 ALTER TABLE `subchapters` DISABLE KEYS */;
INSERT INTO `subchapters` VALUES (1,1,1,'1.1'),(2,1,2,'1.2'),(3,1,3,'1.3'),(4,1,4,'1.4'),(5,2,1,'2.1'),(6,2,2,'2.2'),(7,2,3,'2.3'),(8,2,4,'2.4'),(9,2,5,'2.5'),(10,2,6,'2.6'),(11,2,7,'2.7'),(12,2,8,'2.8'),(13,2,9,'2.9'),(14,2,10,'2.10'),(15,3,1,'3.1'),(16,3,2,'3.2'),(17,3,3,'3.3'),(18,3,4,'3.4'),(19,3,5,'3.5'),(20,3,6,'3.6'),(21,3,7,'3.7'),(22,4,1,'4.1'),(23,4,2,'4.2'),(24,4,3,'4.3'),(25,4,4,'4.4'),(26,4,5,'4.5'),(27,4,6,'4.6'),(28,4,7,'4.7'),(29,5,1,'5.1'),(30,5,2,'5.2'),(31,5,3,'5.3'),(32,5,4,'5.4'),(33,5,5,'5.5'),(34,5,6,'5.6'),(35,5,7,'5.7'),(36,5,8,'5.8'),(37,5,9,'5.9'),(38,6,1,'6.1'),(39,6,2,'6.2');
/*!40000 ALTER TABLE `subchapters` ENABLE KEYS */;
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

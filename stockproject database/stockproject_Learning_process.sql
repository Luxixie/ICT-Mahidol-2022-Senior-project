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
-- Table structure for table `Learning_process`
--

DROP TABLE IF EXISTS `Learning_process`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Learning_process` (
  `Learning_process id` int NOT NULL AUTO_INCREMENT,
  `AccountId` int NOT NULL,
  `chapter_id` int NOT NULL,
  `subchapters_id` int NOT NULL,
  `isLearned` tinyint NOT NULL DEFAULT '0',
  `Time` varchar(100) NOT NULL,
  PRIMARY KEY (`Learning_process id`),
  KEY `AccountId_idx` (`AccountId`),
  KEY `chapter_id_idx` (`chapter_id`),
  KEY `subchapters_id_idx` (`subchapters_id`),
  CONSTRAINT `AccountId` FOREIGN KEY (`AccountId`) REFERENCES `accounts` (`AccountId`),
  CONSTRAINT `chapter_id` FOREIGN KEY (`chapter_id`) REFERENCES `chapters` (`chapters id`),
  CONSTRAINT `subchapters_id` FOREIGN KEY (`subchapters_id`) REFERENCES `subchapters` (`subchapters_id`)
) ENGINE=InnoDB AUTO_INCREMENT=103 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Learning_process`
--

LOCK TABLES `Learning_process` WRITE;
/*!40000 ALTER TABLE `Learning_process` DISABLE KEYS */;
INSERT INTO `Learning_process` VALUES (10,1,1,1,1,'2023-03-18 21:46:40.798417'),(11,1,1,2,1,'2023-03-18 21:46:44.124888'),(13,1,2,1,1,''),(14,1,2,2,1,''),(15,1,3,1,1,''),(16,1,1,3,1,'2023-03-18 21:46:47.591688'),(17,2,2,1,1,''),(18,2,1,3,1,'2023-03-19 16:45:24.049427'),(19,2,2,10,1,'2023-03-19 16:46:49.234726'),(20,2,2,1,1,''),(21,2,3,7,1,'2023-03-19 16:47:30.909301'),(22,2,6,1,1,'2023-03-19 16:48:07.213371'),(23,2,4,1,1,''),(24,2,3,1,1,'2023-03-19 16:47:24.605922'),(25,2,3,2,1,''),(26,2,3,3,1,''),(27,2,3,4,1,'2023-03-19 16:47:29.039638'),(28,2,3,3,1,''),(29,2,3,2,1,''),(30,2,3,2,1,''),(31,2,4,1,1,''),(32,2,4,2,1,'2023-03-19 16:47:38.829584'),(33,2,4,3,1,'2023-03-19 16:47:39.241533'),(34,2,4,4,1,'2023-03-19 16:47:41.454708'),(35,2,4,5,1,'2023-03-19 16:47:41.861648'),(36,2,4,6,1,'2023-03-19 16:47:43.311356'),(37,2,4,7,1,'2023-03-19 16:47:43.742138'),(38,2,5,2,1,'2023-03-19 16:47:55.883075'),(39,2,5,3,1,'2023-03-19 16:47:56.312530'),(40,2,5,4,1,'2023-03-19 16:47:56.686772'),(41,2,5,5,1,'2023-03-19 16:47:57.117880'),(42,2,3,2,1,''),(43,2,1,1,1,'2023-03-19 16:45:20.966978'),(44,2,1,2,1,'2023-03-19 16:45:22.642731'),(45,2,1,4,1,'2023-03-19 16:45:25.238487'),(46,2,2,1,1,''),(47,2,6,2,1,''),(48,2,6,2,1,''),(49,2,6,2,1,''),(50,2,6,2,1,''),(51,2,6,2,1,''),(52,2,6,2,1,''),(53,2,6,2,1,''),(54,2,6,2,1,''),(55,2,6,2,1,''),(56,2,6,2,1,''),(57,2,6,2,1,''),(58,2,6,2,1,''),(59,2,6,2,1,''),(60,2,6,2,1,''),(61,2,5,8,1,'2023-03-19 16:47:59.330038'),(62,2,6,2,1,''),(68,24,2,1,1,'2023-03-23 20:37:05.986544'),(69,24,1,2,1,'2023-03-21 09:33:24.249731'),(70,24,6,1,1,'2023-03-23 21:00:01.248474'),(71,2,2,2,1,'2023-03-19 16:46:28.435723'),(72,2,2,3,1,'2023-03-19 16:46:30.675216'),(73,2,2,4,1,'2023-03-19 16:46:31.564397'),(74,2,2,5,1,'2023-03-19 16:46:32.333066'),(75,2,2,6,1,'2023-03-19 16:46:33.671853'),(76,2,2,7,1,'2023-03-19 16:46:35.050589'),(77,2,2,8,1,'2023-03-19 16:46:35.894644'),(78,2,2,9,1,'2023-03-19 16:46:48.985563'),(79,2,3,5,1,'2023-03-19 16:47:29.715094'),(80,2,3,6,1,'2023-03-19 16:47:30.253843'),(81,2,5,1,1,'2023-03-19 16:47:53.234994'),(82,2,5,6,1,'2023-03-19 16:47:57.503513'),(83,2,5,7,1,'2023-03-19 16:47:58.875921'),(84,2,5,9,1,'2023-03-19 16:47:59.761034'),(85,24,2,10,1,'2023-03-25 19:56:27.310817'),(86,24,1,3,1,'2023-03-21 13:38:05.482600'),(87,24,1,4,1,'2023-03-23 16:34:10.347291'),(88,24,4,7,1,'2023-03-24 15:11:40.378272'),(89,24,2,6,1,'2023-03-23 20:37:24.092356'),(90,24,6,2,1,'2023-03-23 21:00:05.594917'),(91,24,3,7,1,'2023-03-23 20:53:30.837915'),(92,24,5,2,1,'2023-03-23 17:04:34.361479'),(93,24,2,2,1,'2023-03-23 20:37:14.990661'),(94,24,2,3,1,'2023-03-23 20:37:17.901605'),(95,24,2,4,1,'2023-03-23 20:37:20.443737'),(96,24,2,5,1,'2023-03-23 20:37:21.776659'),(97,24,2,7,1,'2023-03-23 20:37:26.833916'),(98,24,2,8,1,'2023-03-23 20:37:29.352684'),(99,24,2,9,1,'2023-03-23 20:37:32.723445'),(100,1,4,7,1,'2023-03-23 21:09:31.240598'),(101,1,1,4,1,'2023-03-24 14:32:58.139380'),(102,1,2,10,1,'2023-03-24 14:33:03.252574');
/*!40000 ALTER TABLE `Learning_process` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-04-09 14:32:15
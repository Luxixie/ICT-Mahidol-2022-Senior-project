-- MySQL dump 10.13  Distrib 8.0.32, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: tester
-- ------------------------------------------------------
-- Server version	8.0.32

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
-- Table structure for table `transactions`
--

DROP TABLE IF EXISTS `transactions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `transactions` (
  `index` int NOT NULL AUTO_INCREMENT,
  `user_id` varchar(45) DEFAULT NULL,
  `ticker` varchar(45) DEFAULT NULL,
  `shares` int DEFAULT NULL,
  `action` varchar(45) DEFAULT NULL,
  `cost` float DEFAULT NULL,
  `timestamp` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`index`)
) ENGINE=InnoDB AUTO_INCREMENT=37 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `transactions`
--

LOCK TABLES `transactions` WRITE;
/*!40000 ALTER TABLE `transactions` DISABLE KEYS */;
INSERT INTO `transactions` VALUES (1,NULL,'AOT.BK',5,'buy',363.75,'2023-02-14 00:13:59'),(2,NULL,'PLANB.BK',100,'buy',900,'2023-02-14 00:15:20'),(3,NULL,'PLANB.BK',100,'buy',905,'2023-02-14 13:03:08'),(4,'1','AOT.BK',100,'buy',7300,'2023-02-21 02:14:03'),(5,'1','AOT.BK',100,'buy',7250,'2023-02-26 01:22:04'),(6,'1','PLANB.BK',100,'buy',970,'2023-02-26 01:35:56'),(7,'1','PLANB.BK',1000,'buy',9700,'2023-02-27 01:30:08'),(8,'1','PLANB.BK',100,'buy',910,'2023-03-05 00:53:00'),(9,'2','siri.bk',100,'buy',189,'2023-03-07 10:59:43'),(10,'2','siri.bk',200,'buy',382,'2023-03-07 11:40:07'),(11,'2','siri.bk',400,'buy',764,'2023-03-07 11:41:09'),(12,'2','siri.bk',100,'buy',191,'2023-03-07 12:13:36'),(13,'2','bch.bk',100,'buy',1930,'2023-03-07 13:11:15'),(14,'3','bch.bk',200,'buy',3980,'2023-03-09 22:34:38'),(15,'3','bch.bk',300,'buy',5970,'2023-03-09 22:34:49'),(16,'2','PLANB.BK',100,'buy',910,'2023-03-09 23:31:02'),(17,'3','siri.bk',100,'buy',1.71,'2023-03-30 12:07:47');
/*!40000 ALTER TABLE `transactions` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-03-31 13:29:52

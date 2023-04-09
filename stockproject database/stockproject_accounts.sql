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
-- Table structure for table `accounts`
--

DROP TABLE IF EXISTS `accounts`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `accounts` (
  `AccountId` int NOT NULL AUTO_INCREMENT,
  `FirstName` varchar(45) NOT NULL,
  `LastName` varchar(45) NOT NULL,
  `Region` varchar(45) NOT NULL,
  `BOD` date NOT NULL,
  `Email` varchar(45) NOT NULL,
  `Password` varchar(45) NOT NULL,
  `LoginToken` varchar(45) NOT NULL,
  `Balance` float NOT NULL DEFAULT '20000',
  `profit` float NOT NULL,
  PRIMARY KEY (`AccountId`)
) ENGINE=InnoDB AUTO_INCREMENT=26 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `accounts`
--

LOCK TABLES `accounts` WRITE;
/*!40000 ALTER TABLE `accounts` DISABLE KEYS */;
INSERT INTO `accounts` VALUES (1,'admin','admin','test','2023-02-06','test@hotmail.com','admin123','zxcvbnmasdfghjklqwertyuiop',20000,0),(2,'test1','test2','TH','2023-02-07','test@123.com','123454321','zxcvbnmasdfghjklqwertyuiopasd',20000,0),(9,'','','','2023-02-07','123@qq.com','123456789o0p','zxcvbnmasdfghjklqwertyuiopasd',20000,0),(10,'','','','2023-02-07','345@qq.com','11234567','zxcvbnmasdfghjklqwertyuiopasd',20000,0),(11,'test4','test4','AF','2023-02-07','test4@qq.com','13245?!','zxcvbnmasdfghjklqwertyuiopasd',20000,0),(12,'234sd','12ges','','2023-02-07','123@qq.com','123456?!','zxcvbnmasdfghjklqwertyuiopasd',20000,0),(13,'1223333','ertg','','2023-02-07','123@123.com','22!','zxcvbnmasdfghjklqwertyuiopasd',20000,0),(14,'12','2e','','2023-02-07','1234@ca.com','12!','zxcvbnmasdfghjklqwertyuiopasd',20000,0),(15,'sa','1d','','2023-02-07','123@qq.com','1!','zxcvbnmasdfghjklqwertyuiopasd',20000,0),(16,'12e','d','','2023-02-07','123@qq.com','2e!','zxcvbnmasdfghjklqwertyuiopasd',20000,0),(17,'ww','ww','','2023-02-07','33@qq.com','ww1@','zxcvbnmasdfghjklqwertyuiopasd',20000,0),(18,'sdd','ss1','','2023-02-07','1234@qq.com','1!2','zxcvbnmasdfghjklqwertyuiopasd',20000,0),(19,'s','1','','2023-02-07','444@qq.com','11!','zxcvbnmasdfghjklqwertyuiopasd',20000,0),(20,'vcjs','22s','','2023-02-07','1224@qq.com','74!','zxcvbnmasdfghjklqwertyuiopasd',20000,0),(21,'xcvhgj','hbhsb','TH','2023-02-07','653@example.com','12334!','zxcvbnmasdfghjklqwertyuiopasd',20000,0),(22,' fdr','gsg','','2023-02-07','q2w@xx.com','123!','zxcvbnmasdfghjklqwertyuiopasd',20000,0),(23,'test5','test5','DZ','2023-02-14','test5@example.com','123!','zxcvbnmasdfghjklqwertyuiopasd',20000,0),(24,'xixi','XIE','CN','2023-03-13','2906848483@qq.com','njbhgv!A1','zxcvbnmasdfghjklqwertyuiopasd',19448.6,0),(25,'n','nnn','','2026-04-28','2906848483@qq.com','njbhgv!A1','zxcvbnmasdfghjklqwertyuiopasd',20000,0);
/*!40000 ALTER TABLE `accounts` ENABLE KEYS */;
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

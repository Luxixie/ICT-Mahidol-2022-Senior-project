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
  `Balance` float NOT NULL DEFAULT '100000',
  `profit` float NOT NULL DEFAULT '0',
  `timestamp` varchar(100) NOT NULL,
  PRIMARY KEY (`AccountId`)
) ENGINE=InnoDB AUTO_INCREMENT=46 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `accounts`
--

LOCK TABLES `accounts` WRITE;
/*!40000 ALTER TABLE `accounts` DISABLE KEYS */;
INSERT INTO `accounts` VALUES (1,'admin','admin','test','2023-02-06','test@hotmail.com','Admin123?','zxcvbnmasdfghjklqwertyuiopasd',100000,0,''),(2,'test1','test2','TH','2023-02-07','test@123.com','123454321','zxcvbnmasdfghjklqwertyuiopasd',100000,0,''),(24,'xixi','XIE','CN','2023-03-13','2906848483@qq.com','njbhgv!A1','zxcvbnmasdfghjklqwertyuiopasd',84710,0,''),(25,'n','nnn','','2026-04-28','2906848483@qq.com','njbhgv!A1','zxcvbnmasdfghjklqwertyuiopasd',100000,0,''),(26,'dd','ww','CN','2020-04-28','112233@qq.com','dscdc13','zxcvbnmasdfghjklqwertyuiopasd',52610,0,''),(27,'d','s','CN','2020-04-27','sxac@qq.com','sddsn12','zxcvbnmasdfghjklqwertyuiopasd',99110,0,''),(28,'Acccc','Bccccc','AF','2020-04-07','Acccc@qq.com','assjA1?11','zxcvbnmasdfghjklqwertyuiopasd',74606,0,''),(29,'Acccc','Bccccc','AF','2020-04-07','Acccc@qq.com','assjA1?11','zxcvbnmasdfghjklqwertyuiopasd',100000,0,''),(30,'saafs','dsvadf','AL','2023-04-02','saafs@qq.com','Asadnjeda1!','zxcvbnmasdfghjklqwertyuiopasd',100000,0,''),(31,'njbhgv','jbkhgvb','AF','2023-04-17','njbhgv@qq.com','Adsmknjkbhf!1','zxcvbnmasdfghjklqwertyuiopasd',100000,0,''),(32,'dsfe','dswfe','AL','2023-03-26','dsfe@qq.com','dssdA1!1w','zxcvbnmasdfghjklqwertyuiopasd',100000,0,''),(33,'dsdk','sejlw','AL','2023-04-02','dsdk@qq.com','Bbjuoaeiqw!1','zxcvbnmasdfghjklqwertyuiopasd',100000,0,''),(42,'yyq2','YANG','CN','2018-04-16','yyq2@qq.com','sdnA!1ww','zxcvbnmasdfghjklqwertyuiopasd',99802,0,'2023-04-23 11:07:36'),(45,'cfffcdx','sdefgb','AR','2023-05-28','2eew3@qq.com','rdsgshr1!Q','zxcvbnmasdfghjklqwertyuiopasd',100000,0,'2023-05-01 23:36:44');
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

-- Dump completed on 2023-05-27 10:10:54

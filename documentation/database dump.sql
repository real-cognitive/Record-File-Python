-- MySQL dump 10.13  Distrib 8.0.43, for Win64 (x86_64)
--
-- Host: localhost    Database: music
-- ------------------------------------------------------
-- Server version	8.0.43

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
-- Table structure for table `auth`
--

DROP TABLE IF EXISTS `auth`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth` (
  `id` int NOT NULL AUTO_INCREMENT,
  `Username` varchar(40) DEFAULT NULL,
  `Password` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `Email` (`Username`),
  UNIQUE KEY `Username` (`Username`)
) ENGINE=InnoDB AUTO_INCREMENT=20 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth`
--

LOCK TABLES `auth` WRITE;
/*!40000 ALTER TABLE `auth` DISABLE KEYS */;
INSERT INTO `auth` VALUES (7,'lkmlkm','123'),(8,'admin','1234'),(15,'new_acc','123'),(17,'ishan','123456'),(18,'test','mvn123'),(19,'User1','12345');
/*!40000 ALTER TABLE `auth` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `gen_mood`
--

DROP TABLE IF EXISTS `gen_mood`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `gen_mood` (
  `Genre` varchar(30) NOT NULL,
  `mood` varchar(30) DEFAULT NULL,
  PRIMARY KEY (`Genre`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `gen_mood`
--

LOCK TABLES `gen_mood` WRITE;
/*!40000 ALTER TABLE `gen_mood` DISABLE KEYS */;
INSERT INTO `gen_mood` VALUES ('blues','sad'),('jazz','calm'),('metal','angry'),('pop','happy'),('r-n-b','romantic'),('rock','energetic'),('world','varied');
/*!40000 ALTER TABLE `gen_mood` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `playlist`
--

DROP TABLE IF EXISTS `playlist`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `playlist` (
  `pid` int NOT NULL AUTO_INCREMENT,
  `Name` varchar(40) DEFAULT NULL,
  `playlist_data` json DEFAULT NULL,
  `uid` int DEFAULT NULL,
  PRIMARY KEY (`pid`),
  KEY `uid` (`uid`),
  CONSTRAINT `playlist_ibfk_1` FOREIGN KEY (`uid`) REFERENCES `auth` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=15 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `playlist`
--

LOCK TABLES `playlist` WRITE;
/*!40000 ALTER TABLE `playlist` DISABLE KEYS */;
INSERT INTO `playlist` VALUES (12,'New Test Playlist','[{\"id\": \"0q84FggW57NXGtLHoetS0Y\", \"art\": \"https://i.scdn.co/image/ab67616d00001e02d5754cde395f5c46792186c7\", \"name\": \"Pardesiya - From \\\"Param Sundari\\\"\"}, {\"id\": \"1ko2lVN0vKGUl9zrU0qSlT\", \"art\": \"https://i.scdn.co/image/ab67616d00001e02472fbc1d5743c7d3c75b9ec0\", \"name\": \"Just the Two of Us (feat. Bill Withers)\"}, {\"id\": \"5fdNHVZHbWB1AaXk4RBGVD\", \"art\": \"https://i.scdn.co/image/ab67616d00001e02d8e0e065037b496212e554b7\", \"name\": \"Just the Two of Us\"}]',8),(13,'Playlist 2','[]',8),(14,'Playlist 3','[]',8);
/*!40000 ALTER TABLE `playlist` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2026-02-01 23:39:21

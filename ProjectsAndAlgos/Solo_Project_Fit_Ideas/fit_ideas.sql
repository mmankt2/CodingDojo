-- MySQL dump 10.13  Distrib 5.7.26, for Linux (i686)
--
-- Host: localhost    Database: fit_ideas
-- ------------------------------------------------------
-- Server version	5.7.26-0ubuntu0.16.04.1

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `exercises`
--

DROP TABLE IF EXISTS `exercises`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `exercises` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) DEFAULT NULL,
  `description` varchar(255) DEFAULT NULL,
  `picture_path` varchar(255) DEFAULT NULL,
  `created_at` datetime DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `exercises`
--

LOCK TABLES `exercises` WRITE;
/*!40000 ALTER TABLE `exercises` DISABLE KEYS */;
INSERT INTO `exercises` VALUES (1,'bicep curl','bicep curl with elbows at sides','','2019-07-07 20:55:43','2019-07-07 20:55:43');
/*!40000 ALTER TABLE `exercises` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `exercises_routines`
--

DROP TABLE IF EXISTS `exercises_routines`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `exercises_routines` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `exercise_key` int(11) DEFAULT NULL,
  `routine_key` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `exercise_key` (`exercise_key`),
  KEY `routine_key` (`routine_key`),
  CONSTRAINT `exercises_routines_ibfk_1` FOREIGN KEY (`exercise_key`) REFERENCES `exercises` (`id`),
  CONSTRAINT `exercises_routines_ibfk_2` FOREIGN KEY (`routine_key`) REFERENCES `routines` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `exercises_routines`
--

LOCK TABLES `exercises_routines` WRITE;
/*!40000 ALTER TABLE `exercises_routines` DISABLE KEYS */;
/*!40000 ALTER TABLE `exercises_routines` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `movement_categories`
--

DROP TABLE IF EXISTS `movement_categories`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `movement_categories` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `category` varchar(30) DEFAULT NULL,
  `created_at` datetime DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `movement_categories`
--

LOCK TABLES `movement_categories` WRITE;
/*!40000 ALTER TABLE `movement_categories` DISABLE KEYS */;
INSERT INTO `movement_categories` VALUES (1,'push','2019-07-07 20:54:30','2019-07-07 20:54:30'),(2,'pull','2019-07-10 21:23:12','2019-07-10 21:23:12'),(3,'hinge','2019-07-10 21:23:25','2019-07-10 21:23:25'),(4,'trunk rotation','2019-07-10 21:23:34','2019-07-10 21:23:34'),(5,'single leg','2019-07-10 21:23:45','2019-07-10 21:23:45'),(6,'trunk flexion/extension','2019-07-10 21:24:12','2019-07-10 21:24:12');
/*!40000 ALTER TABLE `movement_categories` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `movement_categories_exercises`
--

DROP TABLE IF EXISTS `movement_categories_exercises`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `movement_categories_exercises` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `category_key` int(11) DEFAULT NULL,
  `exercise_key` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `exercise_key` (`exercise_key`),
  KEY `category_key` (`category_key`),
  CONSTRAINT `movement_categories_exercises_ibfk_1` FOREIGN KEY (`exercise_key`) REFERENCES `exercises` (`id`),
  CONSTRAINT `movement_categories_exercises_ibfk_2` FOREIGN KEY (`category_key`) REFERENCES `movement_categories` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `movement_categories_exercises`
--

LOCK TABLES `movement_categories_exercises` WRITE;
/*!40000 ALTER TABLE `movement_categories_exercises` DISABLE KEYS */;
INSERT INTO `movement_categories_exercises` VALUES (1,1,1);
/*!40000 ALTER TABLE `movement_categories_exercises` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `routines`
--

DROP TABLE IF EXISTS `routines`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `routines` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `description` varchar(255) DEFAULT NULL,
  `last_used` datetime DEFAULT NULL,
  `playlist_path` varchar(255) DEFAULT NULL,
  `created_at` datetime DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `routines`
--

LOCK TABLES `routines` WRITE;
/*!40000 ALTER TABLE `routines` DISABLE KEYS */;
/*!40000 ALTER TABLE `routines` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `users` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `first_name` varchar(100) DEFAULT NULL,
  `last_name` varchar(100) DEFAULT NULL,
  `email` varchar(255) DEFAULT NULL,
  `password` varchar(255) DEFAULT NULL,
  `created_at` datetime DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users`
--

LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `users` VALUES (1,'Melissa','Littleton','mmankt2@gmail.com','$2b$12$vkgRFwY2k/qYK2E6cljL4O2cUbmnzIPq.Bi9yLQSpaSJ7GAyK2ggq','2019-07-10 21:31:07','2019-07-10 21:31:07');
/*!40000 ALTER TABLE `users` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2019-07-11 10:57:57

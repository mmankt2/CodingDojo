-- MySQL dump 10.13  Distrib 5.7.26, for Linux (i686)
--
-- Host: localhost    Database: basic_registration
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
-- Table structure for table `tweets`
--

DROP TABLE IF EXISTS `tweets`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `tweets` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) DEFAULT NULL,
  `content` text,
  `created_at` datetime DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL,
  `likes` int(11) DEFAULT '0',
  PRIMARY KEY (`id`),
  KEY `user_id` (`user_id`),
  CONSTRAINT `tweets_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=22 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tweets`
--

LOCK TABLES `tweets` WRITE;
/*!40000 ALTER TABLE `tweets` DISABLE KEYS */;
INSERT INTO `tweets` VALUES (20,15,'new tweet\r\n','2019-06-09 20:18:15','2019-06-09 20:18:15',4),(21,15,'newer tweet','2019-06-09 20:21:10','2019-06-09 20:21:10',2);
/*!40000 ALTER TABLE `tweets` ENABLE KEYS */;
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
  `password` varchar(255) DEFAULT NULL,
  `created_at` datetime DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL,
  `email` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=17 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users`
--

LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `users` VALUES (1,'melissa','littleton','$2b$12$aqeGOtYKsNWfcCPclQfID.au/Yr42DymH4J8im9oz5ewbCxXjbfVW','2019-06-09 09:10:37','2019-06-09 09:10:37',NULL),(2,'melissa','littleton','$2b$12$iWdqT3.NcvBbJtIg5rYYQeu7pBbwzTdFmDRrACi2w5f2ZwFIgfFo2','2019-06-09 09:11:29','2019-06-09 09:11:29',NULL),(3,'melissa','littleton','$2b$12$j97N5dm1xW2s4BDqMw7WvebT0XvSd5JahVF8WG5mqai2rRiPKXOGu','2019-06-09 09:32:47','2019-06-09 09:32:47',NULL),(4,'paul','littleton','$2b$12$QubUp4KLG1Sk6e1ZKbb17exHLAelQADuqXImJEQx5lJc07DFmLmZi','2019-06-09 09:44:22','2019-06-09 09:44:22',NULL),(5,'melissa','littleton','$2b$12$lPid/ke6ncZ7sF9CJqn.PeREp0buBZo.tH1C3WnjR36O0P.SW0xt6','2019-06-09 09:45:01','2019-06-09 09:45:01',NULL),(6,'melissa','littleton','$2b$12$u9WbocP02B0vhDjJ6bX/nO/0rtTK8twBybW23.Klfcap94XUiD6Fi','2019-06-09 09:46:34','2019-06-09 09:46:34',NULL),(7,'paul','littleton','$2b$12$VVlkPC/N68Jo8pT5MFoAqeRR7UkOH5JVQgl1APnrifR73YVPEZ4Wm','2019-06-09 09:48:44','2019-06-09 09:48:44',NULL),(8,'melissa','littleton','$2b$12$7DiapXAJJi6GCol3N4LK5ODQFKd6ya2MsSP1klm68Lg/qs7KWtqxe','2019-06-09 09:56:08','2019-06-09 09:56:08',NULL),(9,'melissa','littleton','$2b$12$cYbBfNtwzvMaQr6r.o61tez5CalssbPIK.yUKc0ipVzvtOqBu/vSu','2019-06-09 09:56:47','2019-06-09 09:56:47',NULL),(10,'melissa','littleton','$2b$12$PJJlVhW9GvPSwl.ZliAFDehxooDLbb8jt0IqaCAr.bgbGJ10ijDkK','2019-06-09 10:16:41','2019-06-09 10:16:41',NULL),(11,'melissa','littleton','$2b$12$8Gu.HDqIsZx8bxSLYQDKDuT2OhIB4UfrxCgvaIQJKRn4bo1PwM8dq','2019-06-09 10:17:58','2019-06-09 10:17:58',NULL),(12,'melissa','littleton','$2b$12$ehcHyZ1sLkkXV94htRwICuJR0AhjXrO4/lBaJubLIh2D.Pu.AartS','2019-06-09 10:24:11','2019-06-09 10:24:11',NULL),(13,'paul','littleton','p@gmail.com','2019-06-09 10:26:26','2019-06-09 10:26:26','$2b$12$5pOrPaN00dkgIR8vNjlKP.ycIuHRt8jUzuFFPJ/PXHUtn1ZQHPE4u'),(14,'paul','littleton','$2b$12$6qhTU9VMK2nkxAu.4AmeSOwSwpLrxeaIR6QxDrsHN2CiVq91fjE5K','2019-06-09 10:27:33','2019-06-09 10:27:33','p@gmail.com'),(15,'Melissa','Littleton','$2b$12$cwzvS54LkcuNSTcJ.Xk73O87nRrNdX5uwA28zateGc16AKFJPSj3e','2019-06-09 16:53:16','2019-06-09 16:53:16','mmankt2@gmail.com'),(16,'Melissa','Littleton','$2b$12$5oTD0luY1BwQlawhctXN2OY3JmhGAMdSXhMSqK0q3Q1lZt9bmoH4a','2019-06-09 16:59:28','2019-06-09 16:59:28','melissa@gmail.com');
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

-- Dump completed on 2019-06-09 20:28:22

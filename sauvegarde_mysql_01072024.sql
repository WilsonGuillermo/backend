-- MySQL dump 10.13  Distrib 8.0.37, for Linux (x86_64)
--
-- Host: localhost    Database: boutique
-- ------------------------------------------------------
-- Server version	8.0.37-0ubuntu0.22.04.3

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
-- Current Database: `boutique`
--

CREATE DATABASE /*!32312 IF NOT EXISTS*/ `boutique` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;

USE `boutique`;

--
-- Table structure for table `carta`
--

DROP TABLE IF EXISTS `carta`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `carta` (
  `id_carta` int NOT NULL AUTO_INCREMENT,
  `lista_de_menus` varchar(255) NOT NULL,
  `lista_de_platos` varchar(255) NOT NULL,
  `lista_de_bebidas` varchar(255) NOT NULL,
  `lista_de_postres` varchar(255) NOT NULL,
  PRIMARY KEY (`id_carta`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci COMMENT='tabla de la carta';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `carta`
--

LOCK TABLES `carta` WRITE;
/*!40000 ALTER TABLE `carta` DISABLE KEYS */;
/*!40000 ALTER TABLE `carta` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `categorias`
--

DROP TABLE IF EXISTS `categorias`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `categorias` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `description` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `categorias`
--

LOCK TABLES `categorias` WRITE;
/*!40000 ALTER TABLE `categorias` DISABLE KEYS */;
INSERT INTO `categorias` VALUES (1,'Ropa Femenina','Disponemos de las mejores prendas femeninas'),(2,'Ropa Masculina','Disponemos de la mejor ropa masculina');
/*!40000 ALTER TABLE `categorias` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `imagenes`
--

DROP TABLE IF EXISTS `imagenes`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `imagenes` (
  `id` int NOT NULL AUTO_INCREMENT,
  `product_id` int DEFAULT NULL,
  `url` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `product_id` (`product_id`),
  CONSTRAINT `imagenes_ibfk_1` FOREIGN KEY (`product_id`) REFERENCES `productos` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `imagenes`
--

LOCK TABLES `imagenes` WRITE;
/*!40000 ALTER TABLE `imagenes` DISABLE KEYS */;
INSERT INTO `imagenes` VALUES (1,1,'https://th.bing.com/th/id/OLC.GvENwSFhFW5ChQ480x360?&rs=1&pid=ImgDetMain'),(2,2,'https://maribelarangonovias.com/wp-content/uploads/2020/11/MG_9930.jpg'),(3,3,'https://th.bing.com/th?id=OLC.w4A/SbSSI/Zabw480x360&rs=1&pid=ImgDetMain'),(4,4,'https://maribelarangonovias.com/wp-content/uploads/2020/09/doce.jpg'),(5,5,'https://th.bing.com/th/id/OLC.gYfgB4IYmcVFig480x360?&rs=1&pid=ImgDetMain'),(6,6,'https://th.bing.com/th?id=OLC.rnJ8dmyxA+wZxA480x360&rs=1&pid=ImgDetMain'),(7,7,'https://th.bing.com/th/id/OLC.sVc64BRWRsWI2g480x360?&rs=1&pid=ImgDetMain'),(8,8,'https://th.bing.com/th?id=OLC.ls9L+5+CHEqGMA480x360&rs=1&pid=ImgDetMain'),(9,9,'https://th.bing.com/th/id/OLC.vkP0MvMuYYqfjg480x360?&rs=1&pid=ImgDetMain');
/*!40000 ALTER TABLE `imagenes` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `informal`
--

DROP TABLE IF EXISTS `informal`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `informal` (
  `id_informal` int NOT NULL AUTO_INCREMENT,
  `lista_de_sandwiches` varchar(255) NOT NULL,
  `lista_de_bebidas` varchar(255) NOT NULL,
  `lista_de_postres` varchar(255) NOT NULL,
  PRIMARY KEY (`id_informal`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci COMMENT='tabla de productos informales';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `informal`
--

LOCK TABLES `informal` WRITE;
/*!40000 ALTER TABLE `informal` DISABLE KEYS */;
/*!40000 ALTER TABLE `informal` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `ingredientes`
--

DROP TABLE IF EXISTS `ingredientes`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `ingredientes` (
  `id_ingrediente` int NOT NULL AUTO_INCREMENT,
  `nombre` varchar(255) NOT NULL,
  `cantidad` int NOT NULL,
  `fecha_vencimiento` date NOT NULL,
  PRIMARY KEY (`id_ingrediente`),
  UNIQUE KEY `UC_ingredientes` (`id_ingrediente`,`nombre`),
  KEY `nombre` (`nombre`),
  KEY `nombre_2` (`nombre`,`cantidad`),
  CONSTRAINT `fk_nombre_ingredientes` FOREIGN KEY (`nombre`) REFERENCES `referencia_ingredientes` (`nombre`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci COMMENT='tabla de productos';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ingredientes`
--

LOCK TABLES `ingredientes` WRITE;
/*!40000 ALTER TABLE `ingredientes` DISABLE KEYS */;
INSERT INTO `ingredientes` VALUES (3,'bare',17,'2028-10-10'),(4,'azucar',62,'2028-10-10'),(5,'bocachico',15,'2027-12-12'),(6,'atun',15,'2027-12-12');
/*!40000 ALTER TABLE `ingredientes` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `menus`
--

DROP TABLE IF EXISTS `menus`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `menus` (
  `id_menu` int NOT NULL AUTO_INCREMENT,
  `nombre` varchar(255) NOT NULL,
  `descripcion` text,
  `precio` decimal(10,2) NOT NULL,
  `ingredientes_principales` text,
  `fecha_creacion` datetime NOT NULL,
  PRIMARY KEY (`id_menu`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci COMMENT='tabla de los menus';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `menus`
--

LOCK TABLES `menus` WRITE;
/*!40000 ALTER TABLE `menus` DISABLE KEYS */;
/*!40000 ALTER TABLE `menus` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `pedidos`
--

DROP TABLE IF EXISTS `pedidos`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `pedidos` (
  `id` int NOT NULL AUTO_INCREMENT,
  `id_menu` int DEFAULT NULL,
  `id_plato_carta` int DEFAULT NULL,
  `cantidad` int NOT NULL,
  `fecha_pedido` datetime NOT NULL,
  PRIMARY KEY (`id`),
  KEY `id_menu` (`id_menu`),
  KEY `id_plato_carta` (`id_plato_carta`),
  CONSTRAINT `pedidos_ibfk_1` FOREIGN KEY (`id_menu`) REFERENCES `menus` (`id_menu`),
  CONSTRAINT `pedidos_ibfk_2` FOREIGN KEY (`id_plato_carta`) REFERENCES `platos_carta` (`id_platos`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci COMMENT='tabla de los pedidos';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `pedidos`
--

LOCK TABLES `pedidos` WRITE;
/*!40000 ALTER TABLE `pedidos` DISABLE KEYS */;
/*!40000 ALTER TABLE `pedidos` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `platos_carta`
--

DROP TABLE IF EXISTS `platos_carta`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `platos_carta` (
  `id_platos` int NOT NULL AUTO_INCREMENT,
  `nombre` varchar(255) NOT NULL,
  `descripcion` text,
  `precio` decimal(10,2) NOT NULL,
  `ingredientes_principales` text,
  `fecha_creacion` datetime NOT NULL,
  PRIMARY KEY (`id_platos`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci COMMENT='tabla de los platos a la carta';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `platos_carta`
--

LOCK TABLES `platos_carta` WRITE;
/*!40000 ALTER TABLE `platos_carta` DISABLE KEYS */;
/*!40000 ALTER TABLE `platos_carta` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `productos`
--

DROP TABLE IF EXISTS `productos`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `productos` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `description` varchar(255) DEFAULT NULL,
  `price` decimal(10,2) NOT NULL,
  `category_id` int NOT NULL,
  `size` varchar(50) DEFAULT NULL,
  `color` varchar(50) DEFAULT NULL,
  `stock` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `category_id` (`category_id`),
  CONSTRAINT `productos_ibfk_1` FOREIGN KEY (`category_id`) REFERENCES `categorias` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `productos`
--

LOCK TABLES `productos` WRITE;
/*!40000 ALTER TABLE `productos` DISABLE KEYS */;
INSERT INTO `productos` VALUES (1,'Vestido Rojo','Vestido de verano',49.99,1,'M','Rojo',10),(2,'Camisa Azul clara','Camisa casual',29.99,2,'L','Azul',15),(3,'Vestido Blanco','Vestido de verano',49.99,1,'M','Rojo',10),(4,'Camisa Rosada','Camisa casual',29.99,2,'L','Azul',15),(5,'Vestido Amarillo','Vestido de verano',49.99,1,'M','Rojo',10),(6,'Camisa Blanca','Camisa casual',29.99,2,'L','Azul',15),(7,'Vestido Largo','Vestido de verano',49.99,1,'M','Rojo',10),(8,'Falda de colores','Camisa casual',29.99,2,'L','Azul',15),(9,'Vestido Corto Azul','Vestido de verano',49.99,1,'M','Rojo',10);
/*!40000 ALTER TABLE `productos` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `referencia_ingredientes`
--

DROP TABLE IF EXISTS `referencia_ingredientes`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `referencia_ingredientes` (
  `id` int NOT NULL AUTO_INCREMENT,
  `categoria` varchar(255) NOT NULL,
  `nombre` varchar(255) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `unica_nombre_referencia_ingredientes` (`nombre`),
  KEY `nombre` (`nombre`),
  KEY `fk_categoria_referencia_ingredientes` (`categoria`),
  CONSTRAINT `fk_categoria_referencia_ingredientes` FOREIGN KEY (`categoria`) REFERENCES `referencia_tipos_ingredientes` (`categoria`)
) ENGINE=InnoDB AUTO_INCREMENT=22 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci COMMENT='tabla de productos utilisados';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `referencia_ingredientes`
--

LOCK TABLES `referencia_ingredientes` WRITE;
/*!40000 ALTER TABLE `referencia_ingredientes` DISABLE KEYS */;
INSERT INTO `referencia_ingredientes` VALUES (1,'carnes','entrecote'),(2,'pescados','dorada'),(3,'lacteos','leche'),(4,'lacteos','mantequilla'),(5,'granos','arroz'),(6,'enlatados','sardinas'),(7,'abarrotes','panelas'),(8,'carnes','fauxfilet'),(9,'pescados','bocachico'),(10,'lacteos','queso'),(11,'granos','lentejas'),(12,'enlatados','atun'),(13,'abarrotes','azucar'),(14,'abarrotes','sal'),(15,'carnes','steak'),(16,'pescados','bare'),(17,'lacteos','yogurt'),(18,'granos','frijoles'),(19,'enlatados','cangrejos'),(20,'condimentos','pimienta'),(21,'condimentos','oregano');
/*!40000 ALTER TABLE `referencia_ingredientes` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `referencia_tipos_ingredientes`
--

DROP TABLE IF EXISTS `referencia_tipos_ingredientes`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `referencia_tipos_ingredientes` (
  `id` int NOT NULL AUTO_INCREMENT,
  `categoria` varchar(255) NOT NULL,
  `unidad` varchar(255) NOT NULL,
  `perecedero` bit(1) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `unica_categoria_referencia_typos_ingredientes` (`categoria`),
  KEY `categoria` (`categoria`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci COMMENT='tabla de los tipos de productos';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `referencia_tipos_ingredientes`
--

LOCK TABLES `referencia_tipos_ingredientes` WRITE;
/*!40000 ALTER TABLE `referencia_tipos_ingredientes` DISABLE KEYS */;
INSERT INTO `referencia_tipos_ingredientes` VALUES (1,'carnes','gramos',_binary ''),(2,'pescados','gramos',_binary ''),(3,'lacteos','centilitros',_binary ''),(4,'granos','gramos',_binary '\0'),(5,'enlatados','gramos',_binary '\0'),(6,'abarrotes','gramos',_binary '\0'),(7,'condimentos','gramos',_binary '\0');
/*!40000 ALTER TABLE `referencia_tipos_ingredientes` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `referencial_mesas`
--

DROP TABLE IF EXISTS `referencial_mesas`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `referencial_mesas` (
  `id_mesa` int NOT NULL AUTO_INCREMENT,
  `numero_cubiertos_tabla` int DEFAULT NULL,
  PRIMARY KEY (`id_mesa`),
  UNIQUE KEY `UC_referencial_mesas` (`id_mesa`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci COMMENT='tabla de las mesas';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `referencial_mesas`
--

LOCK TABLES `referencial_mesas` WRITE;
/*!40000 ALTER TABLE `referencial_mesas` DISABLE KEYS */;
INSERT INTO `referencial_mesas` VALUES (1,6),(2,4),(3,8),(4,2);
/*!40000 ALTER TABLE `referencial_mesas` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `roles`
--

DROP TABLE IF EXISTS `roles`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `roles` (
  `id_rol` int NOT NULL AUTO_INCREMENT,
  `nombre_del_rol` varchar(255) NOT NULL,
  `derechos` varchar(255) NOT NULL,
  PRIMARY KEY (`id_rol`),
  UNIQUE KEY `UC_roles` (`id_rol`,`nombre_del_rol`),
  KEY `nombre_del_rol` (`nombre_del_rol`),
  KEY `derechos` (`derechos`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci COMMENT='tabla de roles';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `roles`
--

LOCK TABLES `roles` WRITE;
/*!40000 ALTER TABLE `roles` DISABLE KEYS */;
INSERT INTO `roles` VALUES (1,'Admin','cocina, sala, bar, mantenimiento, stockage_alimentacion, caja'),(2,'Responsable','stockage_alimentacion, sala, bar, mantenimiento, caja'),(3,'Cocinero','cocina, bar, mantenimiento, stockage_alimentacion'),(4,'Vendedor','sala, bar, mantenimiento, caja'),(5,'Aseador','cocina, sala, bar, mantenimiento');
/*!40000 ALTER TABLE `roles` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `usuarios`
--

DROP TABLE IF EXISTS `usuarios`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `usuarios` (
  `id_usuario` int NOT NULL AUTO_INCREMENT,
  `nombre` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_bin NOT NULL,
  `apellido` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_bin NOT NULL,
  `nombre_usuario` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_bin NOT NULL,
  `contrasena` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_bin NOT NULL,
  `rol` varchar(255) NOT NULL,
  `email` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_bin NOT NULL,
  `fecha_de_nacimiento` date NOT NULL,
  `fecha_creacion_cuenta` datetime NOT NULL,
  PRIMARY KEY (`id_usuario`),
  UNIQUE KEY `UC_nombre_usuario` (`nombre_usuario`),
  KEY `nombre_usuario` (`nombre_usuario`),
  KEY `rol` (`rol`),
  CONSTRAINT `fk_categoria_usuario_rol` FOREIGN KEY (`rol`) REFERENCES `roles` (`nombre_del_rol`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci COMMENT='tabla de los utilisadores';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `usuarios`
--

LOCK TABLES `usuarios` WRITE;
/*!40000 ALTER TABLE `usuarios` DISABLE KEYS */;
INSERT INTO `usuarios` VALUES (1,'Wilson','MOSQUERA','Wilson','WilsonMemo1$','Admin','wilsonmemo@hotmail.com','1964-04-14','2024-06-14 11:35:15'),(3,'Guillermo','Mosquera','GuillermoM','WilsonMemo11$','Vendedor','guillermo@eureka.com','1999-06-21','2024-06-21 17:02:57'),(4,'Martha','Rodriguez','Martha','WilsonMemo111$','Vendedor','martha@vitry.com','1999-06-22','2024-06-22 09:33:18');
/*!40000 ALTER TABLE `usuarios` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-07-01 13:52:56

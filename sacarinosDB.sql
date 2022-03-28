
-- phpMyAdmin SQL Dump
-- version 5.0.4deb2
-- https://www.phpmyadmin.net/
--
-- Host: localhost:3306
-- Generation Time: Mar 25, 2022 at 12:28 PM
-- Server version: 8.0.28
-- PHP Version: 7.4.28

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `sacarinosDB`
--

-- --------------------------------------------------------

--
-- Table structure for table `espana`
--

CREATE TABLE `espana` (
  `id` int NOT NULL,
  `tipoVehiculo` varchar(45) DEFAULT NULL,
  `cantidad` int DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;

-- --------------------------------------------------------

--
-- Table structure for table `vehiculos`
--

CREATE TABLE `vehiculos` (
  `idcoches` int NOT NULL,
  `marca` varchar(45) DEFAULT NULL,
  `modelo` varchar(45) DEFAULT NULL,
  `matricula` varchar(10) DEFAULT NULL,
  `tipoVehiculo` int NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;

--
-- Indexes for dumped tables
--

--
-- Indexes for table `espana`
--
ALTER TABLE `espana`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `vehiculos`
--
ALTER TABLE `vehiculos`
  ADD PRIMARY KEY (`idcoches`),
  ADD KEY `fk_vehiculos_espana_idx` (`tipoVehiculo`);

--
-- Constraints for dumped tables
--

--
-- Constraints for table `vehiculos`
--
ALTER TABLE `vehiculos`
  ADD CONSTRAINT `fk_vehiculos_espana` FOREIGN KEY (`tipoVehiculo`) REFERENCES `espana` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
=======

CREATE SCHEMA `sacarinosDB` DEFAULT CHARACTER SET utf8 ;
USE `sacarinosDB` ;

CREATE TABLE `sacarinosDB`.`espana` (
  `id` INT NOT NULL,
  `tipoVehiculo` VARCHAR(45) NULL,
  `cantidad` INT NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;



CREATE TABLE `sacarinosDB`.`vehiculos` (
  `idcoches` INT NOT NULL,
  `marca` VARCHAR(45) NULL,
  `modelo` VARCHAR(45) NULL,
  `matricula` VARCHAR(10) NULL,
  `tipoVehiculo` INT NOT NULL,
  PRIMARY KEY (`idcoches`),
  INDEX `fk_vehiculos_espana_idx` (`tipoVehiculo` ASC),
  CONSTRAINT `fk_vehiculos_espana`
    FOREIGN KEY (`tipoVehiculo`)
    REFERENCES `sacarinosDB`.`espana` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


>>>>>>> 94896ae4168559b12d02fee5b50a857d476f892d

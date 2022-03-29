-- phpMyAdmin SQL Dump
-- version 4.9.5deb2
-- https://www.phpmyadmin.net/
--
-- Servidor: localhost:3306
-- Tiempo de generación: 29-03-2022 a las 13:23:19
-- Versión del servidor: 8.0.28-0ubuntu0.20.04.3
-- Versión de PHP: 7.4.3

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `sacarinosDB`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `tiposVehiculos`
--

CREATE TABLE `tiposVehiculos` (
  `id` int NOT NULL,
  `tipoVehiculo` varchar(45) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;

--
-- Volcado de datos para la tabla `tiposVehiculos`
--

INSERT INTO `tiposVehiculos` (`id`, `tipoVehiculo`) VALUES
(1, 'TURISMOS'),
(2, 'CAMIONES'),
(3, 'CICLOMOTORES'),
(4, 'MOTOCICLETAS'),
(5, 'CABEZAS TRACTORAS'),
(6, 'REMOLQUES Y SEMIRREMOLQUES'),
(7, 'AUTOBUSES'),
(9, 'TRACTORES AGRICOLAS');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `vehiculos`
--

CREATE TABLE `vehiculos` (
  `idcoches` int NOT NULL,
  `marca` varchar(45) DEFAULT NULL,
  `modelo` varchar(45) DEFAULT NULL,
  `matricula` varchar(10) DEFAULT NULL,
  `tipoVehiculo` int NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;

--
-- Volcado de datos para la tabla `vehiculos`
--

INSERT INTO `vehiculos` (`idcoches`, `marca`, `modelo`, `matricula`, `tipoVehiculo`) VALUES
(1, 'TESLA', 'X', '1215JNM', 2),
(5, 'NISSAN', 'ALMERA', 'M3624UZ', 1),
(6, 'AUDI', 'A1', '1461JBZ', 1);

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `tiposVehiculos`
--
ALTER TABLE `tiposVehiculos`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `vehiculos`
--
ALTER TABLE `vehiculos`
  ADD PRIMARY KEY (`idcoches`),
  ADD KEY `fk_vehiculos_espana_idx` (`tipoVehiculo`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `vehiculos`
--
ALTER TABLE `vehiculos`
  MODIFY `idcoches` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- Restricciones para tablas volcadas
--

--
-- Filtros para la tabla `vehiculos`
--
ALTER TABLE `vehiculos`
  ADD CONSTRAINT `fk_vehiculos_espana` FOREIGN KEY (`tipoVehiculo`) REFERENCES `tiposVehiculos` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;

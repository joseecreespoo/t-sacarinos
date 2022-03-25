
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



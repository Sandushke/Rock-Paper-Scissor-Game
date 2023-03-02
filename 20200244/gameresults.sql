-- phpMyAdmin SQL Dump
-- version 5.0.4
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Apr 21, 2021 at 03:27 PM
-- Server version: 10.4.17-MariaDB
-- PHP Version: 8.0.2

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `gamedata`
--

-- --------------------------------------------------------

--
-- Table structure for table `gameresults`
--

CREATE TABLE `gameresults` (
  `Username` varchar(10) DEFAULT NULL,
  `Computer_wins` int(3) DEFAULT NULL,
  `User_wins` int(3) DEFAULT NULL,
  `Ties` int(3) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `gameresults`
--

INSERT INTO `gameresults` (`Username`, `Computer_wins`, `User_wins`, `Ties`) VALUES
('sandushke', 0, 2, 1),
('Nathan', 1, 0, 2),
('Imaya', 2, 1, 0),
('Hirushke', 2, 0, 0),
('Chryshall', 2, 1, 1),
('Shaveen', 0, 1, 1),
('kumuditha', 1, 2, 0),
('Shiran', 1, 1, 1),
('Nilesh', 1, 1, 1),
('Nilesh', 2, 0, 1);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;

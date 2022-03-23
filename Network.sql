-- phpMyAdmin SQL Dump
-- version 5.1.3
-- https://www.phpmyadmin.net/
--
-- Host: localhost
-- Generation Time: Mar 23, 2022 at 03:18 PM
-- Server version: 10.4.21-MariaDB
-- PHP Version: 7.4.28

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `Network`
--

-- --------------------------------------------------------

--
-- Table structure for table `post`
--

CREATE TABLE `post` (
  `postId` int(5) NOT NULL,
  `userId` int(4) NOT NULL,
  `content` varchar(60) NOT NULL,
  `datePost` date NOT NULL,
  `status` char(1) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `post`
--

INSERT INTO `post` (`postId`, `userId`, `content`, `datePost`, `status`) VALUES
(17, 7, 'hello world', '2022-03-22', 'p'),
(19, 7, 'hellsdfsdf', '2022-03-22', 'p'),
(51, 7, 'hello world', '2022-03-23', 'p'),
(60, 14, 'Hello', '2022-03-23', 'w'),
(61, 14, 'Hello World', '2022-03-23', 'w'),
(62, 14, 'Hello World', '2022-03-23', 'w'),
(63, 14, 'Hello', '2022-03-23', 'w'),
(64, 14, 'Hello', '2022-03-23', 'w'),
(65, 14, 'Hello', '2022-03-23', 'w'),
(66, 14, 'Hellos', '2022-03-23', 'w'),
(67, 14, 'sdfs', '2022-03-23', 'w'),
(69, 14, 'sfdsdf', '2022-03-23', 'w'),
(71, 14, 'Hello', '2022-03-23', 'p'),
(72, 16, 'ตื่นมาก็หล่อนอนต่อดีกว่า', '2022-03-23', 'p');

-- --------------------------------------------------------

--
-- Table structure for table `user`
--

CREATE TABLE `user` (
  `userId` int(4) NOT NULL,
  `userName` varchar(60) NOT NULL,
  `password` varchar(60) NOT NULL,
  `e_mail` varchar(60) NOT NULL,
  `type_user` char(1) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `user`
--

INSERT INTO `user` (`userId`, `userName`, `password`, `e_mail`, `type_user`) VALUES
(1, 'sfdsdf', 'sfds', 'asdfs', 'u'),
(2, 'sdfsd', '12312', 'nadsfsf', 'u'),
(7, 'del', 'p1234', 'natthanan.pha2001@gmail.com', 'a'),
(14, 'deldy', 'p1234', 'natthanan.pha2001@gmail.com', 'u'),
(15, 'GG', 'p1234', 'Natthanan@gmail.com', 'u'),
(16, 'User', 'p1234', 'natthanan@gmail.com', 'u');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `post`
--
ALTER TABLE `post`
  ADD PRIMARY KEY (`postId`),
  ADD KEY `userId_fk` (`userId`);

--
-- Indexes for table `user`
--
ALTER TABLE `user`
  ADD PRIMARY KEY (`userId`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `post`
--
ALTER TABLE `post`
  MODIFY `postId` int(5) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=73;

--
-- AUTO_INCREMENT for table `user`
--
ALTER TABLE `user`
  MODIFY `userId` int(4) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=17;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `post`
--
ALTER TABLE `post`
  ADD CONSTRAINT `userId_fk` FOREIGN KEY (`userId`) REFERENCES `user` (`userId`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;

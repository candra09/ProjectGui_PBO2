-- phpMyAdmin SQL Dump
-- version 4.8.2
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Waktu pembuatan: 06 Jun 2021 pada 20.20
-- Versi server: 10.1.34-MariaDB
-- Versi PHP: 7.0.31

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `pilotdb`
--

-- --------------------------------------------------------

--
-- Struktur dari tabel `account`
--

CREATE TABLE `account` (
  `id_acc` int(11) NOT NULL,
  `username` varchar(255) NOT NULL,
  `pwd` varchar(8) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data untuk tabel `account`
--

INSERT INTO `account` (`id_acc`, `username`, `pwd`) VALUES
(1, 'Admin', '1234');

-- --------------------------------------------------------

--
-- Struktur dari tabel `detailnilai`
--

CREATE TABLE `detailnilai` (
  `id` int(11) NOT NULL,
  `NoInduk` int(11) NOT NULL,
  `NilaiTugas` float NOT NULL,
  `NilaiUTS` float NOT NULL,
  `NilaiUAS` float NOT NULL,
  `NilaiAkhir` float NOT NULL,
  `Mutu` text NOT NULL,
  `Status` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data untuk tabel `detailnilai`
--

INSERT INTO `detailnilai` (`id`, `NoInduk`, `NilaiTugas`, `NilaiUTS`, `NilaiUAS`, `NilaiAkhir`, `Mutu`, `Status`) VALUES
(13, 3001, 60, 60, 60, 60, 'C', 'Naik Kelas'),
(14, 3002, 80, 70, 80, 76.5, 'B', 'Naik Kelas'),
(15, 3003, 90, 90, 90, 90, 'A', 'Naik Kelas'),
(16, 3004, 90, 80, 100, 93, 'A', 'Naik Kelas'),
(17, 3005, 50, 50, 50, 50, 'D', 'Tidak Naik Kelas'),
(18, 3006, 75, 88, 79, 82.15, 'A', 'Naik Kelas'),
(19, 3007, 100, 90, 85, 86.75, 'A', 'Naik Kelas'),
(20, 3008, 100, 100, 100, 100, 'A', 'Naik Kelas'),
(21, 3009, 75, 89, 90, 89.65, 'A', 'Naik Kelas'),
(22, 3010, 78, 75, 87, 82.8, 'A', 'Naik Kelas');

-- --------------------------------------------------------

--
-- Struktur dari tabel `siswa`
--

CREATE TABLE `siswa` (
  `NoInduk` int(11) NOT NULL,
  `NamaLengkap` varchar(255) NOT NULL,
  `Jk` varchar(255) NOT NULL,
  `Kelas` varchar(255) NOT NULL,
  `alamat` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data untuk tabel `siswa`
--

INSERT INTO `siswa` (`NoInduk`, `NamaLengkap`, `Jk`, `Kelas`, `alamat`) VALUES
(3001, 'Fatih Ramdhan', 'L', 'XI IPA 2 ', 'Jl Melati'),
(3002, 'Nara Nur F', 'P', 'XI IPA 2', 'Jl Mawar'),
(3003, 'Rahma Fitria', 'P', 'XI IPA 2', 'Jl Brawijaya'),
(3004, 'M. Rahmat', 'L', 'XI IPA 2', 'Sekoto'),
(3005, 'Raihan Rama', 'L', 'XI IPA 2', 'Jl Sakura'),
(3006, 'Miskah', 'P', 'XI IPA 2', 'Jl Flamboyan'),
(3007, 'Ahmad Haikal ', 'L', 'XI IPA 2', 'Jl Pepaya'),
(3008, 'Moh Kazuma', 'L', 'XI IPA 2', 'Jl Manggar'),
(3009, 'Qian Azura', 'L', 'XI IPA 2', 'Jl Sri Rejeki'),
(3010, 'Lalania Aqua', 'P', 'XI IPA 2', 'Jl Dahlia');

--
-- Indexes for dumped tables
--

--
-- Indeks untuk tabel `account`
--
ALTER TABLE `account`
  ADD PRIMARY KEY (`id_acc`);

--
-- Indeks untuk tabel `detailnilai`
--
ALTER TABLE `detailnilai`
  ADD PRIMARY KEY (`id`),
  ADD KEY `int` (`NoInduk`);

--
-- Indeks untuk tabel `siswa`
--
ALTER TABLE `siswa`
  ADD PRIMARY KEY (`NoInduk`);

--
-- AUTO_INCREMENT untuk tabel yang dibuang
--

--
-- AUTO_INCREMENT untuk tabel `account`
--
ALTER TABLE `account`
  MODIFY `id_acc` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT untuk tabel `detailnilai`
--
ALTER TABLE `detailnilai`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=28;

--
-- AUTO_INCREMENT untuk tabel `siswa`
--
ALTER TABLE `siswa`
  MODIFY `NoInduk` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4010;

--
-- Ketidakleluasaan untuk tabel pelimpahan (Dumped Tables)
--

--
-- Ketidakleluasaan untuk tabel `detailnilai`
--
ALTER TABLE `detailnilai`
  ADD CONSTRAINT `int` FOREIGN KEY (`NoInduk`) REFERENCES `siswa` (`NoInduk`) ON DELETE CASCADE ON UPDATE CASCADE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;

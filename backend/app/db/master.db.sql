BEGIN TRANSACTION;
CREATE TABLE IF NOT EXISTS "ttipe" (
	"tipeid"	INTEGER,
	"tipe"	TEXT,
	PRIMARY KEY("tipeid" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "tusers" (
	"userid"	INTEGER,
	"fullname"	TEXT,
	"email"	TEXT,
	"pwd"	TEXT,
	"tipe"	TEXT,
	PRIMARY KEY("userid" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "tcustomer" (
	"customerid"	INTEGER,
	"fullname"	TEXT,
	"email"	TEXT,
	"alamat"	TEXT,
	"notelp"	TEXT,
	PRIMARY KEY("customerid" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "tcartdesc" (
	"cartdescid"	INTEGER,
	"cartid"	INTEGER,
	"barangid"	INTEGER,
	"jumlah"	INTEGER,
	"total"	INTEGER,
	PRIMARY KEY("cartdescid" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "ttrx" (
	"trxid"	INTEGER,
	"tanggal"	TEXT,
	"status"	TEXT,
	"cartid"	INTEGER,
	"jenisbayar"	TEXT,
	PRIMARY KEY("trxid" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "tcart" (
	"cartid"	INTEGER,
	"customerid"	INTEGER,
	"tanggal"	TEXT,
	"telahdibayar"	TEXT,
	"jenisbayar"	TEXT,
	PRIMARY KEY("cartid" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "tbarang" (
	"barangid"	INTEGER,
	"nama"	TEXT,
	"satuan"	TEXT,
	"jumlah"	INTEGER,
	"harga"	INTEGER,
	"tipeid"	INTEGER,
	"desc"	TEXT,
	"path"	TEXT,
	PRIMARY KEY("barangid" AUTOINCREMENT)
);
INSERT INTO "ttipe" VALUES (1,'Obat-obatan');
INSERT INTO "ttipe" VALUES (2,'Pupuk');
INSERT INTO "ttipe" VALUES (3,'Bibit');
INSERT INTO "ttipe" VALUES (11,'Alat Pertanian');
INSERT INTO "tusers" VALUES (2,'Fitri','fitri@gmail.com','fitri','administrasi');
INSERT INTO "tcustomer" VALUES (1,'Amiruddin','amir@gmail.com','Jl Sukosari 62','0812345');
INSERT INTO "tcustomer" VALUES (2,'Iwan Arid','iwan@gmail.com','Jl S Parman','0812345');
INSERT INTO "tcustomer" VALUES (3,'Teddy Sumbayak','teddy@gmail.com','Jl DI Panjaitan','0812345');
INSERT INTO "tcustomer" VALUES (4,'Rinto Harahap','rinto@gmail.com','Jl Merdeka','0812345');
INSERT INTO "tcustomer" VALUES (5,'Dewi Annggraini','dewi@gmail.com','Jl Asahan','0812345');
INSERT INTO "tcustomer" VALUES (6,'Andi',NULL,'Jl Sonata','0812345');
INSERT INTO "tcustomer" VALUES (7,'Tony',NULL,'Jl Luku','0812345');
INSERT INTO "tcustomer" VALUES (8,'Marchel',NULL,'Jl Bunga Rinte','0812345');
INSERT INTO "tcustomer" VALUES (13,'cecec','cecece',NULL,'undefined');
INSERT INTO "tcustomer" VALUES (14,'cedce','cece',NULL,'undefined');
INSERT INTO "tcustomer" VALUES (15,'gvebve','veveev',NULL,'undefined');
INSERT INTO "tcustomer" VALUES (16,'gvebve','veveev',NULL,'undefined');
INSERT INTO "tcustomer" VALUES (17,'bttbt','btbtbt',NULL,'undefined');
INSERT INTO "tcustomer" VALUES (18,'veve','vevev',NULL,'veveve');
INSERT INTO "tcustomer" VALUES (19,'test','tesst',NULL,'test');
INSERT INTO "tcustomer" VALUES (20,'test','tesst',NULL,'test');
INSERT INTO "tcustomer" VALUES (21,'vev','veve',NULL,'veve');
INSERT INTO "tcustomer" VALUES (22,'ve','ve',NULL,'ve');
INSERT INTO "tcustomer" VALUES (23,'bvr','bdfb',NULL,'bfbf');
INSERT INTO "tcustomer" VALUES (24,'bvr','br',NULL,'br');
INSERT INTO "tcustomer" VALUES (25,'br','br',NULL,'br');
INSERT INTO "tcustomer" VALUES (26,'vceve','silalahitotok@gmail.com',NULL,'cecece');
INSERT INTO "tcustomer" VALUES (27,'br','br',NULL,'br');
INSERT INTO "tcustomer" VALUES (28,'br','br',NULL,'br');
INSERT INTO "tcustomer" VALUES (29,'veve','veve',NULL,'veveve');
INSERT INTO "tcartdesc" VALUES (1,4,1,2,2000);
INSERT INTO "tcartdesc" VALUES (2,4,2,5,25000);
INSERT INTO "tcartdesc" VALUES (3,4,3,2,2000);
INSERT INTO "tcartdesc" VALUES (4,5,1,3,3000);
INSERT INTO "tcartdesc" VALUES (5,5,2,3,15000);
INSERT INTO "tcartdesc" VALUES (6,24,1,1,1500);
INSERT INTO "tcartdesc" VALUES (7,24,2,1,5000);
INSERT INTO "tcartdesc" VALUES (8,24,4,1,2500);
INSERT INTO "tcartdesc" VALUES (9,25,1,2,3000);
INSERT INTO "tcartdesc" VALUES (10,25,2,2,10000);
INSERT INTO "tcart" VALUES (4,8,'2022-11-24','y','Transfer');
INSERT INTO "tcart" VALUES (5,8,'2022-11-23',NULL,NULL);
INSERT INTO "tcart" VALUES (9,13,'2022-11-26',NULL,NULL);
INSERT INTO "tcart" VALUES (10,14,'2022-11-26',NULL,NULL);
INSERT INTO "tcart" VALUES (11,15,'2022-11-26',NULL,NULL);
INSERT INTO "tcart" VALUES (12,16,'2022-11-26',NULL,NULL);
INSERT INTO "tcart" VALUES (13,17,'2022-11-26',NULL,NULL);
INSERT INTO "tcart" VALUES (14,18,'2022-11-26',NULL,NULL);
INSERT INTO "tcart" VALUES (24,28,'2022-11-27','y','Transfer');
INSERT INTO "tcart" VALUES (25,29,'2022-11-27','y','Transfer');
INSERT INTO "tbarang" VALUES (1,'NPK','Kg',297,1500,2,'Cras sit amet nibh libero, in gravida nulla. Nulla vel metus scelerisque ante sollicitudin commodo. Cras purus odio, vestibulum in vulputate at, tempus viverra turpis.','static/images/barang/000001.png');
INSERT INTO "tbarang" VALUES (2,'NaCl','bungkus',597,5000,2,'Crus sit amet nibh libero, in gravida nulla. Nulla vel metus scelerisque ante sollicitudin commodo. Cras purus odio, vestibulum in vulputate at, tempus viverra turpis.','static/images/barang/000002.png');
INSERT INTO "tbarang" VALUES (4,'KCL','Kg',549,2500,2,'Cres sit amet nibh libero, in gravida nulla. Nulla vel metus scelerisque ante sollicitudin commodo. Cras purus odio, vestibulum in vulputate at, tempus viverra turpis.','static/images/barang/00003.jpg');
INSERT INTO "tbarang" VALUES (6,'Bibit Mangga','Bungkus',200,1500,3,'Cras sit amet nibh libero, in gravida nulla. Nulla vel metus scelerisque ante sollicitudin commodo. Cras purus odio, vestibulum in vulputate at, tempus viverra turpis.','static/images/barang/04.jpg');
INSERT INTO "tbarang" VALUES (7,'NPK Phonska','Kg',200,5000,2,'Cras sit amet nibh libero, in gravida nulla. Nulla vel metus scelerisque ante sollicitudin commodo. Cras purus odio, vestibulum in vulputate at, tempus viverra turpis.','static/images/barang/04.jpg');
INSERT INTO "tbarang" VALUES (8,'Dolomit Gresik','Kg',400,2000,2,'Cras sit amet nibh libero, in gravida nulla. Nulla vel metus scelerisque ante sollicitudin commodo. Cras purus odio, vestibulum in vulputate at, tempus viverra turpis.','static/images/barang/01.jpg');
INSERT INTO "tbarang" VALUES (9,'ZA Gresik','Kg',400,10000,2,'Pupuk ZA buatan PT Petrokimia Gresik','static/images/barang/za.jpg');
COMMIT;

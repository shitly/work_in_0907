drop database ip4;
create database ip4 DEFAULT CHARACTER SET gbk COLLATE gbk_chinese_ci;
use ip4;

CREATE TABLE IF NOT EXISTS `ips`(
   `id` bigint(20) unsigned NOT NULL auto_increment,
   `start_ip` VARCHAR(100),
   `end_ip` VARCHAR(100),
   `location` VARCHAR(100),
   PRIMARY KEY  (`id`)
);

LOAD DATA LOCAL INFILE 'gaim.txt' INTO TABLE ips character set gbk
FIELDS TERMINATED BY ','
enclosed by ""
LINES TERMINATED BY '\n' (`start_ip`,`end_ip`,`location`);

DROP TABLE `users`;

CREATE TABLE `users` (
  `id` mediumint(8) unsigned NOT NULL auto_increment,
  `user` varchar(255) default NULL,
  `password` TEXT default NULL,
  `display_name` varchar(255) default NULL,
  `rights` TEXT default NULL,
  `enabled` TEXT default NULL,
  PRIMARY KEY (`id`)
) AUTO_INCREMENT=1;

INSERT INTO `users` (`user`,`password`,`display_name`,`rights`) VALUES ("test","627f52351be680bc19f06d52bba92b3d","TTTTESSSTTT","ADMIN,","false");
INSERT INTO `users` (`user`,`password`,`display_name`,`rights`) VALUES ("yonathan","cc03e747a6afbbcbf8be7668acfebee5","Yonathan Klijnsma","ADMIN,","true");
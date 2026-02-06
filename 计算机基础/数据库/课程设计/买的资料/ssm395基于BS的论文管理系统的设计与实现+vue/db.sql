/*
SQLyog Ultimate v11.3 (64 bit)
MySQL - 5.7.32-log : Database - ssmwx41b
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
CREATE DATABASE /*!32312 IF NOT EXISTS*/`ssmwx41b` /*!40100 DEFAULT CHARACTER SET utf8 */;

USE `ssmwx41b`;

/*Table structure for table `config` */

DROP TABLE IF EXISTS `config`;

CREATE TABLE `config` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT COMMENT '主键',
  `name` varchar(100) NOT NULL COMMENT '配置参数名称',
  `value` varchar(100) DEFAULT NULL COMMENT '配置参数值',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8 COMMENT='配置文件';

/*Data for the table `config` */

insert  into `config`(`id`,`name`,`value`) values (1,'picture1','http://localhost:8080/ssmwx41b/upload/picture1.jpg');
insert  into `config`(`id`,`name`,`value`) values (2,'picture2','http://localhost:8080/ssmwx41b/upload/picture2.jpg');
insert  into `config`(`id`,`name`,`value`) values (3,'picture3','http://localhost:8080/ssmwx41b/upload/picture3.jpg');
insert  into `config`(`id`,`name`,`value`) values (6,'homepage',NULL);

/*Table structure for table `gonggaoxinxi` */

DROP TABLE IF EXISTS `gonggaoxinxi`;

CREATE TABLE `gonggaoxinxi` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT COMMENT '主键',
  `addtime` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
  `biaoti` varchar(200) DEFAULT NULL COMMENT '标题',
  `neirong` longtext COMMENT '内容',
  `fabushijian` datetime DEFAULT NULL COMMENT '发布时间',
  `tupian` varchar(200) DEFAULT NULL COMMENT '图片',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=67 DEFAULT CHARSET=utf8 COMMENT='公告信息';

/*Data for the table `gonggaoxinxi` */

insert  into `gonggaoxinxi`(`id`,`addtime`,`biaoti`,`neirong`,`fabushijian`,`tupian`) values (61,'2021-05-15 14:45:08','标题1','内容1','2021-05-15 14:45:08','http://localhost:8080/ssmwx41b/upload/gonggaoxinxi_tupian1.jpg');
insert  into `gonggaoxinxi`(`id`,`addtime`,`biaoti`,`neirong`,`fabushijian`,`tupian`) values (62,'2021-05-15 14:45:08','标题2','内容2','2021-05-15 14:45:08','http://localhost:8080/ssmwx41b/upload/gonggaoxinxi_tupian2.jpg');
insert  into `gonggaoxinxi`(`id`,`addtime`,`biaoti`,`neirong`,`fabushijian`,`tupian`) values (63,'2021-05-15 14:45:08','标题3','内容3','2021-05-15 14:45:08','http://localhost:8080/ssmwx41b/upload/gonggaoxinxi_tupian3.jpg');
insert  into `gonggaoxinxi`(`id`,`addtime`,`biaoti`,`neirong`,`fabushijian`,`tupian`) values (64,'2021-05-15 14:45:08','标题4','内容4','2021-05-15 14:45:08','http://localhost:8080/ssmwx41b/upload/gonggaoxinxi_tupian4.jpg');
insert  into `gonggaoxinxi`(`id`,`addtime`,`biaoti`,`neirong`,`fabushijian`,`tupian`) values (65,'2021-05-15 14:45:08','标题5','内容5','2021-05-15 14:45:08','http://localhost:8080/ssmwx41b/upload/gonggaoxinxi_tupian5.jpg');
insert  into `gonggaoxinxi`(`id`,`addtime`,`biaoti`,`neirong`,`fabushijian`,`tupian`) values (66,'2021-05-15 14:45:08','标题6','内容6','2021-05-15 14:45:08','http://localhost:8080/ssmwx41b/upload/gonggaoxinxi_tupian6.jpg');

/*Table structure for table `jiaoshi` */

DROP TABLE IF EXISTS `jiaoshi`;

CREATE TABLE `jiaoshi` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT COMMENT '主键',
  `addtime` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
  `jiaoshizhanghao` varchar(200) DEFAULT NULL COMMENT '教师账号',
  `mima` varchar(200) DEFAULT NULL COMMENT '密码',
  `jiaoshixingming` varchar(200) DEFAULT NULL COMMENT '教师姓名',
  `xingbie` varchar(200) DEFAULT NULL COMMENT '性别',
  `dianhua` varchar(200) DEFAULT NULL COMMENT '电话',
  `shenfenzheng` varchar(200) DEFAULT NULL COMMENT '身份证',
  `youxiang` varchar(200) DEFAULT NULL COMMENT '邮箱',
  `touxiang` varchar(200) DEFAULT NULL COMMENT '头像',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=27 DEFAULT CHARSET=utf8 COMMENT='教师';

/*Data for the table `jiaoshi` */

insert  into `jiaoshi`(`id`,`addtime`,`jiaoshizhanghao`,`mima`,`jiaoshixingming`,`xingbie`,`dianhua`,`shenfenzheng`,`youxiang`,`touxiang`) values (21,'2021-05-15 14:45:08','教师1','123456','教师姓名1','男','13823888881','440300199101010001','773890001@qq.com','http://localhost:8080/ssmwx41b/upload/jiaoshi_touxiang1.jpg');
insert  into `jiaoshi`(`id`,`addtime`,`jiaoshizhanghao`,`mima`,`jiaoshixingming`,`xingbie`,`dianhua`,`shenfenzheng`,`youxiang`,`touxiang`) values (22,'2021-05-15 14:45:08','教师2','123456','教师姓名2','男','13823888882','440300199202020002','773890002@qq.com','http://localhost:8080/ssmwx41b/upload/jiaoshi_touxiang2.jpg');
insert  into `jiaoshi`(`id`,`addtime`,`jiaoshizhanghao`,`mima`,`jiaoshixingming`,`xingbie`,`dianhua`,`shenfenzheng`,`youxiang`,`touxiang`) values (23,'2021-05-15 14:45:08','教师3','123456','教师姓名3','男','13823888883','440300199303030003','773890003@qq.com','http://localhost:8080/ssmwx41b/upload/jiaoshi_touxiang3.jpg');
insert  into `jiaoshi`(`id`,`addtime`,`jiaoshizhanghao`,`mima`,`jiaoshixingming`,`xingbie`,`dianhua`,`shenfenzheng`,`youxiang`,`touxiang`) values (24,'2021-05-15 14:45:08','教师4','123456','教师姓名4','男','13823888884','440300199404040004','773890004@qq.com','http://localhost:8080/ssmwx41b/upload/jiaoshi_touxiang4.jpg');
insert  into `jiaoshi`(`id`,`addtime`,`jiaoshizhanghao`,`mima`,`jiaoshixingming`,`xingbie`,`dianhua`,`shenfenzheng`,`youxiang`,`touxiang`) values (25,'2021-05-15 14:45:08','教师5','123456','教师姓名5','男','13823888885','440300199505050005','773890005@qq.com','http://localhost:8080/ssmwx41b/upload/jiaoshi_touxiang5.jpg');
insert  into `jiaoshi`(`id`,`addtime`,`jiaoshizhanghao`,`mima`,`jiaoshixingming`,`xingbie`,`dianhua`,`shenfenzheng`,`youxiang`,`touxiang`) values (26,'2021-05-15 14:45:08','教师6','123456','教师姓名6','男','13823888886','440300199606060006','773890006@qq.com','http://localhost:8080/ssmwx41b/upload/jiaoshi_touxiang6.jpg');

/*Table structure for table `ketiguanli` */

DROP TABLE IF EXISTS `ketiguanli`;

CREATE TABLE `ketiguanli` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT COMMENT '主键',
  `addtime` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
  `jiaoshizhanghao` varchar(200) DEFAULT NULL COMMENT '教师账号',
  `jiaoshixingming` varchar(200) DEFAULT NULL COMMENT '教师姓名',
  `dianhua` varchar(200) DEFAULT NULL COMMENT '电话',
  `ketimingcheng` varchar(200) DEFAULT NULL COMMENT '课题名称',
  `ketijianjie` longtext COMMENT '课题简介',
  `ketiwenjian` varchar(200) DEFAULT NULL COMMENT '课题文件',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=37 DEFAULT CHARSET=utf8 COMMENT='课题管理';

/*Data for the table `ketiguanli` */

insert  into `ketiguanli`(`id`,`addtime`,`jiaoshizhanghao`,`jiaoshixingming`,`dianhua`,`ketimingcheng`,`ketijianjie`,`ketiwenjian`) values (31,'2021-05-15 14:45:08','教师账号1','教师姓名1','电话1','课题名称1','课题简介1','');
insert  into `ketiguanli`(`id`,`addtime`,`jiaoshizhanghao`,`jiaoshixingming`,`dianhua`,`ketimingcheng`,`ketijianjie`,`ketiwenjian`) values (32,'2021-05-15 14:45:08','教师账号2','教师姓名2','电话2','课题名称2','课题简介2','');
insert  into `ketiguanli`(`id`,`addtime`,`jiaoshizhanghao`,`jiaoshixingming`,`dianhua`,`ketimingcheng`,`ketijianjie`,`ketiwenjian`) values (33,'2021-05-15 14:45:08','教师账号3','教师姓名3','电话3','课题名称3','课题简介3','');
insert  into `ketiguanli`(`id`,`addtime`,`jiaoshizhanghao`,`jiaoshixingming`,`dianhua`,`ketimingcheng`,`ketijianjie`,`ketiwenjian`) values (34,'2021-05-15 14:45:08','教师账号4','教师姓名4','电话4','课题名称4','课题简介4','');
insert  into `ketiguanli`(`id`,`addtime`,`jiaoshizhanghao`,`jiaoshixingming`,`dianhua`,`ketimingcheng`,`ketijianjie`,`ketiwenjian`) values (35,'2021-05-15 14:45:08','教师账号5','教师姓名5','电话5','课题名称5','课题简介5','');
insert  into `ketiguanli`(`id`,`addtime`,`jiaoshizhanghao`,`jiaoshixingming`,`dianhua`,`ketimingcheng`,`ketijianjie`,`ketiwenjian`) values (36,'2021-05-15 14:45:08','教师账号6','教师姓名6','电话6','课题名称6','课题简介6','');

/*Table structure for table `ketixuanze` */

DROP TABLE IF EXISTS `ketixuanze`;

CREATE TABLE `ketixuanze` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT COMMENT '主键',
  `addtime` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
  `jiaoshizhanghao` varchar(200) DEFAULT NULL COMMENT '教师账号',
  `jiaoshixingming` varchar(200) DEFAULT NULL COMMENT '教师姓名',
  `dianhua` varchar(200) DEFAULT NULL COMMENT '电话',
  `ketimingcheng` varchar(200) DEFAULT NULL COMMENT '课题名称',
  `ketijianjie` varchar(200) DEFAULT NULL COMMENT '课题简介',
  `ketiwenjian` varchar(200) DEFAULT NULL COMMENT '课题文件',
  `zhanghao` varchar(200) DEFAULT NULL COMMENT '账号',
  `xingming` varchar(200) DEFAULT NULL COMMENT '姓名',
  `banji` varchar(200) DEFAULT NULL COMMENT '班级',
  `zhuanye` varchar(200) DEFAULT NULL COMMENT '专业',
  `shijian` datetime DEFAULT NULL COMMENT '时间',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=47 DEFAULT CHARSET=utf8 COMMENT='课题选择';

/*Data for the table `ketixuanze` */

insert  into `ketixuanze`(`id`,`addtime`,`jiaoshizhanghao`,`jiaoshixingming`,`dianhua`,`ketimingcheng`,`ketijianjie`,`ketiwenjian`,`zhanghao`,`xingming`,`banji`,`zhuanye`,`shijian`) values (41,'2021-05-15 14:45:08','教师账号1','教师姓名1','电话1','课题名称1','课题简介1','课题文件1','账号1','姓名1','班级1','专业1','2021-05-15 14:45:08');
insert  into `ketixuanze`(`id`,`addtime`,`jiaoshizhanghao`,`jiaoshixingming`,`dianhua`,`ketimingcheng`,`ketijianjie`,`ketiwenjian`,`zhanghao`,`xingming`,`banji`,`zhuanye`,`shijian`) values (42,'2021-05-15 14:45:08','教师账号2','教师姓名2','电话2','课题名称2','课题简介2','课题文件2','账号2','姓名2','班级2','专业2','2021-05-15 14:45:08');
insert  into `ketixuanze`(`id`,`addtime`,`jiaoshizhanghao`,`jiaoshixingming`,`dianhua`,`ketimingcheng`,`ketijianjie`,`ketiwenjian`,`zhanghao`,`xingming`,`banji`,`zhuanye`,`shijian`) values (43,'2021-05-15 14:45:08','教师账号3','教师姓名3','电话3','课题名称3','课题简介3','课题文件3','账号3','姓名3','班级3','专业3','2021-05-15 14:45:08');
insert  into `ketixuanze`(`id`,`addtime`,`jiaoshizhanghao`,`jiaoshixingming`,`dianhua`,`ketimingcheng`,`ketijianjie`,`ketiwenjian`,`zhanghao`,`xingming`,`banji`,`zhuanye`,`shijian`) values (44,'2021-05-15 14:45:08','教师账号4','教师姓名4','电话4','课题名称4','课题简介4','课题文件4','账号4','姓名4','班级4','专业4','2021-05-15 14:45:08');
insert  into `ketixuanze`(`id`,`addtime`,`jiaoshizhanghao`,`jiaoshixingming`,`dianhua`,`ketimingcheng`,`ketijianjie`,`ketiwenjian`,`zhanghao`,`xingming`,`banji`,`zhuanye`,`shijian`) values (45,'2021-05-15 14:45:08','教师账号5','教师姓名5','电话5','课题名称5','课题简介5','课题文件5','账号5','姓名5','班级5','专业5','2021-05-15 14:45:08');
insert  into `ketixuanze`(`id`,`addtime`,`jiaoshizhanghao`,`jiaoshixingming`,`dianhua`,`ketimingcheng`,`ketijianjie`,`ketiwenjian`,`zhanghao`,`xingming`,`banji`,`zhuanye`,`shijian`) values (46,'2021-05-15 14:45:08','教师账号6','教师姓名6','电话6','课题名称6','课题简介6','课题文件6','账号6','姓名6','班级6','专业6','2021-05-15 14:45:08');

/*Table structure for table `lunwenguanli` */

DROP TABLE IF EXISTS `lunwenguanli`;

CREATE TABLE `lunwenguanli` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT COMMENT '主键',
  `addtime` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
  `jiaoshizhanghao` varchar(200) DEFAULT NULL COMMENT '教师账号',
  `jiaoshixingming` varchar(200) DEFAULT NULL COMMENT '教师姓名',
  `dianhua` varchar(200) DEFAULT NULL COMMENT '电话',
  `ketimingcheng` varchar(200) DEFAULT NULL COMMENT '课题名称',
  `ketijianjie` varchar(200) DEFAULT NULL COMMENT '课题简介',
  `ketiwenjian` varchar(200) DEFAULT NULL COMMENT '课题文件',
  `zhanghao` varchar(200) DEFAULT NULL COMMENT '账号',
  `xingming` varchar(200) DEFAULT NULL COMMENT '姓名',
  `banji` varchar(200) DEFAULT NULL COMMENT '班级',
  `zhuanye` varchar(200) DEFAULT NULL COMMENT '专业',
  `lunwenmingcheng` varchar(200) DEFAULT NULL COMMENT '论文名称',
  `lunwenshangchuan` varchar(200) DEFAULT NULL COMMENT '论文上传',
  `shangchuanshijian` datetime DEFAULT NULL COMMENT '上传时间',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=57 DEFAULT CHARSET=utf8 COMMENT='论文管理';

/*Data for the table `lunwenguanli` */

insert  into `lunwenguanli`(`id`,`addtime`,`jiaoshizhanghao`,`jiaoshixingming`,`dianhua`,`ketimingcheng`,`ketijianjie`,`ketiwenjian`,`zhanghao`,`xingming`,`banji`,`zhuanye`,`lunwenmingcheng`,`lunwenshangchuan`,`shangchuanshijian`) values (51,'2021-05-15 14:45:08','教师账号1','教师姓名1','电话1','课题名称1','课题简介1','课题文件1','账号1','姓名1','班级1','专业1','论文名称1','','2021-05-15 14:45:08');
insert  into `lunwenguanli`(`id`,`addtime`,`jiaoshizhanghao`,`jiaoshixingming`,`dianhua`,`ketimingcheng`,`ketijianjie`,`ketiwenjian`,`zhanghao`,`xingming`,`banji`,`zhuanye`,`lunwenmingcheng`,`lunwenshangchuan`,`shangchuanshijian`) values (52,'2021-05-15 14:45:08','教师账号2','教师姓名2','电话2','课题名称2','课题简介2','课题文件2','账号2','姓名2','班级2','专业2','论文名称2','','2021-05-15 14:45:08');
insert  into `lunwenguanli`(`id`,`addtime`,`jiaoshizhanghao`,`jiaoshixingming`,`dianhua`,`ketimingcheng`,`ketijianjie`,`ketiwenjian`,`zhanghao`,`xingming`,`banji`,`zhuanye`,`lunwenmingcheng`,`lunwenshangchuan`,`shangchuanshijian`) values (53,'2021-05-15 14:45:08','教师账号3','教师姓名3','电话3','课题名称3','课题简介3','课题文件3','账号3','姓名3','班级3','专业3','论文名称3','','2021-05-15 14:45:08');
insert  into `lunwenguanli`(`id`,`addtime`,`jiaoshizhanghao`,`jiaoshixingming`,`dianhua`,`ketimingcheng`,`ketijianjie`,`ketiwenjian`,`zhanghao`,`xingming`,`banji`,`zhuanye`,`lunwenmingcheng`,`lunwenshangchuan`,`shangchuanshijian`) values (54,'2021-05-15 14:45:08','教师账号4','教师姓名4','电话4','课题名称4','课题简介4','课题文件4','账号4','姓名4','班级4','专业4','论文名称4','','2021-05-15 14:45:08');
insert  into `lunwenguanli`(`id`,`addtime`,`jiaoshizhanghao`,`jiaoshixingming`,`dianhua`,`ketimingcheng`,`ketijianjie`,`ketiwenjian`,`zhanghao`,`xingming`,`banji`,`zhuanye`,`lunwenmingcheng`,`lunwenshangchuan`,`shangchuanshijian`) values (55,'2021-05-15 14:45:08','教师账号5','教师姓名5','电话5','课题名称5','课题简介5','课题文件5','账号5','姓名5','班级5','专业5','论文名称5','','2021-05-15 14:45:08');
insert  into `lunwenguanli`(`id`,`addtime`,`jiaoshizhanghao`,`jiaoshixingming`,`dianhua`,`ketimingcheng`,`ketijianjie`,`ketiwenjian`,`zhanghao`,`xingming`,`banji`,`zhuanye`,`lunwenmingcheng`,`lunwenshangchuan`,`shangchuanshijian`) values (56,'2021-05-15 14:45:08','教师账号6','教师姓名6','电话6','课题名称6','课题简介6','课题文件6','账号6','姓名6','班级6','专业6','论文名称6','','2021-05-15 14:45:08');

/*Table structure for table `token` */

DROP TABLE IF EXISTS `token`;

CREATE TABLE `token` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT COMMENT '主键',
  `userid` bigint(20) NOT NULL COMMENT '用户id',
  `username` varchar(100) NOT NULL COMMENT '用户名',
  `tablename` varchar(100) DEFAULT NULL COMMENT '表名',
  `role` varchar(100) DEFAULT NULL COMMENT '角色',
  `token` varchar(200) NOT NULL COMMENT '密码',
  `addtime` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '新增时间',
  `expiratedtime` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '过期时间',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='token表';

/*Data for the table `token` */

/*Table structure for table `users` */

DROP TABLE IF EXISTS `users`;

CREATE TABLE `users` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT COMMENT '主键',
  `username` varchar(100) NOT NULL COMMENT '用户名',
  `password` varchar(100) NOT NULL COMMENT '密码',
  `role` varchar(100) DEFAULT '管理员' COMMENT '角色',
  `addtime` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '新增时间',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8 COMMENT='用户表';

/*Data for the table `users` */

insert  into `users`(`id`,`username`,`password`,`role`,`addtime`) values (1,'abo','abo','管理员','2021-05-15 14:45:08');

/*Table structure for table `xuesheng` */

DROP TABLE IF EXISTS `xuesheng`;

CREATE TABLE `xuesheng` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT COMMENT '主键',
  `addtime` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
  `zhanghao` varchar(200) DEFAULT NULL COMMENT '账号',
  `mima` varchar(200) DEFAULT NULL COMMENT '密码',
  `xingming` varchar(200) DEFAULT NULL COMMENT '姓名',
  `xingbie` varchar(200) DEFAULT NULL COMMENT '性别',
  `shouji` varchar(200) DEFAULT NULL COMMENT '手机',
  `banji` varchar(200) DEFAULT NULL COMMENT '班级',
  `zhuanye` varchar(200) DEFAULT NULL COMMENT '专业',
  `youxiang` varchar(200) DEFAULT NULL COMMENT '邮箱',
  `touxiang` varchar(200) DEFAULT NULL COMMENT '头像',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=17 DEFAULT CHARSET=utf8 COMMENT='学生';

/*Data for the table `xuesheng` */

insert  into `xuesheng`(`id`,`addtime`,`zhanghao`,`mima`,`xingming`,`xingbie`,`shouji`,`banji`,`zhuanye`,`youxiang`,`touxiang`) values (11,'2021-05-15 14:45:08','学生1','123456','姓名1','男','13823888881','班级1','专业1','773890001@qq.com','http://localhost:8080/ssmwx41b/upload/xuesheng_touxiang1.jpg');
insert  into `xuesheng`(`id`,`addtime`,`zhanghao`,`mima`,`xingming`,`xingbie`,`shouji`,`banji`,`zhuanye`,`youxiang`,`touxiang`) values (12,'2021-05-15 14:45:08','学生2','123456','姓名2','男','13823888882','班级2','专业2','773890002@qq.com','http://localhost:8080/ssmwx41b/upload/xuesheng_touxiang2.jpg');
insert  into `xuesheng`(`id`,`addtime`,`zhanghao`,`mima`,`xingming`,`xingbie`,`shouji`,`banji`,`zhuanye`,`youxiang`,`touxiang`) values (13,'2021-05-15 14:45:08','学生3','123456','姓名3','男','13823888883','班级3','专业3','773890003@qq.com','http://localhost:8080/ssmwx41b/upload/xuesheng_touxiang3.jpg');
insert  into `xuesheng`(`id`,`addtime`,`zhanghao`,`mima`,`xingming`,`xingbie`,`shouji`,`banji`,`zhuanye`,`youxiang`,`touxiang`) values (14,'2021-05-15 14:45:08','学生4','123456','姓名4','男','13823888884','班级4','专业4','773890004@qq.com','http://localhost:8080/ssmwx41b/upload/xuesheng_touxiang4.jpg');
insert  into `xuesheng`(`id`,`addtime`,`zhanghao`,`mima`,`xingming`,`xingbie`,`shouji`,`banji`,`zhuanye`,`youxiang`,`touxiang`) values (15,'2021-05-15 14:45:08','学生5','123456','姓名5','男','13823888885','班级5','专业5','773890005@qq.com','http://localhost:8080/ssmwx41b/upload/xuesheng_touxiang5.jpg');
insert  into `xuesheng`(`id`,`addtime`,`zhanghao`,`mima`,`xingming`,`xingbie`,`shouji`,`banji`,`zhuanye`,`youxiang`,`touxiang`) values (16,'2021-05-15 14:45:08','学生6','123456','姓名6','男','13823888886','班级6','专业6','773890006@qq.com','http://localhost:8080/ssmwx41b/upload/xuesheng_touxiang6.jpg');

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

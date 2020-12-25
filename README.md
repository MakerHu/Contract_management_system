# Contract_management_system
合同管理系统
拉取本项目后需要先配置数据库
本项目使用MySQL数据库
在MySQL中创建用户cmsmanager
命令：
CREATE USER 'cmsmanager'@'%' IDENTIFIED BY '123456';
用root用户创建数据库cms并将cms的所有权限授予cmsmanager
命令：
CREATE DATABASE cms;
GRANT ALL PRIVILEGES ON cms.* TO 'cmsmanager'@'%';

启动项目前先运行项目中的initialize.py初始化数据库中的一些数据，如最高管理员root,密码123456

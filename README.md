# Contract_management_system
合同管理系统<br>
<br>
拉取本项目后需要先配置数据库<br>
本项目使用MySQL数据库<br>
<br>
在MySQL中创建用户cmsmanager
命令：<br>
CREATE USER 'cmsmanager'@'%' IDENTIFIED BY '123456';<br>
<br>
用root用户创建数据库cms并将cms的所有权限授予cmsmanager<br>
命令：<br>
CREATE DATABASE cms;<br>
GRANT ALL PRIVILEGES ON cms.* TO 'cmsmanager'@'%';<br>
<br>
启动项目前先运行项目中的initialize.py初始化数据库中的一些数据，如最高管理员root,密码123456<br>
<br>
其他可能用到的命令<br>
数据迁移<br>
python manage.py makemigrations<br>
python  manage.py migrate<br>
<br>
环境安装<br>
pip install --upgrade -i https://pypi.tuna.tsinghua.edu.cn/simple django <br>
pip install --upgrade -i https://pypi.tuna.tsinghua.edu.cn/simple pymysql <br>
pip install --upgrade -i https://pypi.tuna.tsinghua.edu.cn/simple cryptography <br>
pip install --upgrade -i https://pypi.tuna.tsinghua.edu.cn/simple apscheduler <br>


import pymysql  # 导入pymysql

pymysql.version_info = (1, 4, 13, "final", 0)
pymysql.install_as_MySQLdb()  # 设置默认数据库为mysql

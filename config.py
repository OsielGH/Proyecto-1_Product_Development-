DB_ENTPOINT = 'product-dev-2022.cng0wspjwdz4.us-east-1.rds.amazonaws.com'
DB = 'dw_sakila'
DB_USER = 'admin'
DB_PASSWORD = 'admin123'
DB_PORT = '3306'

mysql_connector = 'mysql+pymysql://{}:{}@{}/{}'.format(DB_USER, DB_PASSWORD, DB_ENTPOINT, DB)


import pymysql.cursors

conection = pymysql.connect(host ='localhost',
                            user ='root',
                            password ='',
                            db ='db',
                            charset ='utf8mb4',
                            cursorclass=pymysql.cursors.DictCursor)
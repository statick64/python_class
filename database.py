import pymysql.cursors

#connect to the database
conection = pymysql.connect(host ='localhost',
                            user ='root',
                            password ='',
                            db ='univelcity',
                            charset ='utf8mb4',
                            cursorclass=pymysql.cursors.DictCursor)

file_name = 'loans.csv'
file = open(file_name,'r')

data = file.readline()
print(data)
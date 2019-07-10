import pymysql.cursors

#connect to the database
conection = pymysql.connect(host ='localhost',
                            user ='root',
                            password ='',
                            db ='univelcity',
                            charset ='utf8mb4',
                            cursorclass=pymysql.cursors.DictCursor)
class Sums_Within_Groups():

    def read_file(self):
        file_name = 'loans.csv'
        file = open(file_name,'r')

        data = file.readline()
        print(data)
import pymysql.cursors

# Connect to the database
connection = pymysql.connect(host='localhost',
                             user='root',
                             database='multicloud',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)

import pymysql

def sql(token):
	db_settings={
	       "host":"172.17.0.5",
	       "port":3306,
	       "user":"root",
	       "password":"123456",
	       "db":"DB123",
	       "charset":"utf8"
}

try:
	conn= pymysql.connect(**db_settings)


	with conn.cursor() as cursor:

	         command = "INSERT INTO DB123(aaa)VALUES(%s)"
	         cursor.execute(command,token)
	         conn.commit()

except Exception as ex:
	print(ex)
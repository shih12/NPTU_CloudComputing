import pymysql

def sql(token):
    db_settings = {
        "host": "172.17.0.5",
        "port": 3306,
        "user": "root",
        "password": "123456",
        "db": "computing",
        "charset": "utf8"
    }
    try:
        conn = pymysql.connect(**db_settings)

        with conn.cursor() as cursor:
            command = "INSERT INTO `mes`(`content`) VALUES (%s);"
            cursor.execute(command,token)
            conn.commit()

    except Exception as ex:
        print(ex)

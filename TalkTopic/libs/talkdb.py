import mysql.connector

class Talkdb_operation():
    
    def get_all_data(self):
        ##取得sf db裡面所有資料
        user = 'root'
        pwd = 'eric8767'

        connection = mysql.connector.connect(host='localhost',
                                            port='3306',
                                            user= user,
                                            password= pwd,
                                            database='mmnlab')

        cursor = connection.cursor() #建立sql server連線

        # 取表格所有資料
        cursor.execute('SELECT * FROM `talk_info`;')


        reg_string = ''
        records = cursor.fetchall()
        for r in records:
            reg_string += str(r) + '\n'

        cursor.close()
        connection.close()
        print("output_success")

        return reg_string

    
    def talkdb_insert(self, who, said, time):

        user = 'root'
        pwd = 'eric8767'

        connection = mysql.connector.connect(host='localhost',
                                            port='3306',
                                            user= user,
                                            password= pwd,
                                            database='mmnlab')

        cursor = connection.cursor()

        # 把msg插入表格裡面
        sql_insert = "INSERT INTO `talk_info` VALUES('" + str(who) + "', '" + str(said) + "' , " + str(time) + ");"
        cursor.execute(sql_insert)

        
        cursor.close()
        connection.commit()   ##只要有動到資料的最後都一定要補上這句。
        connection.close()
        print('插入成功')

        return 'insert successful'
#Code to connect to db

import pymysql


def mysqlconnect():
    # To connect MySQL database
    conn = pymysql.connect(
        host='localhost',
        user='root',
        password="Manjunath96@",
        db='manjunathdb',
    )

    cur = conn.cursor()
    return cur
    # cur.execute("select * from emp_details")
    # output = cur.fetchall()
    # print(output)
    #
    # # To close the connection
    # conn.close()


# Driver Code
if __name__ == "__main__":
    mysqlconnect()

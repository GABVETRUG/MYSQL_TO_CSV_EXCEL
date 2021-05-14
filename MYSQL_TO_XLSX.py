import pandas as pd
import mysql.connector as msql
from mysql.connector import Error
import time
import progressbar


def convert(string):
    li = list(string.split(", "))
    return li


def user_inputs():
    print(
        "Welcome to the MYSQL_to_XLSX converter script!\nFirst of all, insert your connection parameters here as follows:")
    print("\n1)host\n2)user\n3)password\n4)db\n ")
    user = str(input())
    conn_params = convert(user)
    print("\nPerfect! Now insert your tabs, separated by a ,\n")
    tabs = str(input())
    tables = convert(tabs)
    return conn_params, tables


def export():
    start = time.time()
    conn_params, tables = user_inputs()
    stats = open('./stats.txt', 'a')
    print("Conn Params: ", conn_params)
    print("Tables: ", tables)
    try:
        print("Starting the execution right now\n")
        conn = msql.connect(host=conn_params[0], user=conn_params[1], password=conn_params[2],
                            auth_plugin='mysql_native_password', db=conn_params[3])
        print("Connected to the db")
        for i in tables:
            print("\nExporting " + i + " tab right now")
            for y in progressbar.progressbar(range(100)):
                query = "SELECT * FROM " + i + ";"
                frame = pd.read_sql_query(query, con=conn)
                frame.to_excel("./" + i + '.xlsx', index=False)
        end = time.time()
        stats.write("\nFiles exported: " + str(tables) + "\nTotal export time: " + "%.2f" % float(
            (end - start) / 60) + " minutes\n")
        print("\nStats file written\n")
        stats.close()
    except Error as e:
        print("\nError while connecting to MySQL", e)

        
if __name__ == '__main__':
    export()

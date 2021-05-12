# MYSQL_TO_CSV_EXCEL
This is a simple script in order to export your tabs from MYSQL DB to .xlsx

Features:

- very low memory usage
- few chuncks of code
- easy to maintain

Required libraries:

- pandas
- mysql-connector
- time
- progressbar (search for progressbar2)
- openpyxl

What do you need?

- config parameters (host, user, password, db)  ->  it's a normal input prompt
- tables list                                   ->  all your wished tables, separed by a ' , ' 

An example:

# Config file:

localhost, root, mypassword, mydb

# Tables list

employee, courses, payments, bills

# Testing

128 rows / 6 tables   -->   40 seconds

100k rows / 1 table   -->   25:40 minutes

# Some additional information

As a reminder, do not try to export 1M ca. data rows into .xlsx. Because of that, Microsoft Excel could severally impact your system's performances. 
See the #testing section to know more about.

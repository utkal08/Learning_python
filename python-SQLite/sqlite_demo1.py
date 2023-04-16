import sqlite3

from employee import Employee

conn = sqlite3.connect('employee.db')

c = conn.cursor()

'''c.execute("""CREATE TABLE employees(
             first text,
             last text,
             pay integer
            )""")'''

emp_1= Employee('John','Wick',1000000)
emp_1= Employee('helen','Wick',1000000)


c.execute("INSERT INTO  employees VALUES (?,?,?)",(emp_1.first,emp_1.last,emp_1.pay))

conn.commit()

c.execute("INSERT INTO  employees VALUES (?,?,?)",(emp_1.first,emp_1.last,emp_1.pay))

conn.commit()


c.execute("SELECT *FROM employees WHERE last ='schefer'")

print(c.fetchall())
conn.commit()
conn.close()
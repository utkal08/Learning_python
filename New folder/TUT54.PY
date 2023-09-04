import os 
db_user ='my_db_user'
db_password='my_db_pass_123!'
db_user=os.environ.get('DB_USER')
db_password=os.environ.get('DB_PASS')

print(db_user)
print(db_password)
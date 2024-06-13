cursor=mydb.cursor()
cursor.execute(
    """
    SHOW TABLES
    """
)

for i in cursor:
    print(i)
import mysql.connector
db=mysql.connector.connect(host="localhost",user="root",passwd="sobikaa3723",database="contact")
cur=db.cursor()
#cur.execute("create table Contacts(contact_name varchar(20),phone_no int NOT NULL,email varchar(30) NOT NULL,image varchar(15),address varchar(30),CONSTRAINT UC_Contacts UNIQUE (phone_no,email))")
#cur.execute("ALTER TABLE Contacts MODIFY phone_no VARCHAR(10)")
#ins="insert into Contacts(contact_name,phone_no,email,image,address) values(%s,%s,%s,%s,%s)"
#contact_details=[("sam","8976543210","sam@gmail.com","img1.jpg","chennai"),("jach","8978743210","jack@gmail.com","img2.jpg","coimbatore"),("micky","9765432180","micky@gmail.com","img3.jpg","chennai")]
#cur.executemany(ins,contact_details)
print("ALL DATA BEFORE OPERATIONS")
cur.execute("select * from Contacts")
data=cur.fetchall()
for j in data:
	print(j)
print("SEARCH CONTACT")
s="select * from Contacts where contact_name=%s"
name=("sam", )
cur.execute(s, name)
record=cur.fetchall()
for row in record:
	print(row)
u="UPDATE Contacts set address='chennai' where email=%s"
up=("micky@gmail.com", )
cur.execute(u, up)
d="DELETE from Contacts where contact_name=%s"
d_name=("jach", )
cur.execute(d,d_name)
print("ALL DATA AFTER OPERATIONS")
cur.execute("select * from Contacts")
alldata=cur.fetchall()
for i in alldata:
	print(i)
db.commit()
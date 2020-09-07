print("")
print("Welcome to Black Phin Room Management System".center(130))
import mysql.connector
sql_connector=mysql.connector.connect(host="localhost",user="root",passwd="admin",database="mysql")
sql_cursor=sql_connector.cursor()
sql_cursor.execute("DROP DATABASE Hotel")
sql_cursor.execute("CREATE DATABASE Hotel")
sql_cursor.execute("USE Hotel")
sql_cursor.execute("CREATE TABLE Room_Details (Room_Type CHAR(20), Rooms_Available INT, Price INT)")
sql=("INSERT INTO Room_Details VALUES (%s, %s, %s)")
val=[
("Economy",40, 1000),
("Deluxe",20, 2000),
("Super Deluxe",10, 2500),
("Premium Suite",5, 4000)
]
sql_cursor.executemany(sql, val)
sql_connector.commit()
while True:
	user=str(input("Enter your Username: "))
	passwd=str(input("Enter your Password: "))
	if user=="admin" and passwd=="admin":
		invoice_no=1000
		while True:
			sql_cursor.execute("SELECT * FROM Room_Details")
			data=sql_cursor.fetchall()
			print(data)
			a=(data[0])[1]
			b=(data[1])[1]
			c=(data[2])[1]
			d=(data[3])[1]
			print("")
			print("")
			print("Rooms Available: ",end="")
			if a>0:
				print((data[0])[0],"| ",end="")
			if b>0:
				print((data[1])[0],"| ",end="")
			if c>0:
				print((data[2])[0],"| ",end="")
			if d>0:
				print((data[3])[0],"| ")
			sql_cursor.execute("SELECT (Price) FROM Room_Details")
			price_all=sql_cursor.fetchall()
			while True:
				room_type=str(input("Select the type of Room Needed: "))
				if room_type=="Economy":
					room_type="Economy"
					price=(price_all[0])[0]
					available=a
					break
				if room_type=="Deluxe":
					room_type="Deluxe"
					price=(price_all[1])[0]
					available=b
					break
				if room_type=="Super Deluxe":
					room_type="Super Deluxe"
					price=(price_all[2])[0]
					available=c
					break
				if room_type=="Premium Suite":
					room_type="Premium Suite"
					price=(price_all[3])[0]
					available=d
					break
				else:
					print("")
					print("Enter a Valid Option".center(130))
			print("")
			print("The price of 1",room_type,"room for 1 night is",price)
			print("")
			while True:
				confirm=str(input("Do you want to proceed with the booking (Yes/No): "))
				print("")
				if confirm=="Yes":
					print("Customer Details".center(130))
					name=str(input("Full Name: "))
					email=str(input("Email: "))
					phone=int(input("Phone: "))
					print("")
					print("Booking Details".center(130))
					while True:
						quantity=int(input("Number of Rooms: "))
						if quantity<=available:
							while True:
								from datetime import date
								today=date.today()
								date=today.strftime("%d/%m/%Y")
								guests=int(input("Number of Guests: "))
								if guests<=(quantity*3):
									nights=int(input("Number of Nights: "))
									print("")
									print("Total amount to be paid:",(price*quantity))
									print("")
									print("Booking has been created".center(130))
									invoice_no+=1
									invoice_list=[]
									invoice_list.append("Black Phin Hotel".center(100)+"\n")
									invoice_list.append("Sector-13, Dwarka, New Delhi".center(100)+'\n')
									invoice_list.append(""+'\n')
									invoice_list.append("Billing Date: ")
									invoice_list.append(date+'\n')
									invoice_list.append("Invoice No.: ")
									invoice_list.append(str(invoice_no)+'\n')
									invoice_list.append(""+'\n')
									invoice_list.append(""+'\n')
									invoice_list.append("Customer Details".center(100)+'\n')
									invoice_list.append("Name: ")
									invoice_list.append(name+'\n')
									invoice_list.append("Email: ")
									invoice_list.append(email+'\n')
									invoice_list.append("Phone Number: ")
									invoice_list.append(str(phone)+'\n')
									invoice_list.append(""+'\n')
									invoice_list.append("Booking Details".center(100)+'\n')
									invoice_list.append("Room Type: ")
									invoice_list.append(room_type+'\n')
									invoice_list.append("No. of Rooms: ")
									invoice_list.append(str(quantity)+'\n')
									invoice_list.append("No. of Guests: ")
									invoice_list.append(str(guests)+'\n')
									invoice_list.append("No. of Nights: ")
									invoice_list.append(str(nights)+'\n')
									invoice_list.append(""+'\n')
									invoice_list.append(""+'\n')
									invoice_list.append("Total Amount Paid: ")
									invoice_list.append(str(price*quantity))
									file=open("D:\\Invoice.txt", 'w')
									file.writelines(invoice_list)
									file.close()
									delete="UPDATE Room_Details SET Rooms_Available="+str(available-quantity)+" WHERE Rooms_Available="+str(available)
									sql_cursor.execute(delete)
									sql_connector.commit()
									break
								else:
									print("Only 3 Persons per Room are allowed")
							break
						else:
							print("Only",available,"Rooms are available in this category")
					break
				elif confirm=="No":
					print("The Booking has been cancelled")
					break
				else:
					print("")
					print("Enter a Valid input")
		break
	else:
		print("Wrong ID/Password".center(130))
user_details=[]
rooms=[1,2,3,4]
roomdata={}

def take_data():    #this function takes the user data from the console and save them in a dicsnary and also save a copy in a text file
    global roomdata # "global" keyword makes the variables glibal so that the changes we made inside the function is applied globally  
    global rooms
    
    file1=open("database.txt","a")  # this part open the text file in append permission 
    
    name=input("Enter Customer's Name: ")
    age=input("Enter Customer's age: ")
    phno=input("Enter Customer's phno: ")
    email=input("Enter Customer's email: ")
    if int(age)>18 and len(phno)==10 and "@gmail.com" in email:     #this checks the data is authintic or not and also the clint is above 18 years or not   
        print("Booked!")
        user_detail=[name,age,phno,email]
        groom=rooms.pop(0)  #this part remove the booked room number from the rooms list 
        roomdata[groom]=user_detail  #this part register the room number with the customer details
        #print(roomdata)
        
        file1.write(str(groom)+":"+"\t"+name+"\t"+age+"\t"+phno+"\t"+email+"\n")    #this part writes the details on a text file and save that
        file1.close()
        
    else:
        print("Something went wrong.") 
def enq():
    #this function provides the customer details who are staying in a perticular room number
    global roomdata
    try:
        z=eval(input("room number:"))
        print(roomdata[z])
    except:
        print("something went wrong!")
def chkout():
    #this function semulate the checkout function of a hotel
    global roomdata
    global rooms
    try:
        a=eval(input("Enter the room number: "))
        roomdata.pop(a)   #Delets the details from the existing user details
        rooms.append(a)   #adds the cheked out room number at the end of the free room lists
    except:
        print("something went wrong!")
    
def vacant_rooms():
    #this function Shows the vackent rooms
    global roomdata
    try:
        for i in rooms:
            print(i)
    except:
        print("!")

        

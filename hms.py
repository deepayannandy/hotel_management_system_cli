import hotel 
while True:
    print("""############### HMS ###############\n""")
    print("""1. New Booking""")
    print("""2. Checkout""")
    print("""3. ENQ""")
    print("""4. AVL Rooms""")
    print("""############### End ###############\n""")
    x=input("choose your option :")
    if x=="1":
        print("############### Enter the details ###############\n")
        hotel.take_data()
        print("############### End ###############\n")
    elif x=="2":
    	print("############### Checkout ###############\n")
    	hotel.chkout()
    	print("############### End ###############\n")
    elif x=="3":
    	print("############### client Details ###############\n")
    	hotel.enq()
    	print("############### End ###############\n")
    elif x=="4":
    	print("############### vackent rooms ###############\n")
    	hotel.vacant_rooms()
    	print("############### End ###############\n")

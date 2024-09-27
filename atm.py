pin=int(input("enter your pin:")) #pin...2222
balance=987654
contact=+917093677755
if pin==2222:
   print("welcome to python bank")
   print("1.balance to enquiry")
   print("2.withdraw")
   print("3.depopsit")
   print("4.help")
   option=int(input("enter your option"))
   if option==1:
      print("your currrent balance:",balance,"rs/-")
   elif option==2:
       w_amount=int(input("enter withdraw amount:"))
       if w_amount<=balance:
          balance=balance-w_amount
          print("your updated balance is:",balance)
       else:
           print("insufficient balance")
   elif option==3:
        deposit_amount=int(input("enter deposit amount:"))
        balance=balance+deposit_amount
        print("your updated balance:",balance)
   elif option==4:
        print("please call to tollfree number:",contact)
   else:
       print("invaild option")
    
             
else:
   print("invalid pin")

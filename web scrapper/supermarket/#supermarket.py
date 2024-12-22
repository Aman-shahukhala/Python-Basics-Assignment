#supermarket v1 simple without functions or classes
import random


chips_quantity= random.randint(1, 64)
soap_quantity= random.randint(1, 64)
noodles_quantity= random.randint(1, 64)
coke_quantity= random.randint(1, 64)
potato_quantity= random.randint(1, 64)
chips_price = 50
soap_price = 20
noodles_price= 35
coke_price = 250
potato_price = 1000
total_cost=0
cart= {}


 
print("welcome to the supermarket")
while True:
 print("1. add item ")
 print("2. remove item ")
 print("3. view cart ")
 print("4. check out ")
 choice = int(input("What would you like to do? "))
 if choice == 1:
  while True:
   print(f"1. Chips   {chips_quantity} left  {chips_price}rs")
   print(f"2. Soap    {soap_quantity} left {soap_price}rs")
   print(f"3. Noodles {noodles_quantity} left {noodles_price}rs")
   print(f"4. Coke    {coke_quantity} left {coke_price}rs")
   print(f"5. Potato  {potato_quantity} left{potato_price}rs")
   print(f"6. go back")
   choice_item = int(input("what do you wanna add to your cart "))
   if choice_item ==1:
     choice_quantity= int(input("how many? "))
     if chips_quantity < choice_quantity:
        print (f"there is not {choice_quantity}  of chips remaining")
     else:
       chips_quantity= chips_quantity - choice_quantity
       total_cost= choice_quantity*chips_price+total_cost
       chips_cart= choice_quantity
       print(f"your total cost till now is {total_cost}") #change later
       cart.update({"chips": chips_cart})
   elif choice_item ==2:
     choice_quantity= int(input("how many? "))
     if soap_quantity < choice_quantity:
        print (f"there is not {choice_quantity}  of  soap remaining")
     else:
        soap_quantity= soap_quantity - choice_quantity
        total_cost= choice_quantity*soap_price+total_cost
        soap_cart= choice_quantity
        print(f"your total cost till now is {total_cost}") #change later
        cart.update({"soap": soap_cart})
   elif choice_item == 3:
     choice_quantity= int(input("how many? "))
     if noodles_quantity < choice_quantity:
        print (f"there is not {choice_quantity}  of  noodles remaining")
     else:
        noodles_quantity= noodles_quantity - choice_quantity
        total_cost= choice_quantity*noodles_price+total_cost
        noodles_cart= choice_quantity
        print(f"your total cost till now is {total_cost}") #change later
        cart.update({"noodles": noodles_cart})
   elif choice_item == 4:
     choice_quantity= int(input("how many? "))
     if coke_quantity < choice_quantity:
        print (f"there is not {choice_quantity}  of  coke remaining")
     else:
        coke_quantity= coke_quantity - choice_quantity
        total_cost= choice*coke_price+total_cost
        coke_cart= choice_quantity
        print(f"your total cost till now is {total_cost}") #change later
        cart.update({"coke": coke_cart})
   elif choice_item == 5:
     choice_quantity= int(input("how many? "))
     if coke_quantity < choice_quantity:
       print (f"there is not {choice_quantity}  of  potato remaining")
     else:
        potato_quantity= potato_quantity - choice_quantity
        total_cost= choice_quantity*potato_price + total_cost
        potato_cart= choice_quantity
        print(f"your total cost till now is {total_cost}") #change later
        cart.update({"potato": potato_cart})
   elif choice_item == 6:    
        break
 elif choice ==2:
   while True:
     print(cart) 
     print("enter 'nothing' if you want to go back ")
     remove= input("what would you like to remove")
     if remove == "chips" or "soap" or "coke" or "potato" or "noodles":
      total_cost= total_cost - cart[f"{remove}"]
      del cart[f"{remove}"]
     elif remove == "nothing":
      break
     else:
      print("item no found")
 elif choice == 3:
   print(cart)
 elif choice == 4:
   print(f"your items are {cart}")
   print(f"your total is {total_cost}")
   break


   
     
     

    
    

 
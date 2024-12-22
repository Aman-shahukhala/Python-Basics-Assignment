#super market v2 with functions and classes
import random
class Items:
 def __init__(self,item_name:str,price:int, quantity:int):
    self.item_name= item_name
    self.price =price
    self.quantity = quantity
class Cart_items():
  def __init__(self, item_name:str, price, quantity):
    self.price = price
    self.item_name = item_name
    self.quantity= quantity
    
    pass
def quantity():
 amount = int(input(" how many? :"))
 return amount
def no_stock(a):
  print(f"there isn't {choice_quantity} of {a.item_name} remaining")
def total_cost(a, b):
  total = a*b
  return total 
def remove_num():
  a= int(input(" enter the amount you would like to remove"))
  return a
def remove_cost(a, b, c):
  c= c-(a*b)
  return c
def insuff():
   print(" you don't have that many items")
  
item1= Items("chip", 50, random.randint(1,55))
item2= Items("soap", 30, random.randint(1,55))
item3 = Items("noodles", 25,random.randint(1,55))
item4= Items("Coke", 250, random.randint(1,55))
item5= Items("potato",1000, random.randint(1,55))
c_item1= Cart_items("", 0 , 0)
c_item2= Cart_items("", 0, 0)
c_item3= Cart_items("", 0 , 0)
c_item4= Cart_items("", 0 , 0)
c_item5= Cart_items("", 0 , 0)
actual_cost= 0
print("welcome to the supermarket")
while True:
   print("1. add item ")
   print("2. remove item ")
   print("3. view cart ")
   print("4. check out ")
   choice = int(input("What would you like to do? "))
   if choice == 1:
     while True:
       print(f"1. Chips   {item1.quantity} left Rs.{item1.price}")           
       print(f"2. Soap    {item2.quantity} left Rs.{item2.price}")
       print(f"3. Noodles {item3.quantity} left Rs.{item3.price}")
       print(f"4. Coke    {item4.quantity} left Rs.{item4.price}")
       print(f"5. Potato  {item5.quantity} left Rs.{item5.price}")
       print(f"6. go back")
       choice_item = int(input("what do you wanna add to your cart? : "))
       if choice_item ==1:
           choice_quantity= quantity()
           if item1.quantity < choice_quantity:
             no_stock(item1)
           else:
             item1.quantity= item1.quantity - choice_quantity
             actual_cost = total_cost(choice_quantity, item1.price) +  actual_cost
             print(f"your total cost till now is {actual_cost}")
             c_item1= Cart_items(item1.item_name,item1.price, choice_quantity)
       elif choice_item == 2:
          choice_quantity= quantity()
          if item2.quantity < choice_quantity:
             no_stock(item2)
          else:
             item2.quantity= item2.quantity - choice_quantity
             actual_cost = total_cost(choice_quantity, item2.price) +  actual_cost
             print(f"your total cost till now is {actual_cost}")
             c_item2= Cart_items(item2.item_name,item2.price, choice_quantity)
       elif choice_item == 3:
          choice_quantity= quantity()
          if item3.quantity < choice_quantity:
             no_stock(item3)
          else:
             item3.quantity= item3.quantity - choice_quantity
             actual_cost = total_cost(choice_quantity, item3.price) +  actual_cost
             print(f"your total cost till now is {actual_cost}")
             c_item3= Cart_items(item3.item_name,item3.price, choice_quantity)
       elif choice_item == 4:
          choice_quantity= quantity()
          if item4.quantity < choice_quantity:
             no_stock(item4)
          else:
             item4.quantity= item4.quantity - choice_quantity
             actual_cost = total_cost(choice_quantity, item4.price) +  actual_cost
             print(f"your total cost till now is {actual_cost}")
             c_item4= Cart_items( item4.item_name,item4.price, choice_quantity)  
       elif choice_item == 5:
          choice_quantity= quantity()
          if item5.quantity < choice_quantity:
             no_stock(item4)
          else:
             item5.quantity= item5.quantity - choice_quantity
             actual_cost = total_cost(choice_quantity, item5.price) +  actual_cost
             print(f"your total cost till now is {actual_cost}")
             c_item5= Cart_items(item5.item_name,item5.price, choice_quantity)
       elif choice_item == 6:
          break 
   elif choice == 2:
      while True:
       print(f"1. {c_item1.item_name} , {c_item1.quantity}")
       print(f"2. {c_item2.item_name} , {c_item2.quantity}")
       print(f"3. {c_item3.item_name}, {c_item3.quantity}")
       print(f"4. {c_item4.item_name}, {c_item4.quantity}")
       print(f"5. {c_item5.item_name}, {c_item5.quantity}")
       print("6. to remove nothing")
       remove = int(input("which item would you like to remove? "))
       if remove ==1:
        re_num = remove_num()
        if re_num> c_item1.quantity:
           insuff()
       elif re_num == c_item1.quantity:
          c_item1 = ("", 0, 0)
       else:
          actual_cost = remove_cost(c_item1.quantity, c_item1.price , actual_cost )
          c_item1.quantity = c_item1.quantity - re_num
       if remove ==2:
        re_num = remove_num()
        if re_num> c_item2.quantity:
          insuff()
       elif re_num == c_item2.quantity:
         c_item2 = ("", 0, 0)
       else:
         actual_cost = remove_cost(c_item2.quantity, c_item2.price , actual_cost )
         c_item2.quantity = c_item2.quantity - re_num
       if remove ==3:
        re_num = remove_num()
        if re_num> c_item3.quantity:
           insuff()
       elif re_num == c_item3.quantity:
          c_item3 = ("", 0, 0)
       else:
          actual_cost = remove_cost(c_item3.quantity, c_item3.price , actual_cost )
          c_item3.quantity = c_item3.quantity - re_num 
       if remove ==4:
        re_num = remove_num()
        if re_num> c_item4.quantity:
           insuff()
       elif re_num == c_item4.quantity:
         c_item4 = ("", 0, 0)
       else:
          actual_cost = remove_cost(c_item4.quantity, c_item4.price , actual_cost )
          c_item4.quantity = c_item4.quantity - re_num
       if remove ==5:
        re_num = remove_num()
        if re_num> c_item5.quantity:
           insuff()
       elif re_num == c_item5.quantity:
          c_item5 = ("", 0, 0)
       else:
         actual_cost = remove_cost(c_item5.quantity, c_item5.price , actual_cost )
         c_item5.quantity = c_item5.quantity - re_num
      else:
        break
   elif choice ==3:
     print(f"1. {c_item1.item_name} , {c_item1.quantity}")
     print(f"2. {c_item2.item_name} , {c_item2.quantity}")
     print(f"3. {c_item3.item_name}, {c_item3.quantity}")
     print(f"4. {c_item4.item_name}, {c_item4.quantity}")
     print(f"5. {c_item5.item_name}, {c_item5.quantity}")
   elif choice ==4:
     print("reciept")
     print(f"1. {c_item1.item_name} , {c_item1.quantity}")
     print(f"2. {c_item2.item_name} , {c_item2.quantity}")
     print(f"3. {c_item3.item_name}, {c_item3.quantity}")
     print(f"4. {c_item4.item_name}, {c_item4.quantity}")
     print(f"5. {c_item5.item_name}, {c_item5.quantity}") 
     print(f" your total amount is {actual_cost}")

      
             
            

  
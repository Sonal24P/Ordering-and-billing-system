import datetime
class billingCounter():
  def __init__(self):
    self.count=1
    self.quantity=0
    self.press_key=None
    self.choice=None
    self.total_amount=0
    self.Menu={"Pav bhaji":60,"Chesse Pav Bhaji":70,"Aloo Paratha":90,"Mumbai Poha":50,"Upma":70,"Sev Usal":100,"Misal Pav":150,"Dhokla":60,"Fafda":80,"Jalebi":60,"Sandwich":70,"Club Sandwich":140}
    self.ordered_items={}
    self.removeItem=None


  def menuList(self,choice):
    for item,price in self.Menu.items():
      if choice=="y":
        print("Press",self.count,"to select",item,"--> INR",price)
        self.count+=1
      elif choice=="c":
        print("Press",self.count,"to remove",item)
        self.count+=1
    self.count=1

  def customer_Choice(self):
    self.choice=input("Please enter your choice (Y to order an item /N to confirm the order /C to change the order)? ").lower()
    if self.choice not in ["y","n","c"]:
      print("Please enter a valid choice")
      self.customer_Choice()
    return self.choice


  def add_item(self,press_key):
      self.press_key=press_key
      if self.press_key in range(len(self.Menu)+1):
        ordered_item=list(self.Menu.keys())[self.press_key-1]
        self.quantity=int(input("Enter the quantity : "))
        if ordered_item in self.ordered_items.keys():
          self.ordered_items[ordered_item]+=self.quantity
          print("The quantity is added successfully")
        else:
          self.ordered_items[ordered_item]=self.quantity
          print("The item is added successfully")
      else:
        print("Please enter a valid Id")
        self.add_item(press_key)


  def remove_item(self,press_key):    
      removeItem=list(self.Menu.keys())[press_key-1]
      if removeItem in self.ordered_items.keys() :
        ordered_item=list(self.Menu.keys())[self.press_key-1]
        self.quantity=int(input("Enter the quantity : "))
        if ordered_item in self.ordered_items.keys():
          if self.quantity<=self.ordered_items[ordered_item]:
            self.ordered_items[ordered_item]-=self.quantity
            print("The item is removed successfully")
          else:
            print("Please enter a valid quantity")
            self.remove_item(press_key)
        else:
          print("Sorry the item is not in the ordered items")
      else:
        print("Please enter a valid Id")
        press_key=int(input("Enter the item Id you want to remove : "))
        self.remove_item(press_key)

  def billing_details(self):
    for item  in self.ordered_items.keys():
      print("{:<20} {:<10} {:<10} {:<10}".format(item,self.ordered_items[item],self.Menu[item],self.ordered_items[item]*self.Menu[item]))
      self.total_amount+=self.ordered_items[item]*self.Menu[item]
  
    if datetime.datetime.now().strftime("%A") in ["Wednesday","Friday"]:
      self.total_amount-=(self.total_amount*0.1)
      if self.total_amount>1000:
        self.total_amount-=(self.total_amount*0.15)
        print("{:<42} {:<20}".format("Discount(25%)",self.total_amount*0.25))
        print("{:<42} {:<20}".format("Grand Total",self.total_amount))
      else:
        print("{:<42} {:<20}".format("Discount(10%)",self.total_amount*0.10))
        print("{:<42} {:<20}".format("Grand Total",self.total_amount))

    elif self.total_amount>1000:
      self.total_amount-=(self.total_amount*0.15)
      print("{:<42} {:<20}".format("Discount(15%)",self.total_amount*0.15))
      print("{:<42} {:<20}".format("Grand Total",self.total_amount))
    else:
      print("{:<42} {:<20}".format("Discount(0%)",0))
      print("{:<42} {:<20}".format("Grand Total",self.total_amount))
      

try:
  billingClass=billingCounter()
  press_key=None
  print("-----------------------------------Welcome to Sun Moon Resturant-------------------------------------")
  print("Special Offer 1: 10 % off on every visit on Wednesday and Friday ")
  print("Special Offer 2: 15 % off on order above 1000")
  while True:
    choice=billingClass.customer_Choice()
    billingClass.menuList(choice)
    if choice=="y":
      press_key=int(input("Enter the item Id you want to order : "))
      billingClass.add_item(press_key)
    elif choice=="c": 
      press_key=int(input("Enter the item Id you want to remove : "))
      billingClass.remove_item(press_key)
    elif choice=="n" and press_key==None:
      print("Please call us when you want to order")
      break
    elif choice=="n" and not press_key==None:
      print("{:<20} {:<10} {:<10} {:<10}".format("Item","Quantity","Price","Total"))
      print("Your order is confirmed")
      billingClass.billing_details()
      break

except:
  print("Something went Wrong")
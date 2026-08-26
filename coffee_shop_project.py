MENU = {
    "espresso" :{
        "ingredients" :{
            "coffee" : 20,
            "water" : 150,
            "sugar" : 10
            
        },"cost" : 100
    
    
},
"latte" :{
    "ingredients" :{
        "coffee" : 30,
        "water" : 100,
        "milk" : 150,
        "sugar" : 10,
    },"cost" : 150
},
"cappuccino" :{
    "ingredients" :{
        "coffee" : 40,
        "water" : 80,
        "milk" : 100,
        "sugar" : 10,

    },"cost": 200
}
    
}
profit = 0
resources ={
    "water" :500,
    "coffee" : 200,
    "milk" : 500,
    "sugar": 100,
 
}
def is_resource_sufficient(other_ingredients):
  for item in other_ingredients:
    if other_ingredients[item] >= resources[item]:
       print(f"sorry,not enough {item}")
       return False
  return True


def make_money():
  total = int(input("Enter the amount in INR: "))
  return total


def is_transaction_successful(money_recieved,drink_cost):
  if money_recieved > drink_cost:
    change = round(money_recieved - drink_cost,2)
    print(f"Here is your {change} change. ")
    global profit
    profit += drink_cost
    return True
  else:
      print("sorry not enough money. money refunded")
  return False

def make_coffee(drink_name,ingredients):
  for items in ingredients:
       resources[items] -= ingredients[items]
  print(f"here is your {drink_name}.Enjoy your coffee")

is_on = True
while is_on:
 choice = input("Enter what you want(espresso/latte/cappuccino): ")
 if choice == "off":
  is_on = False
 elif choice == "report":
  print(f"water:  {resources['water']}ml")
  print(f"coffee:  {resources['coffee']}gm")
  print(f"milk:  {resources['milk']}ml")
  print(f"sugar:  {resources['sugar']}gm")
  print(f"money:  {profit}")
 else:
  drink = MENU .get(choice)
  if choice == "":
    print("please try again")
    continue

  sugar_free = input("Do you want it with sugar(yes/no) :").lower()

  ingredients = drink["ingredients"].copy()
  if sugar_free == "yes":
    if "sugar" in ingredients:
     ingredients["sugar"] = 0
     print("preparing a sugar free dink")



  if is_resource_sufficient(drink["ingredients"]):
    payment = make_money()
    if is_transaction_successful(payment,drink["cost"]):
      make_coffee(choice,drink["ingredients"])

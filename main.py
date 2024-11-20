# def calculate_rocket_fuel_required(distance):
#    requiredFuel = distance * 15
#    if requiredFuel < 100:
#        requiredFuel = 100
#    print(requiredFuel)

# distance = int(input("Enter the distance the rocket will travel: "))
# calculate_rocket_fuel_required(distance)

def calculate_ticket_price_for_performer(regular_ticket_price, performer_type):
   if performer_type == "Juggler":
        cost = regular_ticket_price - (regular_ticket_price * 0.5)
        print(cost)
   elif  performer_type == "Fire twirlers":
        cost = regular_ticket_price - (regular_ticket_price * 0.25)
        print(cost)
   elif performer_type == "Magician":
        cost = regular_ticket_price - (regular_ticket_price * 0.80)
        print(cost)
   elif performer_type == "Escape Artist":
        cost = regular_ticket_price - (regular_ticket_price * 1)
        print(cost)
   else:
        cost = regular_ticket_price
        print(cost)

   return cost

price = int(input("enter ticket price: "))
performer = input("Enter performer type: ")
calculate_ticket_price_for_performer(price, performer)
def get_new_car():
  return {
    'city': 'Toronto',
    'passengers': 0,
    'gas': 100,
  }

def add_car(cars, new_car):
  cars.append(new_car)
  return "Adding new car to fleet. Fleet size is now {}.".format(len(cars))

def pick_up_passenger(car):
  car['passengers'] += 1
  car['gas'] -= 10
  return "Picked up passenger. Car now has {} passengers.".format(car['passengers'])

def get_destination(car):
  if car['city'] == 'Toronto':
    return 'Mississauga'
  elif car['city'] == 'Mississauga':
    return 'London'
  elif car['city'] == 'London':
    return 'Toronto'

def fill_up_gas(car):
  old_gas = car['gas']
  car['gas'] = 100
  return "Filled up to {} on gas from {}.".format( get_gas_display(car['gas']), get_gas_display(old_gas) )

def get_gas_display(gas_amount):
  return "{}%".format(gas_amount)

def drive(car, city_distance):
  if car['gas'] < city_distance:
    return fill_up_gas(car)

  car['city'] = get_destination(car)
  car['gas'] -= city_distance
  return "Drove to {}. Remaining gas: {}.".format(car['city'], get_gas_display(car['gas']))

def drop_off_passengers(car):
  previous_passengers = car['passengers']
  car['passengers'] = 0
  return "Dropped off {} passengers.".format(previous_passengers)

def act(car):
  distance_between_cities = 50

  if car['gas'] < 20:
    return fill_up_gas(car)
  elif car['passengers'] < 3:
    return pick_up_passenger(car)
  else:
    if car['gas'] < distance_between_cities:
      return fill_up_gas(car)

    drove_to = drive(car, distance_between_cities)
    passengers_dropped = drop_off_passengers(car)
    return "{} {}".format(drove_to, passengers_dropped)

def command_fleet(cars):
  i = 1
  for car in cars:
    action = act(car)
    print("Car {}: {}".format(i, action))
    i += 1

  print('---')

def add_one_car_per_day(cars, num_days):
  for day in range(0, num_days):
    new_car = get_new_car()
    print(add_car(cars, new_car))
    command_fleet(cars)

cars = []
add_one_car_per_day(cars, 10)

# what we want to see in the console: 
# Adding new car to fleet. Fleet size is now 1.
# Car 1: Picked up passenger. Car now has 1 passengers.
# ---
# Adding new car to fleet. Fleet size is now 2.
# Car 1: Picked up passenger. Car now has 2 passengers.
# Car 2: Picked up passenger. Car now has 1 passengers.
# ---
# Adding new car to fleet. Fleet size is now 3.
# Car 1: Picked up passenger. Car now has 3 passengers.
# Car 2: Picked up passenger. Car now has 2 passengers.
# Car 3: Picked up passenger. Car now has 1 passengers.
# ---
# Adding new car to fleet. Fleet size is now 4.
# Car 1: Drove to Mississauga. Remaining gas: 20%. Dropped off 3 passengers.
# Car 2: Picked up passenger. Car now has 3 passengers.
# Car 3: Picked up passenger. Car now has 2 passengers.
# Car 4: Picked up passenger. Car now has 1 passengers.
# ---
# Adding new car to fleet. Fleet size is now 5.
# Car 1: Picked up passenger. Car now has 1 passengers.
# Car 2: Drove to Mississauga. Remaining gas: 20%. Dropped off 3 passengers.
# Car 3: Picked up passenger. Car now has 3 passengers.
# Car 4: Picked up passenger. Car now has 2 passengers.
# Car 5: Picked up passenger. Car now has 1 passengers.
# ---
# Adding new car to fleet. Fleet size is now 6.
# Car 1: Filled up to 100% on gas from 10%.
# Car 2: Picked up passenger. Car now has 1 passengers.
# Car 3: Drove to Mississauga. Remaining gas: 20%. Dropped off 3 passengers.
# Car 4: Picked up passenger. Car now has 3 passengers.
# Car 5: Picked up passenger. Car now has 2 passengers.
# Car 6: Picked up passenger. Car now has 1 passengers.
# ---
# Adding new car to fleet. Fleet size is now 7.
# Car 1: Picked up passenger. Car now has 2 passengers.
# Car 2: Filled up to 100% on gas from 10%.
# Car 3: Picked up passenger. Car now has 1 passengers.
# Car 4: Drove to Mississauga. Remaining gas: 20%. Dropped off 3 passengers.
# Car 5: Picked up passenger. Car now has 3 passengers.
# Car 6: Picked up passenger. Car now has 2 passengers.
# Car 7: Picked up passenger. Car now has 1 passengers.
# ---
# Adding new car to fleet. Fleet size is now 8.
# Car 1: Picked up passenger. Car now has 3 passengers.
# Car 2: Picked up passenger. Car now has 2 passengers.
# Car 3: Filled up to 100% on gas from 10%.
# Car 4: Picked up passenger. Car now has 1 passengers.
# Car 5: Drove to Mississauga. Remaining gas: 20%. Dropped off 3 passengers.
# Car 6: Picked up passenger. Car now has 3 passengers.
# Car 7: Picked up passenger. Car now has 2 passengers.
# Car 8: Picked up passenger. Car now has 1 passengers.
# ---
# Adding new car to fleet. Fleet size is now 9.
# Car 1: Drove to London. Remaining gas: 30%. Dropped off 3 passengers.
# Car 2: Picked up passenger. Car now has 3 passengers.
# Car 3: Picked up passenger. Car now has 2 passengers.
# Car 4: Filled up to 100% on gas from 10%.
# Car 5: Picked up passenger. Car now has 1 passengers.
# Car 6: Drove to Mississauga. Remaining gas: 20%. Dropped off 3 passengers.
# Car 7: Picked up passenger. Car now has 3 passengers.
# Car 8: Picked up passenger. Car now has 2 passengers.
# Car 9: Picked up passenger. Car now has 1 passengers.
# ---
# Adding new car to fleet. Fleet size is now 10.
# Car 1: Picked up passenger. Car now has 1 passengers.
# Car 2: Drove to London. Remaining gas: 30%. Dropped off 3 passengers.
# Car 3: Picked up passenger. Car now has 3 passengers.
# Car 4: Picked up passenger. Car now has 2 passengers.
# Car 5: Filled up to 100% on gas from 10%.
# Car 6: Picked up passenger. Car now has 1 passengers.
# Car 7: Drove to Mississauga. Remaining gas: 20%. Dropped off 3 passengers.
# Car 8: Picked up passenger. Car now has 3 passengers.
# Car 9: Picked up passenger. Car now has 2 passengers.
# Car 10: Picked up passenger. Car now has 1 passengers.
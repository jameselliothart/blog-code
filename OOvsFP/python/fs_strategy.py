from functools import partial

def car_strategy(source, destination): return 40

def bike_strategy(source, destination): return 25

def bus_strategy(source, destination): return 60

def get_travel_time(strategy, source, destination):
    result = strategy(source, destination)
    return f'It takes {result} minutes to go from {source} to {destination}'

if __name__ == '__main__':
    print("Please select the mode of transport: \nCar \nBike \nBus")
    userStrategy = input().lower()
    print("\nUser has selected *" + userStrategy + "* as mode of transport\n")
    print("\n*****************************************************************************************************\n")
    calculators = {
        "car"  : partial(get_travel_time, car_strategy),
        "bike" : partial(get_travel_time, bike_strategy),
        "bus"  : partial(get_travel_time, bus_strategy)
    }
    timeBetween = calculators.get(userStrategy)
    if timeBetween: print(timeBetween("Point A", "Point B"))
    else: print("You have chosen an invalid mode of transport.")

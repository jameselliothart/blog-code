class CarStrategy():
    def get_travel_time(self, source, destination): return 40

class BikeStrategy():
    def get_travel_time(self, source, destination): return 25

class BusStrategy():
    def get_travel_time(self, source, destination): return 60

class Trip():
    def __init__(self, strategy):
        self._strategy = strategy

    def get_travel_time(self, source, destination):
        result = self._strategy.get_travel_time(source, destination)
        return f'It takes {result} minutes to go from {source} to {destination}'

if __name__ == '__main__':
    print("Please select the mode of transport: \nCar \nBike \nBus")
    userStrategy = input().lower()
    print("\nUser has selected *" + userStrategy + "* as mode of transport\n")
    print("\n*****************************************************************************************************\n")
    calculators = {
        "car"  : Trip(CarStrategy()),
        "bike" : Trip(BikeStrategy()),
        "bus"  : Trip(BusStrategy())
    }
    timeBetween = calculators.get(userStrategy)
    if timeBetween: print(timeBetween.get_travel_time("Point A", "Point B"))
    else: print("You have chosen an invalid mode of transport.")

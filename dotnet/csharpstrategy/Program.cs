using System;

namespace csharpstrategy
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Please select the mode of transport: \nCar \nBike \nBus");
            var userStrategy = Console.ReadLine().ToLower();
            Console.WriteLine("\nUser has selected *" + userStrategy + "* as mode of transport\n");
            Console.WriteLine("\n*****************************************************************************************************\n");
            switch (userStrategy) {
                case "car":
                    new Trip(new CarStrategy()).GetTravelTime("Point A", "Point B");
                    break;
                case "bike":
                    new Trip(new BikeStrategy()).GetTravelTime("Point A", "Point B");
                    break;
                case "bus":
                    new Trip(new BusStrategy()).GetTravelTime("Point A", "Point B");
                    break;
                default:
                    Console.WriteLine("You have chosen an invalid mode of transport.");
                    break;
            }
        }
    }
}

namespace csharpstrategy
{
    public class CarStrategy: ITravelStrategy
    {
        public string GetTravelTime(string source, string destination) =>
            "It takes 40 minutes to reach from " + source + " to " + destination + " using Car.";
    }
    public class BikeStrategy: ITravelStrategy
    {
        public string GetTravelTime(string source, string destination) =>
            "It takes 25 minutes to reach from " + source + " to " + destination + " using Bike.";
    }
    public class BusStrategy: ITravelStrategy
    {
        public string GetTravelTime(string source, string destination) =>
            "It takes 60 minutes to reach from " + source + " to " + destination + " using Bus.";
    }
}
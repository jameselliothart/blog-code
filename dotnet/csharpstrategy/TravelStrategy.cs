namespace csharpstrategy
{
    public class CarStrategy: ITravelStrategy
    {
        public int GetTravelTime(string source, string destination) => 40;
    }
    public class BikeStrategy: ITravelStrategy
    {
        public int GetTravelTime(string source, string destination) => 25;
    }
    public class BusStrategy: ITravelStrategy
    {
        public int GetTravelTime(string source, string destination) => 60;
    }
}
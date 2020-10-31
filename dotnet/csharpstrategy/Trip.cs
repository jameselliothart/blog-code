using System;

namespace csharpstrategy
{
    public class Trip
    {
        private ITravelStrategy _strategy;

        public Trip(ITravelStrategy chosenStrategy)
        {
            _strategy = chosenStrategy;
        }

        public void GetTravelTime(string source, string destination)
        {
            var result = _strategy.GetTravelTime(source, destination);
            Console.WriteLine(result);
        }
    }
}
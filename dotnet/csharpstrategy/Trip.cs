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

        public string GetTravelTime(string source, string destination)
        {
            var result = _strategy.GetTravelTime(source, destination);
            return $"It takes {result} minutes to go from {source} to {destination}";
        }
    }
}
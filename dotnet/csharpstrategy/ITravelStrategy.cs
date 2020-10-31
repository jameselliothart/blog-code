namespace csharpstrategy
{
    public interface ITravelStrategy
    {
        string GetTravelTime(string source, string destination);
    }
}
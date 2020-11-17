namespace csharpstrategy
{
    public interface ITravelStrategy
    {
        int GetTravelTime(string source, string destination);
    }
}
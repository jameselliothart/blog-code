// Learn more about F# at http://fsharp.org

open System

[<EntryPoint>]
let main argv =
    Console.WriteLine("Please select the mode of transport: \nCar \nBike \nBus");
    let userStrategy = Console.ReadLine().ToLower();
    Console.WriteLine("\nUser has selected *" + userStrategy + "* as mode of transport\n");
    Console.WriteLine("\n*****************************************************************************************************\n");
    let travelTimeBetween =
        match userStrategy with
        | "car" ->
            Trip.getTravelTime TravelStrategy.carStrategy
        | "bike" ->
            Trip.getTravelTime TravelStrategy.bikeStrategy
        | "bus" ->
            Trip.getTravelTime TravelStrategy.busStrategy
        | _ ->
            fun _ _ -> sprintf "You have chosen an invalid mode of transport."
    travelTimeBetween "Point A" "Point B" |> Console.WriteLine
    0 // return an integer exit code

module Trip

let getTravelTime strategy source destination =
    let time = strategy source destination
    sprintf "It takes %i minutes to go from %s to %s" time source destination

func canCompleteCircuit(gas []int, cost []int) int {
    if sum(gas) < sum(cost){
        return -1
    }

    res := 0
    total := 0

    for i := 0; i < len(gas); i++{
        total += gas[i] - cost[i]
        if total < 0{
            total = 0
            res = i + 1
        }

    }
    return res
}

func sum(array []int) int{
    s := 0
    for _,v := range array{
        s += v
    }
    return s
}

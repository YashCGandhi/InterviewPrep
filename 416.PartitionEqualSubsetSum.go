func canPartition(nums []int) bool {
    sum := sum(nums)
    if sum % 2 != 0{
        return false
    }
    target := sum / 2
    set := make(map[int]bool)
    set[0] = true
    for _,i := range nums{
        nextSet := make(map[int]bool)
        for s := range set{
            if (s + i) == target{
                return true
            }
            nextSet[s] = true
            nextSet[s + i] = true
        }
        set = nextSet
    }

    return false
}

func sum(nums []int) int{
    res := 0
    for _, i := range nums{
        res += i
    }
    return res
}

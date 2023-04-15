func jump(nums []int) int {
    res := 0
    l := 0
    r := 0

    for r < len(nums) - 1{
        farthest := 0
        for i := l; i < r + 1; i++{
            farthest = max(farthest, i + nums[i])
        }
        l = r + 1
        r = farthest
        res += 1
    }
    
    return res
}

func max(a, b int) int{
    if a > b{
        return a
    }
    return b
}

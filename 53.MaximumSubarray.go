func maxSubArray(nums []int) int {
    res := nums[0]
    curSum := nums[0]

    for i := 1; i < len(nums);i++{
        if curSum < 0{
            curSum = 0
        }
        curSum += nums[i]
        res = max(res, curSum)
    }
    return res
}

func max(a, b int) int{
    if a > b{
        return a
    }
    return b
}

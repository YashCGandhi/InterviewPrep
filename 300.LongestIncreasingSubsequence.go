func lengthOfLIS(nums []int) int {
    dp := make([]int, len(nums))
    res := 1
    for x := 0; x < len(nums); x++{
        dp[x] = 1
    }
     for i := range nums{
         curMax := 0
         for j := 0; j < i + 1; j++{
             if nums[j] < nums[i]{
                 curMax = max(curMax,dp[j])
             }
         }
         dp[i] = 1 + curMax
         res = max(dp[i], res)
     }

    return res
}

func max(a, b int) int{
    if a > b{
        return a
    } else{
        return b
    }
}

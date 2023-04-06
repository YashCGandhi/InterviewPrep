func coinChange(coins []int, amount int) int {
    dp := make([]int, amount + 1)
    for i := 0; i < len(dp); i++{
        dp[i] = amount + 1
    }
    dp[0] = 0

    for i := 0; i < len(dp); i++{
        for _,c := range coins{
            if i - c >= 0{
                dp[i] = min(dp[i], 1 + dp[i - c])
            }
        }
    }

    if dp[amount] < amount + 1{
        return dp[amount]
    }

    return -1
}

func min(a, b int) int{
    if a < b{
        return a
    } else{
        return b
    }
}

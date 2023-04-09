func wordBreak(s string, wordDict []string) bool {
    dp := make([]bool, len(s) + 1)
    dp[len(s)] = true

    for i := len(s) - 1; i >= 0; i--{
        for _,w := range wordDict{
            if i + len(w) <= len(s) && w == s[i : i + len(w)]{
                dp[i] = dp[i + len(w)]
            }
            if dp[i] == true{
                break
            }
        }
    }
    return dp[0]

}

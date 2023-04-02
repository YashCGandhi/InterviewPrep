func rob(nums []int) int {
  n := len(nums)

  if n == 1{
    return nums[0]
  }

  if n == 2{
    return max(nums[0], nums[1])
  }


  return max(houseRobber(nums, 0, n - 1), houseRobber(nums, 1, n))
}

func houseRobber(money []int, s int, e int) int{
  rob1, rob2 := 0, 0

  for i := s; i < e; i++{
    newRob := max(rob1 + money[i], rob2)
    rob1 = rob2
    rob2 = newRob
  }
  return rob2
}

func max(a, b int) int{
  if a > b{
    return a
  } else {
    return b
  }
}

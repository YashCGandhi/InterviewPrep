func quickSelect(l int, r int, k int, nums []int) int{
    pivot, p := nums[r], l

    for i := l; i < r; i++{
        if nums[i] <= pivot{
            tmp := nums[i]
            nums[i] = nums[p]
            nums[p] = tmp
            p++
        }
    }
    tmp := nums[r]
    nums[r] = nums[p]
    nums[p] = tmp

    if p < k{
        return quickSelect(p + 1, r, k, nums)
    }else if p > k{
        return quickSelect(l, p - 1, k, nums)
    }else{
        return nums[p]
    }

}

func findKthLargest(nums []int, k int) int {
    k = len(nums) - k
    return quickSelect(0, len(nums) - 1, k, nums)
}

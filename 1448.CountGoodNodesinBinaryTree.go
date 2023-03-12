func goodNodes(root *TreeNode) int {
    return recur(root, math.MinInt)
}

func recur(root *TreeNode, curMax int) int{
    if root == nil{
        return 0
    }

    res := 0
    

    if root.Val >= curMax{
        res++
        curMax = root.Val
    }

    res += recur(root.Left, curMax)
    res += recur(root.Right, curMax)

    return res
}

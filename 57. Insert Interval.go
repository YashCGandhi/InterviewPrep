func insert(intervals [][]int, newInterval []int) [][]int {
    output := [][]int{}

    for i, val := range intervals{
        newIntStart, newIntEnd := newInterval[0], newInterval[1]
        currStart, currEnd := val[0], val[1]

        if newIntEnd < currStart{
            output = append(output, newInterval)

            output = append(output, intervals[i:]...)
            return output
        }else if newIntStart > currEnd{
            output = append(output, intervals[i])
        }else{
            newInterval[0] = min(newIntStart, currStart)
            newInterval[1] = max(newIntEnd, currEnd)
        }
    }

    output = append(output, newInterval)
    return output
}

func min(a, b int) int {
	if a > b {
		return b
	}
	return a
}

func max(a, b int) int {
	if a > b {
		return a
	}
	return b
}

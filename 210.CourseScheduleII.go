func findOrder(numCourses int, prerequisites [][]int) []int {
    preMap := make([][]int, 0)
    for i := 0; i< numCourses; i++{
        preMap = append(preMap, make([]int,0)) 
    }

    for _,edge := range prerequisites{
        preMap[edge[0]] = append(preMap[edge[0]], edge[1])
    }

    output := make([]int, 0)
    visit, cycle := make([]bool,numCourses),make([]bool,numCourses)

    var dfs func(int) bool
    dfs = func(crs int) bool{
        if cycle[crs]{
            return false
        }else if visit[crs]{
            return true
        }

        cycle[crs] = true
        for _,pre := range preMap[crs]{
            if !dfs(pre){
                return false
            }
        }
        cycle[crs] = false
        visit[crs] = true
        output = append(output, crs)
        return true
    }

    for i := 0;i < numCourses; i++{
        if !dfs(i){
            return make([]int, 0)
        }
    }
    return output
}

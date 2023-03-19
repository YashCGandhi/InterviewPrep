func canFinish(numCourses int, prerequisites [][]int) bool {
    preMap := make(map[int][]int)

    for _,prerq := range prerequisites{
        preMap[prerq[1]] =  append(preMap[prerq[1]], prerq[0])
    }

    visit := make(map[int]struct{})

    var dfs func(int) bool
    dfs = func( crs int) bool{
        if _,ok := visit[crs]; ok{
            return false
        }

        if len(preMap[crs]) == 0{
            return true
        }

        visit[crs] = struct{}{}

        for _,pre := range preMap[crs]{
            if !dfs(pre){
                return false
            }
        }

        delete(visit, crs)
        preMap[crs] = []int{}
        return true
    }

    for i := 0; i < numCourses ; i++ {
        if !dfs(i){
            return false
        }
    }
    return true
}

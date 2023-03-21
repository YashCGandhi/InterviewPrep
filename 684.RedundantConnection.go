func findRedundantConnection(edges [][]int) []int {
    n := len(edges)
    par := make( []int, n + 1)
    rank := make( []int, n + 1)

    
    find := func(node int) int {
        p := par[node]
        for p != par[p]{
            par[p] = par[par[p]]
            p = par[p]
        }
        return p
    }

    
    union := func(node1 int, node2 int) bool{
        p1, p2 := find(node1), find(node2)

        if p1 == p2{
            return false
        }

        if rank[p1] > rank[p2]{
            par[p2] = p1
            rank[p1] += rank[p2]
        }else{
            par[p1] = p2
            rank[p2] += rank[p1]
        }
        return true
    }

    for i := 0; i < n + 1; i++{
        par[i] = i
        rank[i] = 1
    }

    for _, edge := range edges{
        n1, n2 := edge[0],edge[1]
        if union(n1, n2) == false{
            return edge
        }
        
    }

    return []int{}
}

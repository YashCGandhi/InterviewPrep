type point struct{
    i, j int
}

func wallsAndGates(rooms [][]int)  {
    q := make([]point, 0)
    for i := range rooms{
        for j:= range rooms[i]{
            if rooms[i][j] == 0{
                q = append(q, point{i, j})
            }
        }
    }

    for len(q) > 0{
        from := q[0]
        q = q[1:]

        for _,act := range []point{{1,0}, {-1,0}, {0,1}, {0,-1}}{
            to := point{i:from.i + act.i, j:from.j + act.j}
            if to.i < 0 || to.i >= len(rooms) || to.j < 0 || to.j >= len(rooms[0]){
                continue
            }
            if rooms[to.i][to.j] == math.MaxInt32{
                rooms[to.i][to.j] = 1 + rooms[from.i][from.j]
                q = append(q, to)
            }
        }
    }
}

func mergeTriplets(triplets [][]int, target []int) bool {
    flags := make([]bool, len(target))

    for _,t := range triplets{
        if t[0] > target[0] || t[1] > target[1] || t[2] > target[2]{
            continue
        }

        for i,v := range t{
            if v == target[i]{
                flags[i] = true
            }
        }
        cnt := 0
        for _,f := range flags{
            if f == true{
                cnt++
            }
        }
        if cnt == 3{
            return true
        }
        
    }
    return false
}

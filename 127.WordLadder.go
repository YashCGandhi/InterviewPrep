func ladderLength(beginWord string, endWord string, wordList []string) int {
    if !contains(wordList, endWord){
        return 0
    }

    patterns := make(map[string][]string)
    wordList = append(wordList, beginWord)

    for _, word := range wordList{
        for j := 0; j < len(word); j++{
            pattern := word[:j] + "*" + word[j+1:]
            patterns[pattern] = append(patterns[pattern], word)
        }
    }

    visit := map[string]bool{beginWord:true}
    q := []string{beginWord}
    res := 1

    for len(q) != 0{
        cnt := len(q)
        for i := 0; i < cnt ; i++{
            word := q[0]
            q = q[1:]
            if word == endWord{
                
                return res
            }
            for j := 0; j < len(word); j++{
                pattern := word[:j] + "*" + word[j+1:]
                for _,nei := range patterns[pattern]{
                    if !visit[nei]{
                        visit[nei] = true
                        q = append(q, nei)
                    }
                }
            }
        
        }
        res++
    }

    return 0
}

func contains(s []string, word string) bool{
    for _,w := range s{
        if w == word{
            return true
        }
    }
    return false
}

"""
Intuition is that for every two points calculate the eqn for that line and use it as a key for hash table to store all he other points that fall on that line
"""

class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        res = 1
        for i in range(len(points)):
            dict_slope = defaultdict(int)
            for j in range(i + 1, len(points)):
                if points[j][0] - points[i][0] == 0:
                    slope = 'INF'
                else:
                    slope = (points[j][1] - points[i][1])/(points[j][0] - points[i][0])
                dict_slope[slope] += 1
            for i in dict_slope:
                res = max(res, dict_slope[i] + 1)
        
        return res

"""
Has problem with slope='INF'
Cause: slope = 'inf' happens when x2 = x1 which causes the denominator to go to 0. When you have a global hashmap where you store all the points for a key value(slope), all the slope='inf' points will go together even though their x-coordinates are not the same. Hence use the method above, where a new hashmap in initialized for every i.
testcase : points = [[3,3],[1,4],[1,1],[2,1],[2,2]]

        if len(points) == 1:
            return 1
        res = 1
        dict_slopes = defaultdict(list)
        for i in range(len(points) - 1):
            for j in range(i + 1, len(points)):
                if points[j][0] - points[i][0] == 0:
                    slope = 'INF'
                else:
                    slope = (points[j][1] - points[i][1])/(points[j][0] - points[i][0])
                if points[i] not in dict_slopes[slope]:
                    dict_slopes[slope].append(points[i])
                if points[j] not in dict_slopes[slope]:
                    dict_slopes[slope].append(points[j])
        for i in dict_slopes:
            res = max(res, len(dict_slopes[i]))
        print(dict_slopes)
        return res
"""           

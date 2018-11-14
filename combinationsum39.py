"""
class Solution {
public:
    void dfs(vector<int> &a, int now, int sum, int target, vector<int> &path, vector<vector<int>> &answer){
        if(sum > target){
            return;
        }
        if (now >= a.size()){
            if (sum ==target){
                answer.push_back(path);
            }
            return;
        }
        if ((now == 0) ||(a[now-1] != a[now])){
            path.push_back(a[now]);
            dfs(a,now,sum+a[now],target,path, answer);
            path.pop_back();
        }
        dfs(a,now+1,sum,target,path, answer);
    }
    vector<vector<int>> combinationSum(vector<int>& candidates, int target) {
        sort(candidates.begin(), candidates.end());
        vector<int> path;
        vector<vector<int>> answer;
        dfs(candidates, 0,0, target, path, answer);
        return answer;
    }
};
"""


class Solution():
    def dfs(self, a, now, suma, target, path, answer):
        if suma > target:
            return
        if now >= len(a):
            if target == suma:
                answer.append(path[:])
            return
        if ((now == 0) or (a[now-1]!=a[now])):
            path.append(a[now])
            self.dfs(a, now, suma+a[now],target,path,answer)
            path.pop()
        self.dfs(a,now+1,suma,target,path, answer)
        return
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        path = []
        answer = []
        candidates.sort()
        self.dfs(candidates,0,0,target,path,answer)
        return answer

test = Solution()
print(test.combinationSum([2,3,6,7],7))
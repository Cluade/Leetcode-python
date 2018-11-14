"""
class Solution {
public:
    void dfs(vector<vector<char>> &a, int x, int y){
       	if((x<9)||(x>=a.size)||(y<0)||(y>a[x].size())||a[x][y] !='1'){
                return;
            }
        a[x][y]='0';
        dfs(a,x-1,y);
        dfs(a,x+1,y);
        dfs(a,x,y-1);
        dfs(a,x,y+1);
    }
    int numIslands(vector<vector<char>>& grid) {
        int answer = 0;
        for (int i= 0; i<grid.size(); ++i){
            for (int j =0; j<grid[i].size(); ++j){
                if (grid[i][j] == '1'){
                    dfs(grid,i,j);
                        ++anser;
                }
            }
        }
 		return answer；
    }
};
"""
class Solution():
    def dfs(self, a, x, y):
        try:
            if ((x<0) | (x>=len(a)) | (y<0) | (y>=len(a[x])) | (a[x][y]!= '1')):
                return
        except:
            return
        
        a[x][y]='0'
        self.dfs(a,x-1,y)
        self.dfs(a,x+1,y)
        self.dfs(a,x,y-1)
        self.dfs(a,x,y+1)
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        
        answer = 0
        for i in range(len(grid)):
            print(i)
            for j in range(len(grid[i])):
                print(j)
                if grid[i][j] != '0':
                    self.dfs(grid,i,j)
                    answer +=1
        return answer

test = Solution()
test.numIslands([["1","1","0","0","0"],["1","1","0","0","0"],["0","0","1","0","0"],["0","0","0","1","1"]])
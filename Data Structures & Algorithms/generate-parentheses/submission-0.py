class Solution:

    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def dfs(s, open_count, close_count):
            if len(s) == 2 * n:
                res.append("".join(s[:]))
                return
            
            if open_count < n:
                s.append("(")
                dfs(s, open_count + 1, close_count)
                s.pop()
            if close_count < open_count:
                s.append(")")
                dfs(s, open_count, close_count + 1)
                s.pop()
            
        dfs([], 0, 0)
        
        return res
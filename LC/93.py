class Solution(object):
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        res = []
        self.helper(s, 4, [], res)
        return res

    def helper(self, s, n, path, res):
        if len(s) > n * 3 or len(s) < n:
            return
        if n == 1:
            if (len(s) > 1 and int(s) < 256 and s[0] != '0') or (len(s) == 1):
                res.append('.'.join(path + [s]))
                return
            else:
                return
        for i in [1,2,3]:
            if (n - 1) * 1 <= len(s) - i <= (n - 1) * 3:

                if i > 1 and s[0] == '0':
                    i += 1
                    continue
                if int(s[:i]) < 256:
                    self.helper(s[i:], n - 1, path + [s[:i]], res)
                i += 1

print(Solution().restoreIpAddresses("19216811"))
class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """

        # i and j are the pointers to the char that we are going to check,
        # if i and j reach their ends simultaneously, the two strings are matched.
        
        # next_try stores a position(coordinates) to record the position of last star 
        # (plus one, so that it can be the 'next' 'try') and corresponding j.
        
        # next_try can be seen as another possible starting point to check the two strings.
        # next_try is updated when we meet a new '*'. We only care about the last '*' because
        # the last '*' means that we have already matched as much as we can for p and the last
        # '*' can cover any string so we can throw away the previous next_try values and start
        # from here. We're greedy.
        
        i, j, next_try =  0, 0, None
        
        while 1:
            
            # Quick judge by length of string: if len(p w/o '*') is bigger than len(s), return False
            if len(p)-p.count('*')>len(s):
                return False
            
            # check if i outbounds p
            if i >= len(p):
                # both i and j reaches end of their strings simultaneously
                if j >= len(s):
                    return True
                # go to next_try
                if next_try:
                    i, j = next_try
                    if j>=len(s):
                        # no more try
                        return False
                    else:
                        j+=1
                        next_try = [i,j]
                else:
                    # if there is no next_try (None), return False
                    return False
            else:
                # check if '*'
                if p[i] != '*':
                    # not '*', we compare the two chars if exist else return False
                    if j>=len(s):
                        # see if there is next_try (update it first)
                        if next_try:
                            i, j = next_try
                            if j>=len(s):
                                # cannot update next_try since it's over limit
                                return False
                            else:
                                j+=1
                                next_try = [i,j]
                        else:
                            # if not next_try available, return False
                            return False
                    else:    
                        # j<len(s), we can compare the two chars
                        if (p[i]=='?') or (p[i]==s[j]):
                            i+=1
                            j+=1
                        else:
                            # if chars are not equal, we need to test next_try (update it first)
                            if next_try:
                                next_try=[next_try[0],next_try[1]+1]
                                i, j = next_try
                            else:
                                # if not next_try available, return False
                                return False
                else:
                    # '*', we need to update branch coordinates for next_try
                    next_try = [i+1, j]
                    i, j = next_try
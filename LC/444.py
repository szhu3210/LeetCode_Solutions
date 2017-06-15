class Solution(object):
    def sequenceReconstruction(self, org, seqs):
        """
        :type org: List[int]
        :type seqs: List[List[int]]
        :rtype: bool
        """
        index = {num: i for i, num in enumerate([None] + org)}
        pairs = set(zip([None] + org, org))
        for seq in seqs:
            for a, b in zip([None] + seq, seq):
                if index[a] >= index.get(b, 0):
                    return False
                pairs.discard((a, b))
        return not pairs
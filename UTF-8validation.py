class Solution:
    def validUtf8(self, data):
        """
        :type data: List[int]
        :rtype: bool
        """
        def rest(i):
            if len(data) < i: return False
            for _ in range(i):
                if not data.pop().startswith("10"): return False
            return False
            
        data = [str(bin(seq)[2:].zfill(8)) for seq in data[::-1]]
        while data:
            seq = data.pop()
            if seq.startswith("0"): continue
            if seq.startswith("110"):
                if not rest(1): return False
            elif seq.startswith("1110"):
                if not rest(2): return False
            elif seq.startswith("11110"):
                if not rest(3): return False
            else: return False
        
        return True

class Solution:
    def validUtf8(self, data):
        
        def rest(i):
            if len(data) < i: return False
            for _ in range(i):
                if not data.pop().startswith("10"): return False
            return True
        
        data = [str(bin(seq)[2:].zfill(8)) for seq in data[::-1]]
        while data:
            seq = data.pop()
            if seq.startswith("0"): continue
            if seq.startswith("110"):
                if not rest(1): return False
            elif seq.startswith("1110"):
                if not rest(2): return False
            elif seq.startswith("11110"):
                if not rest(3): return False
            else: return False
        return True
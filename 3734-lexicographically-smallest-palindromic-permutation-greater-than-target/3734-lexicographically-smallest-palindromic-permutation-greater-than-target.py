class Solution:
    def lexPalindromicPermutation(self, s: str, target: str) -> str:
        from collections import Counter
        
        cnt = Counter(s)
        odd_char = ""
        freq = [0] * 26
        
        for char, count in cnt.items():
            if count % 2 != 0:
                if odd_char != "": 
                    return "" 
                odd_char = char
            freq[ord(char) - 97] = count // 2
            
        M = len(s) // 2
        
        matched_len = 0
        curr_freq = list(freq)
        for i in range(min(M, len(target))):
            idx = ord(target[i]) - 97
            if curr_freq[idx] > 0:
                curr_freq[idx] -= 1
                matched_len += 1
            else:
                break
                
        for i in range(matched_len, -1, -1):
            avail = list(freq)
            for j in range(i):
                avail[ord(target[j]) - 97] -= 1
                
            if i == M:
                half = target[:M]
                cand = half + odd_char + half[::-1]
                if cand > target:
                    return cand
            else:
                target_char = target[i] if i < len(target) else chr(0)
                best_c = ""
                
                for c_idx in range(26):
                    c = chr(c_idx + 97)
                    if avail[c_idx] > 0 and c > target_char:
                        best_c = c
                        break
                        
                if best_c != "":
                    avail[ord(best_c) - 97] -= 1
                    
                    rest = []
                    for c_idx in range(26):
                        if avail[c_idx] > 0:
                            rest.append(chr(c_idx + 97) * avail[c_idx])
                    
                    half = target[:i] + best_c + "".join(rest)
                    return half + odd_char + half[::-1]
                    
        return ""
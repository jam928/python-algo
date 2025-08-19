from typing import List

# https://leetcode.com/problems/restore-ip-addresses
# T:O(3^N)
# S:O(1)

class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        result = []
        def helper(i, current_list):
            
            if i == len(s) and len(current_list) == 4:
                result_str = '.'.join(current_list)
                result.append(result_str)
                return
            
            if len(current_list) >= 4:
                return
            
            for len_ in range(1, 4):
                if i + len_ > len(s):
                    break
                part = s[i:i+len_]

                if len(part) > 1 and part[0] == '0' or int(part) > 255:
                    continue
                    
                current_list.append(part)
                helper(i+len_, current_list)
                current_list.pop()

        helper(0, [])

        return result
    
if __name__ == '__main__':
    s = Solution()
    assert s.restoreIpAddresses("25525511135") == ["255.255.11.135","255.255.111.35"]
    assert s.restoreIpAddresses("0000") == ["0.0.0.0"]
    assert s.restoreIpAddresses("101023") == ["1.0.10.23","1.0.102.3","10.1.0.23","10.10.2.3","101.0.2.3"]
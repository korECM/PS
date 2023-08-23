from typing import List


class Solution:
    def validUtf8(self, data: List[int]) -> bool:

        def check(s_bin: list[str]):
            if len(s_bin) >= 1 and s_bin[0][:1] == '0':
                return True, 1
            elif len(s_bin) >= 2 and s_bin[0][:3] == '110' and s_bin[1][:2] == '10':
                return True, 2
            elif len(s_bin) >= 3 and s_bin[0][:4] == '1110' and s_bin[1][:2] == '10' and s_bin[2][:2] == '10':
                return True, 3
            elif len(s_bin) >= 4 and (s_bin[0][:5] == '11110' and s_bin[1][:2] == '10' and s_bin[2][:2] == '10'
                  and s_bin[3][:2] == '10'):
                return True, 4
            return False, -1

        bin_str = [bin(s)[2:].zfill(8) for s in data]
        index = 0
        while bin_str[index:]:
            success, length = check(bin_str[index:])
            if success:
                index += length
            else:
                return False
        return True

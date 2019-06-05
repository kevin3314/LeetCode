class Solution:
    def myAtoi(self, s: str) -> int:
        numbers = set(('1','2','3','4','5','6','7','8','9','0','-', '+'))
        is_first_char_passed = False
        number_str = []
        s = s.strip()
        for c in s:
            if (c == '-' or c == '+') and is_first_char_passed is True:
                break
            elif c in numbers:
                number_str.append(c)
                is_first_char_passed = True
            else:
                break

        if number_str == [] or number_str == ['-'] or number_str == ['+']:
            return 0
        if int(''.join(number_str)) >= 2147483648:
            return 2147483647
        elif int(''.join(number_str)) < -2147483648:
            return -2147483648
        return int(''.join(number_str))

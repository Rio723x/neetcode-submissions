class Solution:
    def isValid(self, s: str) -> bool:

        res_list = []

        for ch in s:

            if ch == '(' or ch == '[' or ch == '{':
                res_list.append(ch)

            else:

                if len(res_list) == 0:
                    return False

                if ch == ')' and res_list[-1] == '(':
                    res_list.pop()

                elif ch == ']' and res_list[-1] == '[':
                    res_list.pop()

                elif ch == '}' and res_list[-1] == '{':
                    res_list.pop()

                else:
                    return False

        return len(res_list) == 0

        
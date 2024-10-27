# parsing_a_boolean_expression_1106
# https://leetcode.com/problems/parsing-a-boolean-expression/description/?envType=daily-question&envId=2024-10-20

class Solution:
    def parseBoolExpr(self, expression: str) -> bool:
        s = expression
        i = 0

        def helper():    
            nonlocal i
            c = s[i]
            i += 1

            if c == "t":
                return True
            if c == "f":
                return False
            if c == "!":
                i+=1
                result = not helper()
                i+=1
                return result
            
            children = []
            i+=1
            while s[i] != ")":
                if s[i] != ",":
                    children.append(helper())
                else:
                    i+=1
                
            i+=1
            if c == "&":
                return all(children)
            if c == "|":
                return any(children)
            

        return helper()
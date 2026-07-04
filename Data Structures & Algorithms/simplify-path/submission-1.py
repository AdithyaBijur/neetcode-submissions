class Solution:
    def simplifyPath(self, path: str) -> str:
        s = path.split("/")
        # print(stack)

        cleaned = []
        for i in s:
            if i != "":
                cleaned.append(i)
        
        stack = []

        for i in cleaned:
            if i == ".":
                continue
            if i == "..":
                if stack:
                    stack.pop()
            else:
                stack.append(i)
        
        return '/' + '/'.join(stack)

        
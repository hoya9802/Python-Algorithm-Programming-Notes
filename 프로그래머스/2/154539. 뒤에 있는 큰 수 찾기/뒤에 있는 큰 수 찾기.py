# solve 9

def solution(numbers):
    ans = [-1] * len(numbers)
    stack = []
    for i in range(len(numbers)-1,-1,-1):
        while stack and numbers[i] >= stack[-1]:
            stack.pop()
        if stack:
            ans[i] = stack[-1]
        stack.append(numbers[i])
    return ans
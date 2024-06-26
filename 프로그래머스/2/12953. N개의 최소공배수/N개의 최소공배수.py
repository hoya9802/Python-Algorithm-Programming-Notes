# solve 13
def gcd(n, m):
    if m == 0:
        return n
    return gcd(m, n%m)

def solution(arr):
    ans = arr[0]
    for i in arr:
        ans = ans * i // gcd(ans, i)
    return ans
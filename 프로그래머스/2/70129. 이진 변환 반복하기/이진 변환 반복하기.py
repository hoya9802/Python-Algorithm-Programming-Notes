def solution(s):
    answer = [0,0]
    while s != '1':
        answer[0] += 1
        answer[1] += len(s) - s.count('1')
        s = bin(s.count('1'))[2:]
    return answer
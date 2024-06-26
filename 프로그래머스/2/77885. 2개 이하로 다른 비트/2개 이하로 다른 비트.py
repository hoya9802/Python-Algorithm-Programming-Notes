def solution(numbers):
    answer = []
    for i in numbers:
        bin_i = bin(i)[2:]
        bin_i = bin_i.zfill(len(bin_i)+1)
        for idx, b in enumerate(bin_i[::-1]):
            if b == '0':
                if idx != 0:
                    idx -= 1
                res = i + pow(2, idx)
                answer.append(res)
                break
    return answer
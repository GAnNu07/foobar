from itertools import permutations
def solution(lis):
    lis.sort(reverse=True)
    for i in range(len(lis),1,-1):
        per=permutations(lis,i)
        for x in per:
            x=int(''.join(map(str,x)))
            if x%3==0:
                return x
                exit()   
    return 0  

if __name__ == "__main__":
    print(solution([3, 1, 4, 1, 5, 9]))


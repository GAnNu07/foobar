#!usr/bin/python
def solution(area):
    sol=[]
    def rec(area):
        if area==0:
            pass
        else:
            x=1
            while area>=(x*x):
                x+=1
            area=area-((x-1)*(x-1))
            sol.append(((x-1)*(x-1)))
            rec(area)
       
    rec(area)
    return sol
    #print(*sol, sep = ",")
print(solution(15324))
print(solution(12))

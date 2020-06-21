def solution(total_lambs):
    li=[]
    maxli=[]
    def generous(li,number,x,total):
        while total<number:
            total+=x
            li.append(x)
            x*=2
        if total==number:
            pass
        else:
            del li[len(li)-1]
        print(li)

    def stingy(maxli,number,x,total):
        index=0
        while total<number:
            if index==0 or index==1:
                maxli.append(x)
                total+=x
                index+=1
            else:
                x=maxli[len(maxli)-1]+maxli[len(maxli)-2]
                total+=x
                maxli.append(x)
        if total==number:
            pass
        else:
            del maxli[len(maxli)-1]
        print(maxli)


    generous(li,total_lambs,1,0)
    stingy(maxli,total_lambs,1,0)
    answer=len(maxli)-len(li)
    return answer

if __name__ == "__main__":
    print(solution(10))

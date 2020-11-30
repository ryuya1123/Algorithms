def linear_serach() -> str:
    A = list(map(int, input('please input array').split()))
    v = 4
    answer = []
    for i in range(0, len(A)):
        if v == A[i]:
            answer.append(A[i])
        else:
            continue
        
    if not answer:
        answer.append('NIL')
        
    return answer
        
    
def __main__():
    print(linear_serach())

    
if __name__ == '__main__':
    __main__()
    

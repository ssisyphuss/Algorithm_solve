def solution(arr):
    answer = []
    N = len(arr)
    
    for i in range(N-1):
        if arr[i] != arr[i+1]:
            answer.append(arr[i])
    
    answer.append(arr[N-1])
        
    return answer
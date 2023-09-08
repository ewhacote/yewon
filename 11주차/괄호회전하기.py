def solution(s):
    count=0
    for strt_idx in range(len(s)):
        temp_s=s[strt_idx:]+s[:strt_idx]
        while True:
            length=len(temp_s)
            temp_s=temp_s.replace("()","")
            temp_s=temp_s.replace("{}","")
            temp_s=temp_s.replace("[]","")
            if len(temp_s)==0: # 반복문을 거듭하며 모든 문자가 소거되었을 때
                count+=1
                break # 해당 While문에서 벗어나, for문을 다시 순회한다. 이 때, 새로운 temp_s가 할당된다.
            if length==len(temp_s): # 소거 작업 후에도 문자열의 길이의 변화가 없을 경우. 즉, 더는 소거가 되질 않는 상황을 의미한다. 이는 Fail.
                break
    return count

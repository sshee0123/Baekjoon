import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int,input().split()))
answer = 0

def merge_sort(s,e):
    global arr,answer
    if s<e:
        mid = (s+e)//2
        merge_sort(s,mid)
        merge_sort(mid+1,e)
        sorted_list = []
        i, j = s, mid+1
        while i<=mid and j<=e:
            if arr[i] <= arr[j]:
                sorted_list.append(arr[i])
                i+=1
            else:
                sorted_list.append(arr[j])
                j+=1
                answer = answer + (mid+1-i)
        while i<=mid:
            sorted_list.append(arr[i])
            i+=1
        while j<=e:
            sorted_list.append(arr[j])
            j+=1
        for i in range(len(sorted_list)):
            arr[s+i] = sorted_list[i]
merge_sort(0,n-1)
print(answer)
array = [7,5,9,0,3,1,6,2,4,8]

#선택정렬 : 가장 작은 것을 선택해 맨 앞에 있는 데이터와 바꾸는 것 반복.
#시간 복잡도 : O(N제곱)
for i in range(len(array)):
    min_index = i
    for j in range(i+1,len(array)):
        if array[min_index] > array[j]:
            min_index = j
    array[i],array[min_index] = array[min_index],array[i]
print(array)

#삽입정렬 : 특정한 데이터를 적절한 위치에 삽입한다.
#(첫 번째 데이터는 정렬되어있다고 가정하고 두번째 데이터 부터 시작)
#시간 복잡도 : O(N제곱)
#이미 정렬되어 있는 리스트에서는 최선의 선택
for i in range(1,len(array)):
    for j in range(i,0,-1):
        #index i 부터 1까지 1씩 감소
        if array[j]<array[j-1]:
            #한칸씩 감소
            array[j], array[j-1] = array[j-1],array[j]
        else: #자신보다 작은 데이터 만나면 종료
            break
print(array)

#퀵정렬 : 기준 데이터(피벗)를 설정하고 그 기준보다 큰 데이터와 작은 데이터 위치 변경
def quick_sort(array,start,end):
    #종료조건 : 원소가 1개인 경우
    if start>=end:
        return
    pivot = start #피벗은 첫 번째 원소
    left = start+1
    right = end
    while left<=right:
        #왼쪽부터 피봇보다 큰 값 찾을 때까지
        while left<=end and array[left]<=array[pivot]:
            left+=1
        #오른쪽부터 피봇보다 작은 값 찾을 때까지
        while right>start and array[right]>=array[pivot]:
            right-=1

        if left>right: #이동하다가 엇갈린다면 피봇과 작은 값인(right) 데이터 위치 변경
            array[pivot],array[right] = array[right],array[pivot]
        else: #엇갈리지 않았다면 큰 값, 작은 값 변경
            array[left],array[right] = array[right],array[left]

    #right 기준으로 왼쪽 오른쪽 재귀함수
    quick_sort(array,start,right-1)
    quick_sort(array,right+1,end)

quick_sort(array,0,len(array)-1)
print(array)

#파이썬 퀵정렬
#시간 복잡도 : O(NlogN)
def quick_python_sort(array):
    if len(array)<=1:
        return array
    pivot = array[0]
    tail = array[1:]
    left_array = [x for x in tail if x<=pivot]
    right_array = [x for x in tail if x>pivot]

    return quick_python_sort(left_array) + [pivot] + quick_python_sort(right_array)
print(quick_python_sort(array))

#계수정렬
#시간 복잡도 O(N+K)
array1 = [7, 5, 9, 0, 3, 1, 6, 2, 9, 1, 4, 8, 0, 5,2]
count = [0]*(max(array1)+1)
for i in range(len(array1)):
    count[array1[i]] +=1
for i in range(len(count)):
    for j in range(count[i]):
        print(i,end=' ')


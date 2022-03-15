#include <iostream>

using namespace std;

int main(){
    int n, m;
    cin >> n >> m;

    int arr[n+1];
    for (int i=0;i<n;i++){
        cin >> arr[i];
    }

    int cnt = 0;
    int left = 0, right = 0;
    int result = arr[0];

    // 투 포인터 알고리즘 적용
    while (left <= right && right < n){
        if (result < m){
            result += arr[++right];
        }
        else if (result == m){
            cnt += 1;
            result += arr[++right];
        }
        else if (result > m){
            result -= arr[left++];

            if (left > right){
                right = left;
                result = arr[left];
            }
        }
    }

    cout << cnt<<endl;
}
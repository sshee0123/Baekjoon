#include <string>
#include <vector>
using namespace std;
bool visited[201]; //방문검사

void dfs(vector<vector<int>> &arr, int idx){
    for(int i=0; i<arr[idx].size(); i++){
        if(arr[idx][i] == 1 && visited[i] == false){ //1이고 아직 방문하지 않은 컴
            arr[idx][i] = 0;
            visited[i] = true;
            dfs(arr, i); //dfs 진행
        }
    }
}

int solution(int n, vector<vector<int>> computers) {
    int answer = 0;
    for(int i=0; i<n; i++){
        if (visited[i]==false){
            dfs(computers,i); //dfs 진행
            answer++;
        }
    }
    return answer;
}
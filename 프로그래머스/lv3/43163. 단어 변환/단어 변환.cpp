#include <string>
#include <vector>
#include <algorithm>
using namespace std;

int answer = 50;
bool visited[50]; //방문words

//begin과 한 글자만 다른 words 찾는 함수
bool oneDiff(string a, string b){
    int cnt_diff = 0;
    for(int i=0; i<b.size(); i++){
        if(a[i]!=b[i]){
            cnt_diff ++;
        }
    }
    if(cnt_diff == 1) //하나만 다르면
        return true;
    else
        return false;
}

void dfs(string begin, string target, vector<string> words, int idx){
   
    if(answer <= idx)
        return;
    
    if(begin == target){ //종료조건
        answer = min(idx, answer);
        return; //종료
    }
    
    for(int i=0; i<words.size(); i++){
        //한글자만 다르고 아직 방문하지 않았으면
        if(oneDiff(begin, words[i]) && !visited[i]){
            visited[i] = true;
            dfs(words[i], target, words, idx+1);
            visited[i] = false; //dfs종료 후 돌아오면, 백트래킹
        }
    }
    return;
}

int solution(string begin, string target, vector<string> words) {

    dfs(begin, target, words,0);
    if(answer == 50){ //변환할 수 없으면 0
        answer = 0;
    }
    return answer;
}
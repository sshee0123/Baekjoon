#include <string>
#include <vector>
#include <queue>
using namespace std;

int solution(vector<int> sco, int K) {
    int answer = 0;
    //우선순위큐 minheap생성
    priority_queue<int, vector<int>, greater<int>> pq(sco.begin(), sco.end());
    
    while(pq.size()>1 && pq.top()<K){
        //큐에 음식 2개이상있고, 가장 작은 스코빌 지수가 k보다 작을때
        int tmp1 = pq.top();
        pq.pop();
        int tmp2 = pq.top();
        pq.pop();
        int tmp3 = (tmp1+ (tmp2*2));
        pq.push(tmp3);
        answer ++; // 섞어주기
    }
    if (pq.top()>=K)
        return answer;
    else
        return -1;
}
#include <string>
#include <vector>
using namespace std;

vector<int> solution(int brown, int yellow) {
    vector<int> answer;
    int carpet = brown + yellow;
    
    //carpet의 약수 구하기 (n가로, m세로)
    for (int m=3; m<carpet/2; m++){
        if (carpet % m == 0){
            int n = carpet / m;
            
            //노란색 개수와 맞는지 확인
            if((m-2)*(n-2) == yellow){
                answer.push_back(n);
                answer.push_back(m);
                break;
            }
        }
    }
    return answer;
}

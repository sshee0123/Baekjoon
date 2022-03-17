#include <string>
#include <vector>
#include <cmath>
#include <set>
#include <iostream>
using namespace std;

set<int> numberSet;
//에라토스테네스의 체
bool isPrime(int n){
    if (n<2)
        return false;
    for (int i=2; i<=sqrt(n); i++){
        if (n%i == 0)
            return false;
    }
    return true;
}
//numbers로 숫자조합 만들기 -> numberSet 셋에 삽입
void makeCombination(string comb, string others){
    if (comb != "")
        numberSet.insert(stoi(comb)); //string to int
    
    for (int i=0; i<others.size(); i++)
        //재귀함수
        makeCombination(comb + others[i], others.substr(0,i) + others.substr(i+1));
}
int solution(string numbers) {
    int answer = 0;
    //numbers로 가능한 숫자 조합 만들기
    makeCombination("", numbers);

    set<int>::iterator iter;
    for(iter = numberSet.begin(); iter!=numberSet.end(); iter++){
        if(isPrime(*iter))
            answer++;
    }
    return answer;
}
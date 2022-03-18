#include <string>
#include <vector>

using namespace std;
int answer = 0;
void dfs(vector<int> numbers, int target, int total, int index){
    if (index == numbers.size()){
        if (total == target){
            answer ++ ;
        }
        return;
    }
    
    dfs(numbers, target, total + numbers[index], index + 1);
    dfs(numbers, target, total - numbers[index], index + 1);
}
int solution(vector<int> numbers, int target) {
    dfs(numbers, target, numbers[0], 1);
    dfs(numbers, target, -numbers[0], 1);
    return answer;
}
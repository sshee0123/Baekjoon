#include <iostream>
#include <regex>
#include <string>
using namespace std;
int main(){
    string str;
    cin >> str;
    string app = "(100+1+|01)+";
    if(regex_match(str,regex(app))) cout << "SUBMARINE";
    else cout <<"NOISE";
    return 0;

}
// https://www.hackerrank.com/challenges/lonely-integer/

#include <iostream>

int main() {
    int n;
    std::cin >> n;
    int c, res = 0; 
    while (n--) {
        std::cin >> c;
        res ^= c; 
    }
    std::cout << res << std::endl; 
    return 0;
}
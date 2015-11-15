// https://leetcode.com/problems/single-number/

int singleNumber(int A[], int n) {
    int number = 0; 
    while(n >= 0) number ^= A[--n]; 
    return number; 
}

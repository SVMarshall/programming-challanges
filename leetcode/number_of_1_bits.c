// https://leetcode.com/problems/number-of-1-bits/

const int hw[] = {
    0, // 0x0000 0
    1, // 0x0001 1
    1, // 0x0010 2
    2, // 0x0011 3
    1, // 0x0100 4
    2, // 0x0101 5
    2, // 0x0110 6
    3, // 0x0111 7
    1, // 0x1000 8
    2, // 0x1001 9
    2, // 0x1010 10
    3, // 0x1011 11
    2, // 0x1100 12
    3, // 0x1101 13
    3, // 0x1110 14
    4, // 0x1111 15
};

int hammingWeight(uint32_t n) {
    return hw[n & 0x000F] + hw[(n >> 4) & 0xF] + hw[(n >> 8) & 0xF] + hw[(n >> 12) & 0xF] + 
           hw[(n >> 16) & 0x000F] + hw[(n >> 20) & 0xF] + hw[(n >> 24) & 0xF] + hw[(n >> 28) & 0xF];
}
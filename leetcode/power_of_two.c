// https://leetcode.com/problems/power-of-two/

static const unsigned char nbits[256] = 
{
#   define B2(n) n,     n+1,     n+1,     n+2
#   define B4(n) B2(n), B2(n+1), B2(n+1), B2(n+2)
#   define B6(n) B4(n), B4(n+1), B4(n+1), B4(n+2)
    B6(0), B6(1), B6(1), B6(2)
};

bool isPowerOfTwo(int n) {
    return (nbits[n & 0xff] + nbits[(n >> 8) & 0xff] + nbits[(n >> 16) & 0xff] + nbits[n >> 24] == 1); 
}
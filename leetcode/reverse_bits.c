// https://leetcode.com/problems/reverse-bits/

const char rev_lookup_table[16] = {
    0b0000, // <-0b0000
    0b1000, // <-0b0001
    0b0100, // <-0b0010
    0b1100, // <-0b0011
    0b0010, // <-0b0100
    0b1010, // <-0b0101
    0b0110, // <-0b0110
    0b1110, // <-0b0111
    0b0001, // <-0b1000
    0b1001, // <-0b1001
    0b0101, // <-0b1010
    0b1101, // <-0b1011
    0b0011, // <-0b1100
    0b1011, // <-0b1101
    0b0111, // <-0b1110
    0b1111, // <-0b1111
};

uint32_t reverseBits(uint32_t n) {
    return 
        rev_lookup_table[(n      ) & 0xF] << 28 | 
        rev_lookup_table[(n >> 4 ) & 0xF] << 24 |
        rev_lookup_table[(n >> 8 ) & 0xF] << 20 |
        rev_lookup_table[(n >> 12) & 0xF] << 16 |
        rev_lookup_table[(n >> 16) & 0xF] << 12 |
        rev_lookup_table[(n >> 20) & 0xF] <<  8 |
        rev_lookup_table[(n >> 24) & 0xF] <<  4 |
        rev_lookup_table[(n >> 28) & 0xF]; 
}
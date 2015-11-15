// https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

#define min(x,y) ((y) + (((x) - (y)) & (((x) - (y)) >> (sizeof(int) * CHAR_BIT - 1))))
#define max(x,y) ((x) - (((x) - (y)) & (((x) - (y)) >> (sizeof(int) * CHAR_BIT - 1))))

int maxProfit(int prices[], int n) {
    int max_profit = 0;
    int i, curr_min; 
    if (n >= 2) {
        curr_min = prices[0];
        for (i = 1; i < n; i++) {
            curr_min = min(curr_min, prices[i]);
            max_profit = max(max_profit, prices[i] - curr_min);
        }
    }
    return max_profit;
}
class Solution {
public:
    bool isPerfectSquare(int num) {
        if (num < 2) return true; // 0 and 1 are perfect squares

        for (long long i = 2; i * i <= num; i++) {
            if (i * i == num) {
                return true;
            }
        }
        return false;
    }
};

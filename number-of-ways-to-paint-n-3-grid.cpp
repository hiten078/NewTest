class Solution {
public:
    int numOfWays(int n) {
        long long MOD = 1e9 + 7;







        long long countA = 6;
        long long countB = 6;

        for (int i = 2; i <= n; ++i) {








            long long next_countA = (2 * countA + 2 * countB) % MOD;
            long long next_countB = (2 * countA + 3 * countB) % MOD;

            countA = next_countA;
            countB = next_countB;
        }

        return (countA + countB) % MOD;
    }
};
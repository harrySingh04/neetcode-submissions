class Solution {


    public int climbStairs(int n) {
        
        if(n == 1 || n == 2)
            return n;
        int[] dp = new int[n+1];
        int a = 1, b = 2, c = a + b;
        
        for(int i=3;i<=n;i++){

            c = a + b;
            a = b;
            b = c;
        }

        return c;
    }
}

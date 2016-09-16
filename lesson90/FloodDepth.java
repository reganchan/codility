// you can also use imports, for example:
// import java.util.*;

// you can write to stdout for debugging purposes, e.g.
// System.out.println("this is a debug message");
import java.util.*;

class Solution {
    public int solution(int[] A) {
        // write your code in Java SE 8
        int N = A.length;
        int[] left    = new int[N];
        for(int i=0; i < N; i++){ left[i]=-1; };

        int maxleft = -1;
        int prev    = A[0];
        for(int i=0; i < N; i++){
            int a = A[i];
            maxleft = maxleft < a ? a : maxleft;
            left[ i ] = maxleft;
        }
//        System.out.println( Arrays.toString(left) );

        int maxright = -1;
        int maxdepth = 0;
        for(int i=N-1; i >= 0; i--){
            int a = A[i];
            maxright = maxright < a ? a : maxright;
            int level = maxright < left[i] ? maxright : left[i];
            int depth = level - a;
//            System.out.println( depth );
            maxdepth = maxdepth < depth ? depth : maxdepth;
        }
        return maxdepth;
    }
}
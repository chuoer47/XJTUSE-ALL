package src;

public class Bttsp5_6 {
    static int n; // 图G的顶点数
    static int[] x; // 当前解
    static int[] bestx; // 当前最优解
    static float bestc; // 当前最优值
    static float cc; // 当前费用
    static float[][] a; // 图G的邻接矩阵
    static float[] mina; // 记录a每一行最小的值

    static float MAX_VALUE;

    public static float tsp(int[] v){
        // 置x为单位排列
        x = new int[n+1];
        for (int i = 1; i <= n ; i++) {
            x[i] = i;
        }
        // 设置上界
        MAX_VALUE = maxC();
        // 设置mina
        setMina();
        // 下面为源代码的程序
        bestc = MAX_VALUE;
        bestx = v;
        cc = 0;
        // 搜索x[2:n]的全排序
        backtrack(2);
        return bestc;
    }

    private static void backtrack(int i){
        if (i == n) { // 到达边界
            // 该判断条件不变
            if (a[x[n-1]][x[n]] <MAX_VALUE
                    && a[x[n]][1]<MAX_VALUE
                    && cc+a[x[n-1]][x[n]]+a[x[n]][1]<bestc){
                for (int j = 1; j <= n ; j++) {
                    bestx[j] = x[j];
                }
                bestc = cc +a[x[n-1]][x[n]]+a[x[n]][1];
            }
        }
        else {
            for (int j = i; j <= n; j++) {
                // 是否可进入x[j]子树，该判断条件可以进行改变，即进行剪枝
                if (a[x[i-1]][x[j]] < MAX_VALUE
                        && cc+a[x[i-1]][x[j]]+calRest(i)<bestc){
                    swap(x,i,j);
                    cc+=a[x[i-1]][x[i]];
                    backtrack(i+1);
                    cc-=a[x[i-1]][x[i]];
                    swap(x,i,j);
                }
            }
        }
    }

    private static void swap(int[] x,int i,int j){
        int temp = x[i];
        x[i] = x[j];
        x[j] = temp;
        return;
    }

    private static float maxC(){
        float sum = 0;
        for (int i = 1; i <= n; i++) {
            float t = a[i][0];
            for (int j = 1; j <= n; j++) {
                t = Math.max(t,a[i][j]);
            }
            sum+=t;
        }
        return sum+1;
    }

    private static void setMina() {
        mina = new float[n + 1];
        for (int i = 1; i <= n; i++) {
            float t = a[i][0];
            for (int j = 1; j <= n; j++) {
                t = Math.min(t, a[i][j]);
            }
            mina[i] = t;
        }
        return;
    }

    private static float calRest(int i){
        float sum = 0;
        for (int j = i; j <= n ; j++) {
            sum += mina[x[j]];
        }
        return sum;
    }
}

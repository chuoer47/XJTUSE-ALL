package src;

public class Bttsp {
    static int n; // 图G的顶点数
    static int[] x; // 当前解
    static int[] bestx; // 当前最优解
    static float bestc; // 当前最优值
    static float cc; // 当前费用
    static float[][] a; // 图G的邻接矩阵

    public static float tsp(int[] v){
        // 置x为单位排列
        x = new int[n+1];
        for (int i = 1; i <= n ; i++) {
            x[i] = i;
        }
        bestc = Float.MAX_VALUE;
        bestx = v;
        cc = 0;
        // 搜索x[2:n]的全排序
        backtrack(2);
        return bestc;
    }

    private static void backtrack(int i){
        if (i == n) {
            if (a[x[n-1]][x[n]] <Float.MAX_VALUE
                    && a[x[n]][1]<Float.MAX_VALUE
                    && (bestc==Float.MAX_VALUE || cc+a[x[n-1]][x[n]]+a[x[n]][1]<bestc) ) {
                for (int j = 1; j <= n ; j++) {
                    bestx[j] = x[j];
                }
                bestc = cc +a[x[n-1]][x[n]]+a[x[n]][1];
            }
        }
        else {
            for (int j = i; j <= n; j++) {
                // 是否可进入x[j]子树
                if (a[x[i-1]][x[j]] < Float.MAX_VALUE
                        && (bestc== Float.MAX_VALUE || cc+a[x[i-1]][x[j]]<bestc)){
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

}

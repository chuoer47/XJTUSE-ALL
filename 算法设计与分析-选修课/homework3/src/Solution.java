package src;

import java.lang.reflect.Array;
import java.util.Arrays;
import java.util.Comparator;

public class Solution {
    static int n; // 集装箱个数
    static int c; // 轮船载重量
    static Integer[] w; // 集装箱重量数组
    static int[] x; // 当前装载解
    static int[] bestx; // 当前装载最优解
    static int bestc; // 当前最大载重量
    static int cw; // 当前载重量

    public static int tsp(int[] v){
        // 置x为单位排列
        x = new int[n+1];
        for (int i = 1; i <= n ; i++) {
            x[i] = i;
        }
        // 下面为初始化
        bestc = 0;
        bestx = v;
        cw = 0;
        // 从第1个开始
        backtrack(1);
        return bestc;
    }

    private static void backtrack(int i) {
        if(i>n){ // 达到叶节点
            if (cw>bestc){
                bestc = cw;
                for (int j = 1; j <= n; j++) {
                    bestx[j] = x[j];
                }
            }
            return;
        }
        else{
            if (cw+w[i]<=c){
                // 进入左子树
                cw += w[i]; // 加上重量
                x[i] = 1; // 装载上
                backtrack(i+1);
                cw -= w[i]; // 减去重量
                x[i] = 0; // 卸载
            }
            if (rest(i+1)+cw > bestc){
                x[i] = 0;
                backtrack(i+1); // 进入右子树
            }

        }
    }

    // 上界函数
    private static int rest(int i){
        int sum = 0;
        for (int j = i; j <= n ; j++) {
            sum += w[j];
        }
        return sum;
    }

    private static void swap(int[] x,int i,int j){
        int temp = x[i];
        x[i] = x[j];
        x[j] = temp;
        return;
    }

    public static void main(String[] args) {

        n = 6;
        c = 25;
        System.out.println("n="+n);
        System.out.println("c="+c);
        w = new Integer[]{0, 7, 2, 6, 5, 4,9};
        tsp(new int[n+1]);
        System.out.print("w为");
        for (int i = 1; i <= n ; i++) {
            System.out.print(w[i]+" ");
        }
        System.out.println();
        System.out.println("最佳装载量："+bestc);
        System.out.println("最佳装载方案（1：装载；0：不装载）");
        for (int i = 1; i <= n ; i++) {
            System.out.print(bestx[i]+" ");
        }

    }

}

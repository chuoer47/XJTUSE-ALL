import java.util.Arrays;

public class KruskalCase {

    private int edgeNum; //边的个数
    private char[] vertexs; //顶点数组
    private int[][] matrix; //邻接矩阵
    //使用 INF 表示两个顶点不能连通
    private static final int INF = Integer.MAX_VALUE;

    public static void main(String[] args) {
        char[] vertexs = {'1', '2', '3', '4', '5'};
        //克鲁斯卡尔算法的邻接矩阵
        int matrix[][] = {
                /*A*//*B*//*C*//*D*//*E*/
                /*A*/ {   0,  3, INF, INF, 1},
                /*B*/ {  3,   0,  5,   3,  2},
                /*C*/ { INF,  5,   0,   6, INF},
                /*D*/ { INF,  3,   6,   0,   2},
                /*E*/ {   1,  2,  INF,   2,   0}};

        //创建KruskalCase 对象实例
        KruskalCase kruskalCase = new KruskalCase(vertexs, matrix);
        //输出构建的
        kruskalCase.kruskal();

    }

    //构造器
    public KruskalCase(char[] vertexs, int[][] matrix) {
        //初始化顶点数和边的个数
        int vlen = vertexs.length;
        //初始化顶点, 复制拷贝的方式
        this.vertexs = vertexs;
        //初始化边, 使用的是复制拷贝的方式
        this.matrix = matrix;
        //统计边的条数
        for(int i =0; i < vlen; i++) {
            for(int j = i+1; j < vlen; j++) {
                if(this.matrix[i][j] != INF) {
                    edgeNum++;
                }
            }
        }

    }
    public void kruskal() {
        int index = 0; //表示最后结果数组的索引
        int[] ends = new int[edgeNum]; //用于保存"已有最小生成树" 中的每个顶点在最小生成树中的终点
        //创建结果数组, 保存最后的最小生成树
        EData[] rets = new EData[edgeNum];

        //获取图中 所有的边的集合 ， 一共有12边
        EData[] edges = getEdges();

        //按照边的权值大小进行排序(从小到大)
        sortEdges(edges);

        //遍历edges 数组，将边添加到最小生成树中时，判断是准备加入的边否形成了回路，如果没有，就加入 rets, 否则不能加入
        for(int i=0; i < edgeNum; i++) {
            //获取到第i条边的第一个顶点(起点)
            int p1 = getPosition(edges[i].start);
            //获取到第i条边的第2个顶点
            int p2 = getPosition(edges[i].end);

            //获取p1这个顶点在已有最小生成树中的终点
            int m = getEnd(ends, p1);
            //获取p2这个顶点在已有最小生成树中的终点
            int n = getEnd(ends, p2);
            //是否构成回路
            if(m != n) { //没有构成回路
                ends[m] = n; // 设置m 在"已有最小生成树"中的终点
                rets[index++] = edges[i]; //有一条边加入到rets数组
            }
        }
        //统计并打印 "最小生成树", 输出  rets
        System.out.println("最小生成树生成路径为");
        int sum = 0;
        for(int i = 0; i < index; i++) {
            System.out.println(rets[i]);
            sum += rets[i].weight;
        }
        for (int i = 0; i < index; i++) {
            System.out.println(ends[i]);
        }
        System.out.println("sum cost:" + sum);


    }
    /**
     * 功能：对边进行排序处理, 冒泡排序
     * @param edges 边的集合
     */
    private void sortEdges(EData[] edges) {
        for(int i = 0; i < edges.length - 1; i++) {
            for(int j = 0; j < edges.length - 1 - i; j++) {
                if(edges[j].weight > edges[j+1].weight) {//交换
                    EData tmp = edges[j];
                    edges[j] = edges[j+1];
                    edges[j+1] = tmp;
                }
            }
        }
    }
    /**
     *
     * @param ch 顶点的值，比如'A','B'
     * @return 返回ch顶点对应的下标，如果找不到，返回-1
     */
    private int getPosition(char ch) {
        for(int i = 0; i < vertexs.length; i++) {
            if(vertexs[i] == ch) {//找到
                return i;
            }
        }
        //找不到,返回-1
        return -1;
    }
    /**
     * 功能: 获取图中边，放到EData[] 数组中，后面我们需要遍历该数组
     * 是通过matrix 邻接矩阵来获取
     * EData[] 形式 [['A','B', 12], ['B','F',7], .....]
     * @return
     */
    private EData[] getEdges() {
        int index = 0;
        EData[] edges = new EData[edgeNum];
        for(int i = 0; i < vertexs.length; i++) {
            for(int j=i+1; j <vertexs.length; j++) {
                if(matrix[i][j] != INF) {
                    edges[index++] = new EData(vertexs[i], vertexs[j], matrix[i][j]);
                }
            }
        }
        return edges;
    }
    /**
     * 功能: 获取下标为i的顶点的终点(), 用于后面判断两个顶点的终点是否相同
     * @param ends ： 数组就是记录了各个顶点对应的终点是哪个,ends 数组是在遍历过程中，逐步形成
     * @param i : 表示传入的顶点对应的下标
     * @return 返回的就是 下标为i的这个顶点对应的终点的下标,
     */
    private int getEnd(int[] ends, int i) { // i = 4 [0,0,0,0,5,0,0,0,0,0,0,0]
        while(ends[i] != 0) {
            i = ends[i];
        }
        return i;
    }
    //创建一个类EData 表示一条边的数据类
    public class EData {
        char start; //边的一个点
        char end; //边的另外一个点
        int weight; //边的权值
        //构造器
        public EData(char start, char end, int weight) {
            this.start = start;
            this.end = end;
            this.weight = weight;
        }
        @Override
        public String toString() {
            return  start + "<————>" + end + " cost time: " + weight;
        }
    }
}



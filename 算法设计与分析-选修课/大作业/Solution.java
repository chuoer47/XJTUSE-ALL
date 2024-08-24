import java.util.Scanner;

public class Solution {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        // 模拟input.txt录入
        System.out.println("input.txt输入：");
        int B = scanner.nextInt();
        int[] id = new int[5]; // 用于进行商品的编号转化为id号的数组：id号表示为下标，比如7、8转化为0、1.
        Goods[] goods = new Goods[5];
        for (int i = 0; i < B; i++) {
            int C = scanner.nextInt();
            int K = scanner.nextInt();
            int P = scanner.nextInt();
            goods[i] = new Goods(i,K,P);
            id[i] = C;
        }
        for (int i = B; i < 5; i++) { // 将剩余的商品假设出来
            goods[i] = new Goods(i,0,0); // 将K=0表示不需要
        }
        System.out.println("offer.txt输入：");
        int S = scanner.nextInt();
        int j = 0;
        Offer[] offers = new Offer[S]; // 优惠策略清单
        for (int i = 0; i < S; i++) { // 将优惠政策列表记录下来！
            Offer offer = new Offer();
            j = scanner.nextInt();
            for (int k = 0; k < j; k++) {
                int C = scanner.nextInt();
                int K = scanner.nextInt();
                offer.num[findId(id,C)] = K; // 记录id号的优惠政策
            }
            int price = scanner.nextInt();
            offer.setPrice(price);
            offers[i] = offer;
        }
        System.out.println(fuc(goods,offers));
    }
    public static int fuc(Goods[] goods,Offer[] offers){
        int[][][][][] dp = new int[5][5][5][5][5]; // 因为每个产品至多只购买5个。
        // 更新dp矩阵，更新值为不使用优惠策略。
        for (int i1 = 0; i1 <= goods[0].need; i1++) {
            for (int i2 = 0; i2 <= goods[1].need; i2++) {
                for (int i3 = 0; i3 <= goods[2].need; i3++) {
                    for (int i4 = 0; i4 <= goods[3].need; i4++) {
                        for (int i5 = 0; i5 <= goods[4].need; i5++) {
                            dp[i1][i2][i3][i4][i5] = i1*goods[0].price + i2*goods[1].price +i3*goods[2].price
                                    + i4*goods[3].price + i5*goods[4].price;
                        }
                    }
                }
            }
        }
        // 使用优惠政策
        for (int i = 0; i < offers.length; i++) {
            for (int i1 = offers[i].num[0]; i1 <= goods[0].need; i1++) {
                for (int i2 = offers[i].num[1]; i2 <= goods[1].need; i2++) {
                    for (int i3 = offers[i].num[2]; i3 <= goods[2].need; i3++) {
                        for (int i4 = offers[i].num[3]; i4 <= goods[3].need; i4++) {
                            for (int i5 = offers[i].num[4]; i5 <= goods[4].need; i5++) {
                                dp[i1][i2][i3][i4][i5] = Integer.min(dp[i1][i2][i3][i4][i5],
                                        dp[i1-offers[i].num[0]][i2-offers[i].num[1]][i3-offers[i].num[2]][i4-offers[i].num[3]][i5-offers[i].num[4]]+offers[i].price);
                            }
                        }
                    }
                }
            }
        }
        return dp[goods[0].need][goods[1].need][goods[2].need][goods[3].need][goods[4].need];
    }
    public static int findId(int[] id, int C){ // 找到商品编号对于的id号
        for (int i = 0; i < id.length; i++) {
            if(id[i]==C){
                return i;
            }
        }
        return -1;
    }
    public static class Goods{ // 商品类
        int id; // 编号
        int price; // 价格
        int need; // 需要数量
        public Goods(int C,int K,int P){
            this.id = C;
            this.price = P;
            this.need = K;
        }
    }
    public static class Offer{ // 用来表示优惠组合的类
        int[] num = new int[5]; // num下标表示第几个商品，num的数字表示所需商品的数量
        int price; // 优惠价格
        public int getPrice() {
            return price;
        }
        public void setPrice(int price) {
            this.price = price;
        }
    }

}

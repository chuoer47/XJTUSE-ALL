// 按两次 Shift 打开“随处搜索”对话框并输入 `show whitespaces`，
// 然后按 Enter 键。现在，您可以在代码中看到空格字符。
public class Main {
    public static void main(String[] args) {
        Image image = new ProxyImage("test_10mb.jpg");
        System.out.println("-----");
        // 图像将从磁盘加载
        image.display();
        System.out.println("-----");
        // 图像不需要从磁盘加载
        image.display();
    }
}
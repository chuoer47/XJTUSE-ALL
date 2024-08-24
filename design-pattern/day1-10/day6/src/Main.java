// 按两次 Shift 打开“随处搜索”对话框并输入 `show whitespaces`，
// 然后按 Enter 键。现在，您可以在代码中看到空格字符。
public class Main {
    public static void main(String[] args) {
        Shape redCircle = new Circle(1, 1, 1, new RedCircle());
        Shape greenCircle = new Circle(1, 1, 1, new GreenCircle());
        redCircle.draw();
        greenCircle.draw();
    }
}
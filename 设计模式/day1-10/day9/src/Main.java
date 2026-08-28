// 按两次 Shift 打开“随处搜索”对话框并输入 `show whitespaces`，
// 然后按 Enter 键。现在，您可以在代码中看到空格字符。
public class Main {
    public static void main(String[] args) {
        Shape shape = new Circle();
        ShapeDecorator shapeDecorator = new RedShapeDecorator(new Circle());
        ShapeDecorator shapeDecorator1 = new RedShapeDecorator(new Rectangle());
        shape.draw();
        shapeDecorator.draw();
        shapeDecorator1.draw();
    }
}
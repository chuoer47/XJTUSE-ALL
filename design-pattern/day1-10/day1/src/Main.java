public class Main {
    public static void main(String[] args) {
        Shape shape;
        int[] kind = {Const.SQUARE, Const.RECTANGLE, Const.CIRCLE};
        for (int i : kind) {
            shape = ShapeFactory.getShape(i);
            shape.draw();
        }
    }
}
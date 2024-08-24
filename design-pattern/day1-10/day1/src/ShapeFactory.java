public class ShapeFactory {
    public static Shape getShape(int SHAPE) {
        Shape shape;
        if (SHAPE == Const.CIRCLE) {
            shape = new Circle();
        } else if (SHAPE == Const.RECTANGLE) {
            shape = new Rectangle();
        } else if (SHAPE == Const.SQUARE) {
            shape = new Square();
        } else {
            shape = null;
        }
        return shape;
    }
}

import java.util.Hashtable;

public class ShapeCache {
    private static Hashtable<String, Shape> hashtable = new Hashtable<String, Shape>();

    public static Shape getShape(String shapeId) {
        Shape shape = hashtable.get(shapeId);
        return (Shape) shape.clone();
    }

    public static void loadCache() {
        Square square = new Square();
        square.setId("Square");
        hashtable.put(square.getId(), square);
        Triangle triangle = new Triangle();
        triangle.setId("Triangle");
        hashtable.put(triangle.getId(), triangle);
    }
}

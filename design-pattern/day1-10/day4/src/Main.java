// Press Shift twice to open the Search Everywhere dialog and type `show whitespaces`,
// then press Enter. You can now see whitespace characters in your code.
public class Main {
    public static void main(String[] args) {
        ShapeCache.loadCache();
        Shape shape = ShapeCache.getShape("Square");
        shape.draw();
        System.out.println(shape);
        shape = ShapeCache.getShape("Triangle");
        shape.draw();
        shape = ShapeCache.getShape("Square");
        shape.draw();
        System.out.println(shape);
    }
}
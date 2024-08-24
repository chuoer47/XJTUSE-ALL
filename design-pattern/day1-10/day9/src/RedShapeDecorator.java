public class RedShapeDecorator extends ShapeDecorator {

    public RedShapeDecorator(Shape shape) {
        super(shape);
    }

    @Override
    public void draw() {
        shape.draw();
        setColor();
    }

    private void setColor() {
        System.out.println("red color.");
    }
}

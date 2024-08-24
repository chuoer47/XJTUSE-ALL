public class Square extends Shape {
    @Override
    void draw() {
        System.out.println("draw Square");
    }

    public Square() {
        this.setType("Square");
    }
}

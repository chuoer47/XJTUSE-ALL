public class Triangle extends Shape {

    @Override
    void draw() {
        System.out.println("draw triangle");
    }

    public Triangle() {
        this.setType("Triangle");
    }
}

public class Circle extends Shape {
    int r, x, y;

    public Circle(int r, int x, int y, DrawAPI drawAPI) {
        super(drawAPI);
        this.r = r;
        this.x = x;
        this.y = y;
    }

    @Override
    public void draw() {
        drawAPI.drawCircle(r, x, y);
    }
}

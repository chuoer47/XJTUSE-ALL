public class RedCircle implements DrawAPI {
    @Override
    public void drawCircle(int r, int x, int y) {
        System.out.println("draw red circle: r: " + r + " x: " + x + " y: " + y);
    }
}

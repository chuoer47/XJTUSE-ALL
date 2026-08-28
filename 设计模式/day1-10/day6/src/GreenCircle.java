public class GreenCircle implements DrawAPI {
    @Override
    public void drawCircle(int r, int x, int y) {
        System.out.println("draw green circle: r: " + r + " x: " + x + " y: " + y);
    }
}

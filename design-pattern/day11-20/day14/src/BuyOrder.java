public class BuyOrder implements Order {
    private Stock stock;

    public BuyOrder(Stock stock) {
        this.stock = stock;
    }

    @Override
    public void execute() {
        stock.buy();
    }
}

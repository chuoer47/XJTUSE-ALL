import java.util.ArrayList;
import java.util.List;

public class Broker {
    private List<Order> orderList = new ArrayList<>();
    public void addStockList(Order order){
        orderList.add(order);
    }
    public void placeStockList(){
        for (Order order:
             orderList) {
            order.execute();
        }
        orderList.clear();
    }
}

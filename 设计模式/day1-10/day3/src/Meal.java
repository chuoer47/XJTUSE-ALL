import java.util.ArrayList;

public class Meal {
    private ArrayList<Item> items = new ArrayList<Item>();

    public void addItem(Item item) {
        items.add(item);
    }

    public double getCost() {
        double cost = 0;
        for (Item it :
                items) {
            cost += it.getPrice();
        }
        return cost;
    }

    public void showItems() {
        for (Item it :
                items) {
            System.out.println("name:" + it.getName());
            System.out.println("price" + it.getPrice());
            System.out.printf("packing");
            it.getPacking().packing();
        }
    }
}

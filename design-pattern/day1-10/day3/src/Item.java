import java.util.SplittableRandom;

public abstract class Item implements ItemImp {
    private Packing packing;
    private String name;
    private double price;

    @Override
    public Packing getPacking() {
        return packing;
    }

    @Override
    public String getName() {
        return name;
    }

    @Override
    public double getPrice() {
        return price;
    }

    public void setPacking(Packing packing) {
        this.packing = packing;
    }

    public void setName(String name) {
        this.name = name;
    }

    public void setPrice(double price) {
        this.price = price;
    }

}

public class ColdDrink extends Item {
    public ColdDrink() {
        this.setPacking(new Bottle());
    }

    public ColdDrink(String name, double price) {
        this.setPacking(new Bottle());
        this.setName(name);
        this.setPrice(price);
    }
}

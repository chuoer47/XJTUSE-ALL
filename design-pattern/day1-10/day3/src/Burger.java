public class Burger extends Item {

    public Burger() {
        this.setPacking(new Wrapper());
    }

    public Burger(String name, double price) {
        this.setName(name);
        this.setPrice(price);
        this.setPacking(new Wrapper());
    }
}

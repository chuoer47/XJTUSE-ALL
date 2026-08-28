// Press Shift twice to open the Search Everywhere dialog and type `show whitespaces`,
// then press Enter. You can now see whitespace characters in your code.
public class Main {
    public static void main(String[] args) {
        Meal meal = MealBuilder.orderVegMeal();
        meal.showItems();
        System.out.println(meal.getCost());
        System.out.println("------------");
        meal = MealBuilder.orderNonVegMeal();
        meal.showItems();
        System.out.println(meal.getCost());
    }
}
public class MealBuilder {
    public static Meal orderVegMeal() {
        Meal meal = new Meal();
        meal.addItem(new Burger("vegetableBurger", 5.2));
        meal.addItem(new ColdDrink("pepsi", 6.6));
        return meal;
    }

    public static Meal orderNonVegMeal() {
        Meal meal = new Meal();
        meal.addItem(new Burger("chickenBurger", 9.62));
        meal.addItem(new ColdDrink("coke", 3.5));
        return meal;
    }
}

public class Singleton5 {
    private class SingletonData {
        private static final Singleton5 INSTANCE = new Singleton5();
    }

    private Singleton5() {
    }

    ;

    public static Singleton5 getInstance() {
        return SingletonData.INSTANCE;
    }
}

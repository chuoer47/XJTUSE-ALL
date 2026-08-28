/*
 * 懒汉式
 * 线程安全
 * */
public class Singleton2 {
    private static Singleton2 instance;

    private Singleton2() {
    }

    public static synchronized Singleton2 getInstance() { // 加互斥锁？
        if (instance == null) {
            instance = new Singleton2();
        }
        return instance;
    }
}

import java.util.concurrent.Callable;

class Task implements Callable<Integer> {
    @Override
    public Integer call() throws Exception {
        System.out.println("子线程在进行计算>");
        Thread.sleep(3000);
        int sum = 0;
        for (int i = 0; i < 100; i++)
            sum += i;
        System.out.println("子线程完成计算<");
        return sum;
    }
}

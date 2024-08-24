import java.util.concurrent.*;

public class CallableFuture {
    public static void main(String[] args) {
        ExecutorService executor = Executors.newCachedThreadPool();
        Task task = new Task();
        Future<Integer> result = executor.submit(task);
        executor.shutdown();

        try {
            Thread.sleep(1000);
        } catch (InterruptedException e1) {
            e1.printStackTrace();
        }

        System.out.println("主线程在执行任务>>>");
        try {
            System.out.println("task运行结果>>"+result.get());
        } catch (InterruptedException e) {
            e.printStackTrace();
        } catch (ExecutionException e) {
            e.printStackTrace();
        }
        catch (CancellationException e) {
            System.out.println("子线程已经取消任务");
        }

        System.out.println("所有任务执行完毕<<<");
    }
}
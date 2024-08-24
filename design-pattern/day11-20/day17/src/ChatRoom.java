import java.util.Date;
import java.util.concurrent.atomic.DoubleAccumulator;

public class ChatRoom {
    public static void showMassage(User user,String message){
        System.out.println(new Date().toString()+"["+user.getName()+"]"+message);
    }
}

import java.util.NoSuchElementException;
import java.lang.IllegalArgumentException;

public class ResizingQueue<T> {
    //    成员变量外加初始化
    private int maxSize = 2;
    private int front = 0;
    private int rear = 0;
    private T[] listArray =(T[]) new Object[2];
    //    无参构造方法
    public ResizingQueue(){}
    //    入队操作，要注意空队列，满队列等情况
    public void enqueue(T element) throws IllegalArgumentException{
        if (element == null){
            throw new IllegalArgumentException();
        }
        if (isExpand()){
//            expand()方法改变了大小，改变了front,rear,maxSize数值
            listArray = expand(maxSize,(maxSize-1)*2+1);
        }
        rear = (rear+1)%maxSize;
        listArray[rear] = element;
    }
    public T dequeue() throws NoSuchElementException{
        if (isEmpty()){
            throw new NoSuchElementException();
        }
        listArray[front] = null;
        front = (front+1)%maxSize;
        T res =listArray[front];
        if (isShrink()){
            listArray = shrink(maxSize,(maxSize-1)/2);
        }
        return res;
    }
    public int size(){
        if (rear>=front){
            return rear-front;
        }
        return maxSize-front+rear;
    }
    public boolean isFull(){
        return front == (rear+1)%maxSize;
    }
    public boolean isEmpty(){
        return rear == front;
    }
    private boolean isExpand(){
        return isFull();
    }
    private boolean isShrink(){
        return size()<=(maxSize-1)/4;
    }
    private T[] expand(int eSize, int nSize){
        T[] tem = (T[]) new Object[nSize];
        int temPivot = 0;
        if (front>rear){
            for (int i=front;i<eSize;i++){
                tem[temPivot++] = listArray[i];
            }
            for (int i=0;i<=rear;i++){
                tem[temPivot++] = listArray[i];
            }
        }
        else {
            for (int i=front;i<=rear;i++){
                tem[temPivot++] = listArray[i];
            }
        }
        maxSize = nSize;
        front = 0;
        rear = temPivot-1;
        return tem;
    }
    private T[] shrink(int eSize,int nSize){
//        需要对nSize进行判断
        nSize = (nSize<=3)?2:nSize;
        T[] tem = (T[]) new Object[nSize];
        int temPivot = 0;
        if (rear>=front){
            for (int i=front;i<=rear;i++){
                tem[temPivot++] = listArray[i];
            }
        }
        else{
            for (int i=front;i<eSize;i++){
                tem[temPivot++] = listArray[i];
            }
            for (int i=0;i<=rear;i++){
                tem[temPivot++] = listArray[i];
            }
        }
        front = 0;
        rear = temPivot - 1;
        maxSize = nSize;
        return tem;
    }
    @Override
    public String toString() {
        String res = "";
        res += "[";
//        不大于20的情况
        if (this.size()<=20){
            if (rear>=front){
                for (int i = front+1;i<=rear;i++){
                    res = res + listArray[i] + " ";
                }
            }
            else {
                for (int i = front+1;i<maxSize;i++){
                    res = res + listArray[i] + " ";
                }
                for (int i = 0;i<=rear;i++){
                    res = res + listArray[i] + " ";
                }
            }
        }
//        大于20的情况
        else {
            int tem = (front+1)%maxSize;
            int count = 0;
//            去前五个元素
            do{
                res = res + listArray[tem] + " ";
                tem = (tem+1)%maxSize;
                count++;
            }
            while (count<5);
            res += " ... ";
//            取后五个元素
            while (count<this.size()-5){
                tem = (tem+1)%maxSize;
                count++;
            }
            while (count<this.size()){
                res = res + listArray[tem] + " ";
                tem = (tem+1)%maxSize;
                count++;
            }
        }
        res = res.strip()+"]";
        res += "\nelements: " + this.size() + " size:"+(this.maxSize-1);
        return res;
    }
}
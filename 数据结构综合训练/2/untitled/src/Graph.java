import java.io.*;
import java.util.Objects;
import java.util.Scanner;

public class Graph {
    public static int UNVISITED = 0;
    public static int VISITED = 1;
    public int MAX_LINK = 9999;
    public Link link = new Link();
    public PrintWriter pw = new PrintWriter(new File("src/result_complex.txt"));

    public Graph() throws FileNotFoundException {
    }

    public class Link {
        public BST<String,Circle> character2 = new BST<String,Circle>();
        public String[] nameArr;

        public void addLink2(String name_1, String name_2, String filmName) {
            if (name_1.equals(name_2)) return;
            Circle xp = character2.search(name_1);
            if (xp == null) {
                character2.insert(name_1,new Circle(name_1));
                xp = character2.search(name_1);
            }
            xp.setNext(new Circle(name_2, filmName));
        }

        public void oneForAll() {
            int number = character2.numNode;
            for(String name:nameArr){
                System.out.println("一共有人数:"+ number);
                System.out.println("当前为："+ name);
                pw.println("下面是" + name + "的关系表");
                clear();
                txt2(name);
                System.out.println(name +"已完成！");
            }
            pw.close();
        }
        public void clear(){
            for (String name : nameArr) {
                Circle tem = character2.search(name);
                tem.visit = UNVISITED;
            }
        }
        public void txt2(String name){
            ResizingQueue<Circle> queue = new ResizingQueue<>();
            int capacity = character2.numNode;
            int[] bn = new int[capacity];
            String[] cn = new String[capacity];
            for (int i = 0; i < capacity; i++){
                bn[i] = MAX_LINK;
                cn[i] = "sorry, not found!\n";
            }
            int pivot_1 = findNamePivot(this.nameArr,name);
            bn[pivot_1] = 0;
            cn[pivot_1] = "";
            int pivot_2 = -1;
            queue.enqueue(character2.search(name));
            while (!queue.isEmpty()) {
                Circle tem = queue.dequeue();
                tem.visit = VISITED;
                Circle next = tem.next;
                pivot_1 =  findNamePivot(this.nameArr,tem.name);
                while (next != null) {
                    pivot_2 =  findNamePivot(this.nameArr,next.name);
                    Circle tem2 = character2.search(nameArr[pivot_2]);
                    if (tem2 != null && tem2.visit == UNVISITED) {
                        tem2.visit = VISITED;
                        queue.enqueue(tem2);
                    }
                    if (bn[pivot_1] + 1 < bn[pivot_2]) {
                        bn[pivot_2] = bn[pivot_1] + 1;
                        cn[pivot_2] = cn[pivot_1] +
                                "link is:" + tem.name + "\t " + next.name + "\t" + next.filmName + "\n";
                    }
                    next = next.next;
                }
            }
            for (int t = 0; t < capacity; t++) {
                if (bn[t] != MAX_LINK && bn[t] != 0) {
                    pw.println(name + "--->" + nameArr[t] + "\tBacon Number:" + bn[t]);
                    pw.println(cn[t]);
                }
            }
        }

        public int findNamePivot(String[] arr,String name) {
            int low = 0;
            int high = arr.length;
            while (low <= high) {
                int mid = (low + high) / 2;
                if (name.compareTo(arr[mid]) < 0) {
                    high = mid - 1;
                } else if (name.compareTo(arr[mid]) > 0)
                    low = mid + 1;
                else {
                    return mid;
                }
            }
            return -1;
        }
    }
    public class Circle {
        private String name = null;
        private Circle next = null;
        private String filmName = null;
        private int visit = UNVISITED;//判断是否被访问
        private Circle tail = this;
        public int pivot = -1;

        // 初始化构建
        public Circle(String name){
            this.name = name;
            this.filmName = "warn: this is the beginning!";
        }
        // 关联建构
        public Circle(String name,String filmName){
            this.name = name;
            this.filmName = filmName;
        }

        // setter and getter
        public String getName() {
            return name;
        }

        public void setName(String name) {
            this.name = name;
        }

        public Circle getNext() {
            return next;
        }

        public void setNext(Circle next) {
            pivot++;
            getTail().next = next;
            setTail(getTail().next);
        }

        public String getFilmName() {
            return filmName;
        }

        public void setFilmName(String filmName) {
            this.filmName = filmName;
        }

        public int getVisit() {
            return visit;
        }

        public void setVisit(int visit) {
            this.visit = visit;
        }

        public Circle getTail() {
            return tail;
        }

        public void setTail(Circle tail) {
            this.tail = tail;
        }
    }
    public void init2(File file) throws FileNotFoundException {
        int row = -1;
        Scanner sc = new Scanner(file);
        while (sc.hasNextLine()){
            row++;
            String strip = sc.nextLine().strip();
            if (!Objects.equals(strip, "")) {
                String[] arr = strip.split("/");
                int len = arr.length;
                String filmName = arr[0];
                for (int k = 1; k < len; k++) {
                    String name_1 = arr[k];
                    for (int j = k; j < len; j++) {
                        String name_2 = arr[j];
                        link.addLink2(name_1,name_2,filmName);
                        link.addLink2(name_2,name_1,filmName);
                    }
                }
            }
            System.out.println("处理完"+row);
        }
        this.setMaxLink(row);
        link.nameArr = link.character2.formName();
    }
    public void setMaxLink(int MAX_LINK){
        this.MAX_LINK = MAX_LINK;
    }
}

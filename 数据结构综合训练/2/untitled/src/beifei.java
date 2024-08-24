//import java.io.*;
//import java.util.Objects;
//import java.util.Queue;
//import java.util.Scanner;
//import java.util.concurrent.ConcurrentLinkedQueue;
//
//public class Graph {
//    public static int UNVISITED = 0;
//    public static int VISITED = 1;
//    public int MAX_LINK = 9999;
//    public Link link = new Link();
//    public String res = "";
//    public PrintWriter pw = new PrintWriter(new File("src/result_complex.txt"));
//
//    public Graph() throws FileNotFoundException {
//    }
//
//    public class Link {
//        public Circle[] character = new Circle[1];
//        public BST<String,Circle> character2 = new BST<String,Circle>();
//        public int pivot = -1;
//        public int capacity = 1;
//
//        public void addLink(String name_1, String name_2, String filmName) {
//            if (name_1.equals(name_2)) return;
//            Circle xp = findCharacter(name_1);
//            if (xp == null) {
//                addCharacter(name_1);
//                xp = character[pivot];
//            }
//            xp.setNext(new Circle(name_2, filmName));
//        }
//        public void addLink2(String name_1, String name_2, String filmName) {
//            if (name_1.equals(name_2)) return;
//            Circle xp = character2.search(name_1);
//            if (xp == null) {
//                character2.insert(name_1,new Circle(name_1));
//                xp = character2.search(name_1);
//            }
//            xp.setNext(new Circle(name_2, filmName));
//        }
//
//        public void addCharacter(String s) {
//            if (findCharacter(s) == null) {
//                if (pivot == capacity - 1) resize();
//                character[++pivot] = new Circle(s);
//            }
//        }
//
//        public void resize() {
//            Circle[] tem = new Circle[2 * capacity];
//            capacity *= 2;
//            if (pivot + 1 >= 0) System.arraycopy(character, 0, tem, 0, pivot + 1);
//            character = tem;
//        }
//
//        public Circle findCharacter(String s) {
//            for (Circle tem : character)
//                if (tem != null)
//                    if (s.equals(tem.getName())) return tem;
//            return null;
//        }
//        public int findCharacterPivot(String s) {
//            for (int i=0;i<capacity;i++)
//                if (character[i] != null)
//                    if (s.equals(character[i].getName())) return i;
//            return -1;
//        }
//        public int find(String name_1){
//            return find("Kevin Bacon",name_1);
//        }
//
//        public int find(String name_1,String name_2){
//            Queue<Circle> queue = new ConcurrentLinkedQueue<Circle>();
//            int[] bn = new int[capacity];
//            String[] cn = new String[capacity];
//            for (int i = 0; i < capacity; i++){
//                bn[i] = MAX_LINK;
//                cn[i] = "sorry, not found!\n";
//            }
//            int pivot_1 = findCharacterPivot(name_1);
//            bn[pivot_1] = 0;
//            cn[pivot_1] = "";
//            int pivot_2 = -1;
//            queue.add(character[pivot_1]);
//            while (!queue.isEmpty()) {
//                Circle tem = queue.poll();
//                tem.visit = VISITED;
//                Circle next = tem.next;
//                pivot_1 = findCharacterPivot(tem.name);
//                while (next != null) {
//                    pivot_2 = findCharacterPivot(next.name);
//                    Circle tem2 = character[pivot_2];
//                    if (tem2 != null && tem2.visit == UNVISITED) {
//                        queue.add(tem2);
//                    }
//                    if (bn[pivot_1] + 1 < bn[pivot_2]) {
//                        bn[pivot_2] = bn[pivot_1] + 1;
//                        cn[pivot_2] = cn[pivot_1] + next.name +
//                                " was in" + next.filmName + " with " +
//                                tem.name + "\n";
//                    }
//                    next = next.next;
//                }
//            }
//            int i = findCharacterPivot(name_2);
//            for (int t=0;t<=pivot;t++) {
//                pw.println(name_2 + "--->" + character[t].name+"\tBacon Number:"+bn[t]);
//                pw.println(cn[t]);
//            }
//            pw.close();
//            if (i > -1) {
//                res = cn[i];
//                return bn[i];
//            }
//            System.out.println(name_2+" not found!");
//            return -1;
//        }
//
//        public void txt(String name){
//            Queue<Circle> queue = new ConcurrentLinkedQueue<Circle>();
//            int[] bn = new int[capacity];
//            String[] cn = new String[capacity];
//            for (int i = 0; i < capacity; i++){
//                bn[i] = MAX_LINK;
//                cn[i] = "sorry, not found!\n";
//            }
//            int pivot_1 = findCharacterPivot(name);
//            bn[pivot_1] = 0;
//            cn[pivot_1] = "";
//            int pivot_2 = -1;
//            queue.add(character[pivot_1]);
//            while (!queue.isEmpty()) {
//                Circle tem = queue.poll();
//                tem.visit = VISITED;
//                Circle next = tem.next;
//                pivot_1 = findCharacterPivot(tem.name);
//                while (next != null) {
//                    pivot_2 = findCharacterPivot(next.name);
//                    Circle tem2 = character[pivot_2];
//                    if (tem2 != null && tem2.visit == UNVISITED) {
//                        queue.add(tem2);
//                    }
//                    if (bn[pivot_1] + 1 < bn[pivot_2]) {
//                        bn[pivot_2] = bn[pivot_1] + 1;
//                        cn[pivot_2] = cn[pivot_1] +
//                                "link is:" + tem.name + "\t " + next.name + "\t" + next.filmName + "\n";
//                    }
//                    next = next.next;
//                }
//            }
//            for (int t=0;t<=pivot;t++) {
//                if (bn[t] != MAX_LINK || bn[t]!=0) {
//                    pw.println(name + "--->" + character[t].name+"\tBacon Number:"+bn[t]);
//                    pw.println(cn[t]);
//                }
//            }
//        }
//
//        public void oneForAll() {
//            int number = character2.numNode;
//            System.out.println("一共有人数:"+ number);
//            for (int i = 0; i<= number; i++) {
//                Circle one = character[i];
//                String name = one.name;
//                System.out.println(i+"当前为："+ name+" 有："+one.pivot);
//                pw.println("下面是" + name + "的关系表");
//                txt(name);
//                System.out.println(name +"已完成！");
//            }
//            pw.close();
//        }
//        public int find2(String name_1,String name_2){
//            Queue<Circle> queue = new ConcurrentLinkedQueue<Circle>();
//            int[] bn = new int[capacity];
//            String[] cn = new String[capacity];
//            for (int i = 0; i < capacity; i++){
//                bn[i] = MAX_LINK;
//                cn[i] = "sorry, not found!\n";
//            }
//            int pivot_1 = findCharacterPivot(name_1);
//            bn[pivot_1] = 0;
//            cn[pivot_1] = "";
//            int pivot_2 = -1;
//            queue.add(character[pivot_1]);
//            while (!queue.isEmpty()) {
//                Circle tem = queue.poll();
//                tem.visit = VISITED;
//                Circle next = tem.next;
//                pivot_1 = findCharacterPivot(tem.name);
//                while (next != null) {
//                    pivot_2 = findCharacterPivot(next.name);
//                    Circle tem2 = character[pivot_2];
//                    if (tem2 != null && tem2.visit == UNVISITED) {
//                        queue.add(tem2);
//                    }
//                    if (bn[pivot_1] + 1 < bn[pivot_2]) {
//                        bn[pivot_2] = bn[pivot_1] + 1;
//                        cn[pivot_2] = cn[pivot_1] + next.name +
//                                " was in" + next.filmName + " with " +
//                                tem.name + "\n";
//                    }
//                    next = next.next;
//                }
//            }
//            int i = findCharacterPivot(name_2);
//            for (int t=0;t<=pivot;t++) {
//                pw.println(name_2 + "--->" + character[t].name+"\tBacon Number:"+bn[t]);
//                pw.println(cn[t]);
//            }
//            pw.close();
//            if (i > -1) {
//                res = cn[i];
//                return bn[i];
//            }
//            System.out.println(name_2+" not found!");
//            return -1;
//        }
//    }
//    public class Circle {
//        private String name = null;
//        private Circle next = null;
//        private String filmName = null;
//        private int visit = UNVISITED;//判断是否被访问
//        private Circle tail = this;
//        public int pivot = -1;
//
//        // 初始化构建
//        public Circle(String name){
//            this.name = name;
//            this.filmName = "warn: this is the beginning!";
//        }
//        // 关联建构
//        public Circle(String name,String filmName){
//            this.name = name;
//            this.filmName = filmName;
//        }
//        public Circle clear() {
//            next = null;
//            tail = this;
//            return this;
//        }
//
//        // setter and getter
//        public String getName() {
//            return name;
//        }
//
//        public void setName(String name) {
//            this.name = name;
//        }
//
//        public Circle getNext() {
//            return next;
//        }
//
//        public void setNext(Circle next) {
//            pivot++;
//            getTail().next = next;
//            setTail(getTail().next);
//        }
//
//        public String getFilmName() {
//            return filmName;
//        }
//
//        public void setFilmName(String filmName) {
//            this.filmName = filmName;
//        }
//
//        public int getVisit() {
//            return visit;
//        }
//
//        public void setVisit(int visit) {
//            this.visit = visit;
//        }
//
//        public Circle getTail() {
//            return tail;
//        }
//
//        public void setTail(Circle tail) {
//            this.tail = tail;
//        }
//    }
//    public void init(File file){
//        int row = 0;
//        String all = txt2String(file);
//        StringBuilder str;
//        for (int i = 0; i < all.length(); i++) {
//            str = new StringBuilder();
//            while (i < all.length() && all.charAt(i) != '\n') {
//                str.append(all.charAt(i));
//                i++;
//            }
//            row++;
//            String strip = str.toString().strip();
//            if (!Objects.equals(strip, "")) {
//                String[] arr = strip.split("/");
//                int len = arr.length;
//                String filmName = arr[0];
//                for (int k = 1; k < len; k++) {
//                    String name_1 = arr[k];
//                    for (int j = k; j < len; j++) {
//                        String name_2 = arr[j];
//                        link.addLink(name_1,name_2,filmName);
//                        link.addLink(name_2,name_1,filmName);
//                    }
//                }
//            }
//        }
//        this.setMaxLink(row);
//    }
//    public void init2(File file) throws FileNotFoundException {
//        int row = -1;
//        Scanner sc = new Scanner(file);
//        while (sc.hasNextLine()){
//            row++;
//            String strip = sc.nextLine().strip();
//            if (!Objects.equals(strip, "")) {
//                String[] arr = strip.split("/");
//                int len = arr.length;
//                String filmName = arr[0];
//                for (int k = 1; k < len; k++) {
//                    String name_1 = arr[k];
//                    for (int j = k; j < len; j++) {
//                        String name_2 = arr[j];
//                        link.addLink2(name_1,name_2,filmName);
//                        link.addLink2(name_2,name_1,filmName);
//                    }
//                }
//            }
//            System.out.println("处理完"+row);
//        }
//        this.setMaxLink(row);
//    }
//    public String txt2String(File file) {
//        StringBuilder result = new StringBuilder();
//        try {
//            BufferedReader br = new BufferedReader(new FileReader(file)); //构造一个BufferedReader类来读取文件
//            String s = null;
//            while((s = br.readLine()) != null) { //使用readLine方法，一次读一行
//                result.append(System.lineSeparator() + s);
//            }
//            br.close();
//        } catch(Exception e) {
//            e.printStackTrace();
//        }
//        return result.toString();
//    }
//    public void clear(){
//        link = new Link();
//    }
//    public int find(String name_1){
//        return link.find(name_1);
//    }
//    public int find(String name_1,String name_2){
//        return link.find(name_1,name_2);
//    }
//    public void setMaxLink(int MAX_LINK){
//        this.MAX_LINK = MAX_LINK;
//    }
//}

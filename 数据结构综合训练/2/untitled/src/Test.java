import java.io.File;
import java.io.FileNotFoundException;
import java.util.Scanner;

public class Test {
    public static void main(String[] args) throws FileNotFoundException {
        Graph graph = new Graph();
        Scanner sc = new Scanner(System.in);
        File file = new File("src/Complex.txt");
//        File file = new File("src/Simple.txt");
        graph.init2(file);
        System.out.println("初始化完成！\n请输入你要查询的人，生成文件至result_complex.txt");
        graph.link.oneForAll();
    }
}
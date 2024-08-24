package Trie;

import java.io.*;

public class Test {
    public static void main(String[] args) throws FileNotFoundException {
        Trie myTrie = new Trie();
        File file = new File("src/Trie/dictionary.txt");
        File file2 = new File("src/Trie/dic.txt");
        PrintWriter pw = new PrintWriter("src/Trie/dic_result.txt");
        String sum = txt2String(file);
        String sum2 = txt2String(file2);
        StringBuilder str;
        for (int i = 0; i < sum.length(); i++) {
            str = new StringBuilder();
            while (i < sum.length() && sum.charAt(i) != '\n') {
                str.append(sum.charAt(i));
                i++;
            }
            String strip = str.toString().strip();
            myTrie.insert(strip);
        }
        System.out.println("开始删除");
        long start = System.currentTimeMillis();
        for (int i = 0; i < sum2.length(); i++) {
            str = new StringBuilder();
            while (i < sum2.length() && sum2.charAt(i) != '\n') {
                str.append(sum2.charAt(i));
                i++;
            }
            String strip = str.toString().strip();
            myTrie.delete(strip);
        }
        long end = System.currentTimeMillis();
        System.out.println("用时:"+(end-start)+"ms");
        System.out.println("删除完毕");
        myTrie.showStr("");
    }
    public static String txt2String(File file) {
        StringBuilder result = new StringBuilder();
        try {
            BufferedReader br = new BufferedReader(new FileReader(file)); //构造一个BufferedReader类来读取文件
            String s = null;
            while((s = br.readLine()) != null) { //使用readLine方法，一次读一行
                result.append(System.lineSeparator() + s);
            }
            br.close();
        } catch(Exception e) {
            e.printStackTrace();
        }
        return result.toString();
    }
}

package T9Trie;

import java.io.BufferedReader;
import java.io.File;
import java.io.FileReader;
import java.util.Scanner;

public class Test {
    public static void main(String[] args) {
        T9Trie myT9Trie = new T9Trie();
        File file = new File("src/T9Trie/dictionary.txt");
        String sum = txt2String(file);
        StringBuilder str;
        for (int i = 0; i < sum.length(); i++) {
            str = new StringBuilder();
            while (i < sum.length() && sum.charAt(i) != '\n') {
                str.append(sum.charAt(i));
                i++;
            }
            String strip = str.toString().strip();
            String ns = changeNS(strip);
            myT9Trie.insert(ns,strip);
        }
        System.out.println("Enter “exit” to quit. ");
        String ns;
        int num;
        String[] res = null;
        int resPivot = 0;
        while (true) {
            System.out.println("Enter Key Sequence (or “#” for next word):");
            Scanner sc = new Scanner(System.in);
            String input = sc.next().strip();
            if (input.equals("exit")) break;
            else if (input.equals("#")){
                resPivot++;
                if (resPivot < res.length - 1) {
                    System.out.println(res[resPivot]);
                } else {
                    System.out.println("There are no more T9 words. ");
                }
                continue;
            }
            ns = getNS(input);
            num = getNum(input);
            res = myT9Trie.search(ns);
            resPivot = num;
            if (res == null||num>res.length-1) {
                System.out.println("There are no more T9 words. ");
            } else {
                System.out.println(res[num]);
            }
        }

    }
    public static String txt2String(File file) {
        StringBuilder result = new StringBuilder();
        try {
            BufferedReader br = new BufferedReader(new FileReader(file)); //构造一个BufferedReader类来读取文件
            String s;
            while((s = br.readLine()) != null) { //使用readLine方法，一次读一行
                result.append(System.lineSeparator() + s);
            }
            br.close();
        } catch(Exception e) {
            e.printStackTrace();
        }
        return result.toString();
    }
    public static String changeNS(String s){
        StringBuilder res = new StringBuilder();
        for (int i = 0; i < s.length(); i++) {
            char tem = s.charAt(i);
            if (tem<='c') {
                res.append(2);
            } else if (tem<='f') {
                res.append(3);
            } else if (tem<='i') {
                res.append(4);
            }else if (tem<='l') {
                res.append(5);
            }else if (tem<='o') {
                res.append(6);
            }else if (tem<='s') {
                res.append(7);
            }else if (tem<='v') {
                res.append(8);
            }else{
                res.append(9);
            }
        }
        return res.toString().strip();
    }

    public static String getNS(String s) {
        StringBuilder res = new StringBuilder();
        for (int i = 0; i < s.length(); i++) {
            char tem = s.charAt(i);
            if (tem<='9'&&tem>='2') {
                res.append(tem);
            }
        }
        return res.toString().strip();
    }
    public static int getNum(String s) {
        int res = 0;
        for (int i = 0; i < s.length(); i++) {
            char tem = s.charAt(i);
            if (tem=='#') {
                res++;
            }
        }
        return res;
    }

}

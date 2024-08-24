package BST;

import javax.swing.*;
import java.io.*;
import java.util.Scanner;

public class indexTest {
    public static void main(String[] args) throws FileNotFoundException {
        File file = new File("src/BST/article.txt");
        PrintWriter pw = new PrintWriter("src/BST/index_result.txt");
        BST<String, String> myBST = new BST<String, String>();
        Scanner sc = new Scanner(file);
        int row = -1;
        StringBuilder str = new StringBuilder();
        String sum = txt2String(file);
        for (int i = 0; i < sum.length(); i++) {
            str = new StringBuilder();
            while (i<sum.length()&&sum.charAt(i) != '\n') {
                str.append(sum.charAt(i));
                i++;
            }
            row++;
            str = new StringBuilder(str.toString().strip());
            System.out.println(row+ " " + str);
            String[] dic = str.toString().split(" ");
            for (String s:dic) {
                s = clean(s);
                if (s.equals("")) break;
                String preKey = myBST.search(s);
                if (preKey == null) {
                    myBST.insert(s, row + "");
                } else {
                    myBST.update(s,preKey+" "+row);
                }
            }
        }
        myBST.printInorder(pw);
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
    public static String clean(String s){
        String res = "";
        s = s.toLowerCase();
        int pivot = 0;
        char tem;
        for (int i = 0; i < s.length(); i++) {
            tem = s.charAt(i);
            if(tem<='z'&&tem>='a'){
                pivot=i;
                break;
            }
        }
        for (int i = pivot; i < s.length(); i++) {
            tem = s.charAt(i);
            if(tem<='z'&&tem>='a') res+=tem;
            else return res;
        }
        return res;
    }
}

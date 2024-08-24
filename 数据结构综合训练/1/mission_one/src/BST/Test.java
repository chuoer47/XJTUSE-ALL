package BST;

import java.io.File;
import java.io.FileNotFoundException;
import java.io.PrintWriter;
import java.util.Scanner;

public class Test {
    public static void main(String[] args) throws FileNotFoundException {
        PrintWriter pw = new PrintWriter("src/BST/file.txt");
        BST<String, String> myBST = new BST<String, String>();
        Scanner sc = new Scanner(new File("src/BST/BST_testcases.txt"));
        while (sc.hasNext()){
            String str = sc.nextLine().strip();
            char syn = str.charAt(0);
            String key = "";
            String value = "";
            switch (syn){
                case '+':{
                    int pivot = 2;
                    while(str.charAt(pivot)!=',') pivot++;
                    key = value = "";
                    for(int i=3;i<pivot-1;i++) key+=str.charAt(i);
                    for(int i=pivot+3;i<str.length()-3;i++) value+=str.charAt(i);
                    myBST.insert(key,value);
                    break;
                }
                case '#':{
                    myBST.showStructure(pw);
                    break;
                }
                case '-':{
                    key = "";
                    for(int i=3;i<str.length()-2;i++) key+=str.charAt(i);
                    value = myBST.remove(key);
                    if(value!=null) pw.println("remove success ---"+key+" "+value);
                    else pw.println("remove unsuccess ---"+key);
                    break;
                }
                case '=':{
                    int pivot = 2;
                    while(str.charAt(pivot)!=',') pivot++;
                    key = value = "";
                    for(int i=3;i<pivot-1;i++) key+=str.charAt(i);
                    for(int i=pivot+3;i<str.length()-3;i++) value+=str.charAt(i);
                    boolean flag = myBST.update(key,value);
                    if (flag) pw.println("update success ---"+key+" "+value);
                    break;
                }
                case '?':{
                    key = "";
                    for(int i=2;i<str.length()-2;i++) key+=str.charAt(i);
                    key = key.strip();
                    value = myBST.search(key);
                    if(value==null) pw.println("search unsuccess ---"+key);
                    else pw.println("search success ---"+key+" "+value);
                    break;
                }
                default:{
                    break;
                }
            }
        }
        pw.close();
    }
}

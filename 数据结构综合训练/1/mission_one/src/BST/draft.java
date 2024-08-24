package BST;

import java.io.File;
import java.io.FileNotFoundException;
import java.util.Scanner;

public class draft {
    public static void main(String[] args) throws FileNotFoundException {
        Scanner sc = new Scanner(new File("src/BST/article.txt"));
        int row = 0;
        while (sc.hasNextLine()){
            row++;
            String s = sc.nextLine();
            System.out.println(row + " "+s);
        }
    }
}

package Trie;

public class Trie {
    public static final int RED = 1;
    public static final int BLUE = 0;
    public Node root = new Node();
    private class Node{
        private int color = BLUE;
        public String res = "";
        public Node[] subNode = new Node[26];
        public Node(){}
        public Node(Node rt,char s){
            this.res = rt.res+s;
        }
        public void setBlue(){
            color = BLUE;
        }
        public void setRed(){
            color = RED;
        }
    }
    public void insert(String s){
        insert(root,s);
    }
    public void insert(Node rt, String s) {
        for (int i = 0; i < s.length(); i++) {
            char c = s.charAt(i);
            int pivot = c - 'a';
            if (rt.subNode[pivot] == null) {
                rt.subNode[pivot] = new Node(rt, c);
            }
            rt = rt.subNode[pivot];
            if (i == s.length() - 1) {
                rt.setRed();
            }
        }
    }
    public boolean search(String s){
        Node res = search(root, s);
        return res != null;
    }
    public Node search(Node rt,String s){
        for (int i = 0; i < s.length(); i++) {
            char c = s.charAt(i);
            int pivot = c - 'a';
            if (rt.subNode[pivot] == null) {
                return null;
            } else {
                rt = rt.subNode[pivot];
            }
        }
        return rt;
    }
    public void delete(String s) {
        delete(root,s);
    }
    public void delete(Node rt, String s) {
        Node res = search(rt, s);
        if (res == null) {
            return;
        } else {
            res.setBlue();
        }
    }
    public void showStr(String s){
        showStr(root,s);
    }
    public void showStr(Node rt,String s) {
        Node cur = search(rt,s);
        if (cur == null) {
            return;
        } else {
            showStr(cur);
        }
    }
    public void showStr(Node rt){
        for (int i = 0; i < 26; i++) {
            Node subNode = rt.subNode[i];
            if (subNode != null) {
                if (subNode.color == RED) {
                    System.out.print(subNode.res+" ");
                }
                showStr(subNode);
            }
        }
    }
}

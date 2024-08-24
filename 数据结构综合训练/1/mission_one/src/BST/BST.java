package BST;

import java.io.PrintWriter;

public class BST<K extends Comparable<K>,V>{
    private class Node{
        private K key;
        private V value;
        private Node left;
        private Node right;

        public Node(K key,V value,Node left,Node right){
            this.key = key;
            this.value = value;
            this.left = left;
            this.right = right;
        }
    }
    private Node root = null;
    private int numNode = 0;
    private int height = 0;
    public void insert(K key, V value){
        root = insertHelp(root,key,value);
    }
    public V remove(K key){
        V res = search(key);
        removeHelp(root,key);
        return res;
    }
    public V search(K key){
        Node pivot = searchHelp(root,key);
        if(pivot==null) return null;
        return pivot.value;
    }
    public boolean update(K key,V value){
        Node pivot = searchHelp(root,key);
        if(pivot==null) return false;
        pivot.value = value;
        return true;
    }
    public boolean isEmpty(){
        return root==null;
    }
    public void clear(){
        numNode = 0;
        height = 0;
        root = null;
    }
    public void showStructure(PrintWriter pw){
        height = getHeight(root,0);
        pw.println("-----------------------------");
        pw.printf("There are %d nodes in this BST.%nThe height of this BST is %d.%n",numNode,height);
        pw.println("-----------------------------");
    }
    public void printInorder(PrintWriter pw){
        // 中序遍历
        printInorderHelp(pw,root);
        pw.close();
    }
    public Node insertHelp(Node root,K key,V value){
        if (root==null){
            numNode++;
            return new Node(key,value,null,null);
        }
        if (root.key.compareTo(key)>0) root.left = insertHelp(root.left,key,value);
        else if (root.key.compareTo(key)<0) root.right= insertHelp(root.right,key,value);
        else root.value = value;
        return root;
    }
    public Node searchHelp(Node root, K key){
        if (root==null) return null;
        Node cur = root;
        while(cur!=null){
            if (cur.key.compareTo(key)==0) return cur;
            else if (cur.key.compareTo(key)<0) cur = cur.right;
            else cur = cur.left;
        }
        return null;
    }
    public Node removeHelp(Node root,K key){
        if (root==null) return null;
        if (root.key.compareTo(key)<0) root.right = removeHelp(root.right,key);
        else if (root.key.compareTo(key)>0) root.left = removeHelp(root.left,key);
        else{
            numNode--;
            if (root.left==null){
                if (this.root == root) this.root = root.right;
                return root.right;
            }
            else if (root.right==null){
                if (this.root == root) this.root =root.left;
                return root.left;
            }
            else {
                Node rightMinNode = minNode(root.right);
                root.key = rightMinNode.key;
                root.value = rightMinNode.value;
                root.right = delMinNode(root.right);
            }
        }
        return root;
    }
    public void printInorderHelp(PrintWriter pw,Node rt){
        if (rt == null) {
            return;
        } else {
            printInorderHelp(pw,rt.left);
            pw.printf("["+rt.key+" ---- < "+rt.value+" >]%n");
            printInorderHelp(pw,rt.right);
        }
    }
    public Node minNode(Node root){
        while(root.left != null) root = root.left;
        return root;
    }
    public Node delMinNode(Node root){
        if (root.left==null) return root.right;
        else {
            root.left = delMinNode(root.left);
            return root;
        }
    }
    public int getHeight(Node root,int height){
        if (root.left==null&&root.right==null)
            return height + 1;
        else if (root.left!=null&&root.right!=null)
            return Math.max(getHeight(root.right,height+1),getHeight(root.left,height+1));
        else{
            if (root.left!=null) return height+getHeight(root.left,1);
            else return height+getHeight(root.right,1);
        }
    }
}

package T9Trie;

public class T9Trie {
    public Node root = new Node();
    private class Node{
        private String[] data = null;
        private int dataPivot = -1;
        private Node[] subNode = new Node[8];
        public Node() {

        }
        public void add(String s){
            if (data == null)
                data = new String[1];
            else if (dataPivot == data.length - 1)
                resize();
            data[++dataPivot] = s;
        }
        private void resize(){
            String[] tem = new String[data.length*2];
            int temPivot = 0;
            for (String s:data) {
                tem[temPivot++] = s;
            }
            data = tem;
        }
    }
    public void insert(String ns,String ss){
        insert(root,ns,ss);
    }
    public void insert(Node rt,String ns,String ss){
        for (int i = 0; i < ns.length(); i++) {
            char c = ns.charAt(i);
            int pivot = c - '2';
            if (rt.subNode[pivot] == null) {
                rt.subNode[pivot] = new Node();
            }
            rt = rt.subNode[pivot];
            if (i == ns.length() - 1) {
                rt.add(ss);
            }
        }
    }
    public String[] search(String ns){
        return search(root,ns);
    }
    public String[] search(Node rt,String ns){
        for (int i = 0; i < ns.length(); i++) {
            char c = ns.charAt(i);
            int pivot = c - '2';
            if (rt.subNode[pivot] == null) {
                return null;
            } else {
                rt = rt.subNode[pivot];
            }
        }
        return rt.data;
    }
}

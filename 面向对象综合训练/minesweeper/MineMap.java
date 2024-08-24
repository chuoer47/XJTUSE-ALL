package minesweeper;

/** 这个类主要用来存储地雷在单元格中的位置，目前这个类只是一个示意，所以地雷都是固定位置。 */
/** 需要更改为可以随机的分布地雷的函数方法 */
public class MineMap {
    int numMines;
    boolean[][] isMined = new boolean[GameBoardPanel.ROWS][GameBoardPanel.COLS];
    public MineMap(){}
    public void newMineMap(int row, int col,int numMines){
        this.numMines = numMines;
        int num = 0;
        // 随机生成地雷，但是存在缺点，当地雷数字较大的时候，随机生成的可能很慢
        while (num<this.numMines){
            int x = (int) (Math.random()*row);
            int y = (int) (Math.random()*col);
            if (!isMined[x][y]){
                isMined[x][y] = true;
                num++;
            }
        }
    }
}

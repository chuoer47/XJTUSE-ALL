package minesweeper;
import java.awt.*;
import javax.swing.*;
import java.awt.event.*;

//这个类的作用就是充当“棋盘”
public class GameBoardPanel extends JPanel {
    private static final long serialVersionUID = 1L;
    // 设定了“棋盘”中有多少个Cell对象
    public static final int ROWS = 10;
    public static final int COLS = 10;
    // 每一个Cell对象的尺寸大小，依次大小再去计算“棋盘”的大小
    public static final int CELL_SIZE = 60;
    public static final int CANVAS_WIDTH = CELL_SIZE * COLS;
    public static final int CANVAS_HEIGHT = CELL_SIZE * ROWS;

    Cell cells[][] = new Cell[ROWS][COLS];
    int numMines = 10;

    public GameBoardPanel(){
        super.setLayout(new GridLayout(ROWS, COLS, 1, 1));
        for(int row = 0; row < ROWS; ++row){
            for(int col = 0; col < COLS; ++col){
                cells[row][col] = new Cell(row, col);
                super.add(cells[row][col]);
            }
        }
        // [TODO 3] 为所有的Cell单元对象创建一个共享的鼠标事件监听器
        CellMouseListener listener = new CellMouseListener();
        // [TODO 4] 通过下面的循环，将每个Cell对象的鼠标事件监听器对象设为listener
        for(int row = 0; row < ROWS; ++row){
            for(int col = 0; col <COLS; ++col){
                cells[row][col].addMouseListener(listener);
            }
        }
        super.setPreferredSize(new Dimension(CANVAS_WIDTH, CANVAS_HEIGHT));
    }

    // 初始化一个新的游戏
    public void newGame(){
        // 通过MineMap获得新游戏中的地雷数据的布局
        MineMap mineMap = new MineMap();
        mineMap.newMineMap(ROWS,COLS,numMines);
        // 根据mineMap中的数据初始化每个Cell单元对象,numMines)
        for(int row = 0; row < ROWS; ++row){
            for(int col = 0; col < COLS; ++col){
                cells[row][col].newGame(mineMap.isMined[row][col]);
            }
        }
    }
    // 获得[srcRow, srcCol]Cell单元对象周围的8个邻居的地雷总数
    private int getSurroundingMines(int srcRow, int srcCol){
        int numMines = 0;
        for(int row = srcRow-1; row <= srcRow+1; ++row){
            for(int col = srcCol-1; col <= srcCol+1; ++col){
                if(row >= 0 && row < ROWS && col >= 0 && col < COLS)
                    if(cells[row][col].isMined) numMines++;
            }
        }
        return numMines;
    }
    // 对[srcRow, srcCol]Cell单元对象执行挖雷操作
    // 如果该单元格对象中的标记的雷的数量为0，那么就自动递归对其周围8个邻居执行挖雷操作
    private void revealCell(int srcRow, int srcCol){
        int numMines = getSurroundingMines(srcRow, srcCol);
        cells[srcRow][srcCol].setText(numMines + "");
        cells[srcRow][srcCol].isRevealed = true;
        cells[srcRow][srcCol].paint();
        if(numMines == 0){
            for(int row = srcRow-1; row <= srcRow+1; ++row){
                for(int col = srcCol-1; col <= srcCol+1; ++col){
                    if(row >= 0 && row < ROWS && col >= 0 && col < COLS)
                        if(!cells[row][col].isRevealed) revealCell(row, col);
                }
            }
        }
    }
    // 用来判断玩家是否已经赢得此次游戏
    public boolean hasWon(){
        // 如果将所有单元格都成功执行了挖雷操作或者所有的地雷都被标记
        // ...
        int count = 0; // 统计未被点击的格子
        int flag = 0; // 统计插旗的格子
        for (int i=0;i<ROWS;i++){
            for (int j=0;j<COLS;j++){
                if (!cells[i][j].isRevealed) count++;
                if (cells[i][j].isFlagged) flag++;
            }
        }
        if (count==numMines) return true;
        else if (flag==numMines) return true;
        return false;
    }
    // [TODO 2] 定义一个内部类，该类的作用为鼠标事件监听器
    private class CellMouseListener extends MouseAdapter{
        public void mouseClicked(MouseEvent e){
            // 获得触发此次鼠标事件的Cell对象
            Cell sourceCell = (Cell)e.getSource();
            // 获得鼠标事件的类型，MouseEvent.BUTTON1为单击鼠标左键
            if(e.getButton() == MouseEvent.BUTTON1)
                // [TODO 5] 如果当前Cell对象里面有地雷，则游戏结束；否则对该Cell对象执行挖雷操作
                if(sourceCell.isMined){
                    System.out.println("Game Over");
                    sourceCell.setText("*");
                }
                else if(sourceCell.isFlagged){
                    ;
                }
                else{
                    revealCell(sourceCell.row, sourceCell.col);
                }
            else
                if(e.getButton() == MouseEvent.BUTTON3){ //MouseEvent.BUTTON3为单击鼠标右键
                    // [TODO 6] 如果该Cell对象上插了旗子，那么就去掉旗子；否则将该Cell对象打上旗子的标记。
                    if (sourceCell.isFlagged){
                        sourceCell.isFlagged = false;
                        sourceCell.setText("");
                    }
                    else{
                        sourceCell.isFlagged = true;
                        sourceCell.setText("!");
                    }
                }
            // [TODO 7] 当对Cell单元格对象执行了挖雷操作之后判断玩家是否赢得该游戏
            // ...
            if (hasWon()){
                System.out.println("You win!!");
            }

        }
    }
}

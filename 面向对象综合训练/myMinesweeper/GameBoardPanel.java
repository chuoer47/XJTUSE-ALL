package myMinesweeper;

import javax.swing.*;
import java.awt.*;
import java.awt.event.MouseAdapter;
import java.awt.event.MouseEvent;
import java.io.Serial;
import java.util.Objects;

import static myMinesweeper.Data.*;

//这个类的作用就是充当“棋盘”
public class GameBoardPanel extends JPanel {
    @Serial
    private static final long serialVersionUID = 1L;
    public int ROWS;
    public int COLS;
    public int canvasWidth;
    public int canvasHeight;
    // 设定了“棋盘”中有多少个Cell对象
    private Cell[][] cells;
    public int numMines;
    private int remainNumMines;
    private JLabel myText;// 计算剩余地雷的
    private Timer myTime;// 控制计时器开始停止的
    public MineMap mineMap;

    public GameBoardPanel(){
        this(Easy);
    }
    public GameBoardPanel(int mode){
        switch (mode){
            case Easy -> {
                this.ROWS = EASY_ROWS;
                this.COLS = EASY_COLS;
                this.numMines = EASY_MINES;
                this.canvasWidth = this.ROWS * EASY_SIZE;
                this.canvasHeight = this.COLS * EASY_SIZE;
            }
            case Intermediate -> {
                this.ROWS = MIDDLE_ROWS;
                this.COLS = MIDDLE_COLS;
                this.numMines = MIDDLE_MINES;
                this.canvasWidth = this.ROWS * MIDDLE_SIZE;
                this.canvasHeight = this.COLS * MIDDLE_SIZE;
            }
            case Difficult -> {
                this.ROWS = DIFFICULT_ROWS;
                this.COLS = DIFFICULT_COLS;
                this.numMines = DIFFICULT_MINES;
                this.canvasWidth = this.ROWS * DIFFICULT_SIZE;
                this.canvasHeight = this.COLS * DIFFICULT_SIZE;
            }
        }
        remainNumMines = numMines;
        cells = new Cell[ROWS][COLS];
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
        super.setPreferredSize(new Dimension(canvasWidth, canvasHeight));
    }

    // 初始化一个新的游戏
    public void newGame(){
        // 通过MineMap获得新游戏中的地雷数据的布局
        mineMap = new MineMap();
        mineMap.newMineMap(ROWS,COLS,numMines);
        // 根据mineMap中的数据初始化每个Cell单元对象,numMines)
        for(int row = 0; row < ROWS; ++row){
            for(int col = 0; col < COLS; ++col){
                cells[row][col].newGame(mineMap.isMined[row][col]);
                cells[row][col].setIcon(new ImageIcon());;
            }
        }
        freshRemainMined();
        MyTimer.restart();
    }
    public void resetGame(){
        for(int row = 0; row < ROWS; ++row){
            for(int col = 0; col < COLS; ++col){
                cells[row][col].newGame(mineMap.isMined[row][col]);
                cells[row][col].setIcon(new ImageIcon());;
            }
        }
        remainNumMines = numMines;
        freshRemainMined();
        MyTimer.restart();
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
        if (numMines!=0) cells[srcRow][srcCol].setText(numMines + "");
        cells[srcRow][srcCol].isRevealed = true;
        cells[srcRow][srcCol].paint();
        if(numMines == 0){
            for(int row = srcRow-1; row <= srcRow+1; ++row){
                for(int col = srcCol-1; col <= srcCol+1; ++col){
                    if(row >= 0 && row < ROWS && col >= 0 && col < COLS)
                        if(!cells[row][col].isRevealed&&!cells[row][col].isFlagged) revealCell(row, col);
                }
            }
        }
    }
    // 用来判断玩家是否已经赢得此次游戏
    public boolean hasWon(){
        // 如果将所有单元格都成功执行了挖雷操作或者所有的地雷都被标记
        int count = 0; // 统计未被点击的格子
        int flag = 0; // 统计插旗的格子
        for (int i=0;i<ROWS;i++){
            for (int j=0;j<COLS;j++){
                if (!cells[i][j].isRevealed) count++;
                if (cells[i][j].isFlagged&&cells[i][j].isMined) flag++;
            }
        }
        if (count==numMines) return true;
        else if (flag==numMines) return true;
        return false;
    }
    // 返回剩余地雷个数
    public int hasRemainMines(){
        return remainNumMines;
    }
    private void freshRemainMined(){
        myText.setText("remain mines："+hasRemainMines());
    }

    // 设置各种变量
    public void setRemainMines(JLabel myText){
        this.myText = myText;
    }
    public void setMyTime(Timer myTime){
        this.myTime = myTime;
    }

    // [TODO 2] 定义一个内部类，该类的作用为鼠标事件监听器
    private class CellMouseListener extends MouseAdapter{
        private void lock(){
            for(int row = 0; row < ROWS; ++row)
                for(int col = 0; col < COLS; ++col)
                    cells[row][col].isCanClick = false;
        }
        public void mouseClicked(MouseEvent e){
            // 获得触发此次鼠标事件的Cell对象
            Cell sourceCell = (Cell)e.getSource();
            if (!sourceCell.isCanClick) return;
            // 获得鼠标事件的类型，MouseEvent.BUTTON1为单击鼠标左键
            if(e.getButton() == MouseEvent.BUTTON1)
                // [TODO 5] 如果当前Cell对象里面有地雷，则游戏结束；否则对该Cell对象执行挖雷操作
                if(sourceCell.isMined&&!sourceCell.isFlagged){
                    sourceCell.setIcon(new ImageIcon(Objects.requireNonNull(getClass().getResource("mine.png"))));
                    myText.setText("YOU LOSE...");
                    myTime.stop();
                    lock();
                }
                else if(sourceCell.isFlagged){ //被标记的格子无法点开
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
                        remainNumMines++;
                        freshRemainMined();
                        sourceCell.setIcon(new ImageIcon());
                    }
                    else if(sourceCell.isRevealed){
                        ;
                    }
                    else{
                        sourceCell.isFlagged = true;
                        remainNumMines--;
                        freshRemainMined();
                        sourceCell.setIcon(new ImageIcon(Objects.requireNonNull(getClass().getResource("flag.png"))));
                    }
                }
            // [TODO 7] 当对Cell单元格对象执行了挖雷操作之后判断玩家是否赢得该游戏
            if (hasWon()){
                myTime.stop();
                lock();
                myText.setText("YOU WIN!!");
            }
        }
    }
}
package minesweeper;
import java.awt.Color;
import java.awt.Font;
import javax.swing.JButton;

/**
 * 类Cell是对JButton的类定制（也就是JButton的一个子类，其目的是表示扫雷游戏的一个单元格；
 * 该类中定义了row/column属性以及相关状态函数。
 */
public class Cell extends JButton{
    // 为Cell单元格定义若干颜色和字体常量
    // 这些常量将随着Cell单元格的状态变化而被使用
    private static final long serialVersionUID = 1L;  // to prevent serial warning
    public static final Color BG_NOT_REVEALED = Color.GREEN;
    public static final Color FG_NOT_REVEALED = Color.RED;    // flag, mines
    public static final Color BG_REVEALED = Color.DARK_GRAY;
    public static final Color FG_REVEALED = Color.YELLOW;     // number of mines
    public static final Font FONT_NUMBERS = new Font("Monospaced", Font.BOLD, 20);

    // 定义Cell对象的属性，比如row和col值用来表示单元格在最终“棋盘”上的位置定位
    int row, col;
    boolean isRevealed; // 标记是否已经被挖出？
    boolean isMined;    // 标记是否是地雷？
    boolean isFlagged;  // 标记是否被玩家插上了一个小红旗

    public Cell(int row, int col){
        this.row = row;
        this.col = col;
        super.setFont(FONT_NUMBERS);
    }

    public void newGame(boolean isMined){
        this.isRevealed = false;
        this.isFlagged = false;
        this.isMined = isMined;
        super.setEnabled(true);
        super.setText("");
        paint();
    }
    /** 基于单元格的状态进行绘制 */
    public void paint(){
        super.setForeground(isRevealed? FG_REVEALED: FG_NOT_REVEALED);
        super.setBackground(isRevealed? BG_REVEALED: BG_NOT_REVEALED);
    }
}

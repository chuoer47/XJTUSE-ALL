package myMinesweeper;

import javax.swing.*;
import java.awt.*;
import java.io.Serial;

import static myMinesweeper.Data.*;

/**
 * 挖雷游戏的主程序。
 * 单击鼠标左键对单元格执行挖雷操作。
 * 单击鼠标右键用来对单元格执行添加标记，或者移除标记，标记疑似有地雷的单元格。
 * 如果所有没有地雷的单元格都执行了挖雷操作，那么玩家赢得游戏。
 * 如果对某个有地雷的单元格执行了挖雷操作，那么玩家输。
 */
public class MineSweeperMain extends JFrame {
    @Serial
    private static final long serialVersionUID = 1L;
    private GameBoardPanel board;
    public MineSweeperMain(){
        this(Easy);
    }
    public MineSweeperMain(int mode) {
        board = new GameBoardPanel(mode);
        setJMenuBar(new Menu(board));//给窗体添加菜单--注意：用的不是add

        // 容器布局
        this.setLayout(new BorderLayout());
        this.add(board, BorderLayout.CENTER);
        this.add(new Tool(board),BorderLayout.NORTH);

        // 初始化，启动游戏使其可见
        board.newGame();
        pack(); // Pack the UI components, instead of setSize()
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        setTitle("Minesweeper");
        setVisible(true);
    }

    public static void main(String[] args){
        // [TODO 1] 使用安全的方式启动下面的构造函数
        new MineSweeperMain();
    }
}

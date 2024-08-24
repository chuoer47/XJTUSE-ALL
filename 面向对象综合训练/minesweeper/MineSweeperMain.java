package minesweeper;

import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

/**
 * 挖雷游戏的主程序。
 * 单击鼠标左键对单元格执行挖雷操作。
 * 单击鼠标右键用来对单元格执行添加标记，或者移除标记，标记疑似有地雷的单元格。
 * 如果所有没有地雷的单元格都执行了挖雷操作，那么玩家赢得游戏。
 * 如果对某个有地雷的单元格执行了挖雷操作，那么玩家输。
 */
public class MineSweeperMain extends JFrame {
    private static final long serialVersionUID = 1L;
    GameBoardPanel board = new GameBoardPanel();
    JButton btnNewGame = new JButton("New Game");
    public MineSweeperMain(){
        Container cp = this.getContentPane();
        cp.setLayout(new BorderLayout());
        cp.add(board, BorderLayout.CENTER);
        cp.add(btnNewGame, BorderLayout.SOUTH);
        // 使用匿名类的方式为btnNewGame按钮添加Action事件监听器
        btnNewGame.addActionListener(new ActionListener(){
            public void actionPerformed(ActionEvent event){
                board.newGame();
            }
        });
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

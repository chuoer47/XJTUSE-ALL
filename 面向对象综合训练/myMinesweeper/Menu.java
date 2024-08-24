package myMinesweeper;

import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

public class Menu extends JMenuBar {
    private static JMenuItem btnNewGame = new JMenuItem("New Game");//创建菜单对象
    private static JMenuItem  btnResetGame = new JMenuItem ("Reset Game");//创建菜单对象
    private static JMenuItem  btnExitGame = new JMenuItem ("Exit");//创建菜单对象
    private GameBoardPanel board;
    private JMenu menu = new JMenu("File");
    public Menu(GameBoardPanel board){
        this.board = board;
        this.add(menu);
        btnNewGame.addActionListener(new ActionListener() {// 使用匿名类的方式为btnNewGame按钮添加Action事件监听器
            @Override
            public void actionPerformed(ActionEvent e) {
                board.newGame();
            }
        });
        menu.add(btnNewGame);
        btnResetGame.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                board.resetGame();
            }
        });
        menu.add(btnResetGame);
        btnExitGame.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                System.exit(0);
            }
        });
        menu.add(btnExitGame);
    }
}

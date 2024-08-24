package myMinesweeper;

import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

import static myMinesweeper.Data.*;

public class Play extends JFrame {
    /**
     * 这是初始界面程序
     * 包含了三个按钮以及对应的事件链
     * */
    private ActionListener btnAllListener = new ActionListener() {
        @Override
        public void actionPerformed(ActionEvent e) {
            Select select = (Select) e.getSource();
            new MineSweeperMain(select.getMode());
        }
    };
    public Play(){
        setLayout(new GridLayout(3,1));
        setDefaultCloseOperation(WindowConstants.EXIT_ON_CLOSE);
        this.setSize(500,500);
        // 布置按钮选择
        for(Select btn:btnAll){
            btn.addActionListener(btnAllListener);
            this.add(btn);
        }
        this.setVisible(true);
        this.setTitle("Minesweeper");
    }

    public static void main(String[] args) {
        new Play();
    }
}

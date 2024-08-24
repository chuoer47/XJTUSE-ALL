package myMinesweeper;

import javax.swing.*;
import java.awt.*;

public class Tool extends JPanel {
    /**
     * 这个类包含了统计地雷个数和计时两大工具
     * */
    JLabel myTime = MyTimer.getTimeLabel();
    JLabel myMines = new JLabel("",JLabel.CENTER);
    private GameBoardPanel board;
    public Tool(GameBoardPanel board){
        this.board = board;
        setLayout(new GridLayout(1,2));
        board.setRemainMines(myMines);
        board.setMyTime(MyTimer.time);
        this.add(myMines);
        this.add(myTime);
    }
}

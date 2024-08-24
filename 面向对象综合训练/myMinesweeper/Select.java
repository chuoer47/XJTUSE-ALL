package myMinesweeper;

import javax.swing.*;
import java.awt.*;

import static myMinesweeper.Data.*;

public class Select extends JButton {
    /**
     * 这个类是界面选择难度的按钮
     * 变量为难度模式（mode）和按钮文本（s）
     * */
    public static final Font FONT_NUMBERS = new Font("Monospaced", Font.BOLD, 35);
    private int mode;
    private String s;
    public Select(int mode,String s){
        this.mode = mode;
        this.s = s;
        super.setFont(FONT_NUMBERS);
        super.setEnabled(true);
        super.setText(this.s);
        super.setForeground(SEL_FG_COLOR);
        super.setBackground(SEL_BG_COLOR);
    }
    public int getMode(){
        return this.mode;
    }
}

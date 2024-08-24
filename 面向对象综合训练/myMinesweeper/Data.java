package myMinesweeper;

import java.awt.*;

public class Data {
    /** 棋盘的参数
     * */
    // 记录不同模式的棋盘大小,地雷数目,布局尺寸
    // 简单模式
    public static final int EASY_ROWS = 9;
    public static final int EASY_COLS = 9;
    public static final int EASY_MINES = 10;
    public static final int EASY_SIZE = 60;

    // 中等模式
    public static final int MIDDLE_ROWS = 12;
    public static final int MIDDLE_COLS = 12;
    public static final int MIDDLE_MINES = 24;
    public static final int MIDDLE_SIZE = 60;

    // 困难模式
    public static final int DIFFICULT_ROWS = 12;
    public static final int DIFFICULT_COLS = 12;
    public static final int DIFFICULT_MINES = 36;
    public static final int DIFFICULT_SIZE = 60;

    /** 单元格的参数
    * */
    public static final Color BG_NOT_REVEALED = Color.GRAY;
    public static final Color FG_NOT_REVEALED = Color.WHITE;    // flag, mines
    public static final Color BG_REVEALED = Color.WHITE;
    public static final Color FG_REVEALED = Color.BLACK;     // number of mines

    /** 难度选择参数
     * */
    public static final int SELECT_WIDTH = 120;
    public static final int SELECT_HEIGHT = 40;
    public static final int Easy = 1;
    public static final int Intermediate = 2;
    public static final int Difficult = 3;

    /**
     * 界面的参数与组件
     * */
    public static final Select[] btnAll = {new Select(Easy,"Easy")
            ,new Select(Intermediate,"Intermediate")
            ,new Select(Difficult,"Difficult")};
    public static final Color SEL_FG_COLOR = Color.RED;
    public static final Color SEL_BG_COLOR = Color.CYAN;

}

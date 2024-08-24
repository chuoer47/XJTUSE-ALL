package myMinesweeper;

import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

public class MyTimer{
    public static Timer time;
    private static JLabel timeLabel = null;
    private static final String INITIAL_LABEL_TEXT = "00:00:00";
    // 记录程序开始时间
    private static long programStart = System.currentTimeMillis();
    //时间显示
    public static JLabel getTimeLabel() {
        if (timeLabel == null) {
            timeLabel = new JLabel(INITIAL_LABEL_TEXT,JLabel.CENTER);
            timeLabel.setFont(new Font("微软雅黑", Font.BOLD, 15));
            timeLabel.setForeground(Color.BLACK);
            timeLabel.setBackground(Color.PINK);
            time = new Timer(1000,new ActionListener() {
                @Override
                public void actionPerformed(ActionEvent arg0) {
                    long elapsed = System.currentTimeMillis() - programStart;
                    timeLabel.setText(format(elapsed));
                }
            });
            time.start();
        }
        return timeLabel;
    }
    public static void restart(){
        programStart = System.currentTimeMillis();
        time.start();
    }

    private static String format(long elapsed) {
        int hour, minute, second, milli;
        milli = (int) (elapsed % 1000);
        elapsed = elapsed / 1000;
        second = (int) (elapsed % 60);
        elapsed = elapsed / 60;
        minute = (int) (elapsed % 60);
        elapsed = elapsed / 60;
        hour = (int) (elapsed % 60);
        return String.format("%02d:%02d:%02d", hour, minute, second);
    }
}

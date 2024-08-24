import java.awt.*;
import java.awt.event.*;
import javax.swing.*;

public class MyFirstActionListener extends JFrame {
    final static long serialVersionUID = 1L;
    Container container = getContentPane();
    JButton button = new JButton("点击我");

    class ButtonListener implements ActionListener {
        int x = 0;

        public void actionPerformed(ActionEvent arg0) {
            MyFirstActionListener.this.button.setText("我被点机了" + (++x) + "次");
        }
    }

    public MyFirstActionListener()
    {
        super("JFrame窗体");
        this.setBounds(200, 100, 200, 200);
        button.addActionListener(new ButtonListener());
        container.add(button);
        this.setVisible(true);
    }

    public static void main(String[] args)
    {
        new MyFirstActionListener();
    }
}

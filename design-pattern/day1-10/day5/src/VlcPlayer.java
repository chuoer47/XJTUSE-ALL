public class VlcPlayer implements AdvancedMediaPlayer {
    @Override
    public void playVlc(String fileName) {
        System.out.println("play vlc:" + fileName);
    }

    @Override
    public void playMp4(String fileName) {
        return; // 不实现
    }
}

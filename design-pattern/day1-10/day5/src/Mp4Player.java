public class Mp4Player implements AdvancedMediaPlayer {
    @Override
    public void playVlc(String fileName) {
        return;
    }

    @Override
    public void playMp4(String fileName) {
        System.out.println("play mp4:" + fileName);
    }
}

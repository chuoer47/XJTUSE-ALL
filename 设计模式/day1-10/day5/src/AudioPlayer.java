public class AudioPlayer implements MediaPlayer {
    MediaPlayer mediaPlayer;

    @Override
    public void play(String audioType, String fileName) {
        if (audioType.equals("mp4") || audioType.equals("vlc")) {
            mediaPlayer = new MediaAdapter(audioType);
            mediaPlayer.play(audioType, fileName);
        } else if (audioType.equals("mp3")) {
            System.out.println("play mp3:" + fileName);
        } else {
            System.out.println("cannot play this file.");
        }
    }
}

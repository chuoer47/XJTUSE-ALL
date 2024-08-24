public class ProxyImage implements Image{
    private String filename;



    public class ProxyImageSource{
        private static RealImage realImage;

        public static void setRealImage(String filename) {
            ProxyImageSource.realImage = new RealImage(filename);
        }
    }

    public ProxyImage(String filename) {
        this.filename = filename;
        ProxyImageSource.setRealImage(filename);
    }

    @Override
    public void display() {
        ProxyImageSource.realImage.display();
    }
}

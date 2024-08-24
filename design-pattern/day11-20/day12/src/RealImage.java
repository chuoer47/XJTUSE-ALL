public class RealImage implements Image{
    private String filename;

    public RealImage(String filename) {
        this.filename = filename;
        loadFileDisk(filename);
    }

    @Override
    public void display() {
        System.out.println("showing:"+filename);
    }
    private void loadFileDisk(String filename){
        System.out.println("disking:"+filename);
    }
}

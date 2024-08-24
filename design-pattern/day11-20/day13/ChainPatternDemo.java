public class ChainPatternDemo {
    public static void main(String[] args) {
        AbstractLogger chainLogger = getChainLogger();
        chainLogger.logMessage(AbstractLogger.INFO, "This is an information.");

        chainLogger.logMessage(AbstractLogger.DEBUG,
                "This is a debug level information.");

        chainLogger.logMessage(AbstractLogger.ERROR,
                "This is an error information.");
    }
    public static AbstractLogger getChainLogger(){
        AbstractLogger consoleLogger = new ConsoleLogger(AbstractLogger.DEBUG);
        AbstractLogger errorLogger = new ErrorLogger(AbstractLogger.ERROR);
        AbstractLogger fileLogger = new FileLogger(AbstractLogger.INFO);
        errorLogger.setNextLogger(consoleLogger);
        consoleLogger.setNextLogger(fileLogger);
        return errorLogger;
    }
}

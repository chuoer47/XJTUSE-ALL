import java.sql.DataTruncation;
import java.util.ArrayList;
import java.util.List;
import java.util.logging.Logger;

public class Employee {
    private String name;
    private String dept;
    private int salary;
    private List<Employee> subordinates = new ArrayList<Employee>();

    public Employee(String name, String dept, int salary) {
        this.name = name;
        this.dept = dept;
        this.salary = salary;
    }

    public boolean add(Employee employee) {
        try {
            subordinates.add(employee);
            return true;
        } catch (Exception e) {
            Logger.getLogger(e.toString());
            return false;
        }
    }

    public boolean remove(Employee employee) {
        try {
            subordinates.remove(employee);
            return true;
        } catch (Exception e) {
            Logger.getLogger(e.toString());
            return false;
        }
    }

    @Override
    public String toString() {
        return "Employee{" +
                "name='" + name + '\'' +
                ", dept='" + dept + '\'' +
                ", salary=" + salary +
                '}';
    }

    public List<Employee> getSubordinates() {
        return subordinates;
    }


}

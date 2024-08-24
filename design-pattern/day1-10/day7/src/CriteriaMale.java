import java.util.ArrayList;
import java.util.List;

public class CriteriaMale implements Criteria {


    @Override
    public List<Person> meetCriteria(List<Person> personList) {
        List<Person> res = new ArrayList<Person>();
        for (Person person :
                personList) {
            if (person.getGender().equalsIgnoreCase("male")) {
                res.add(person);
            }
        }
        return res;
    }
}

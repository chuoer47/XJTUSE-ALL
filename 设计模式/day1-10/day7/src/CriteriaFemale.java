import java.util.ArrayList;
import java.util.List;

public class CriteriaFemale implements Criteria {


    @Override
    public List<Person> meetCriteria(List<Person> personList) {
        List<Person> res = new ArrayList<Person>();
        for (Person person :
                personList) {
            if (person.getGender().equalsIgnoreCase("female")) {
                res.add(person);
            }
        }
        return res;
    }
}

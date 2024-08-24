import java.util.List;

public class CriteriaOr implements Criteria {
    Criteria criteriaFirst;
    Criteria criteriaSecond;

    public CriteriaOr(Criteria criteriaFirst, Criteria criteriaSecond) {
        this.criteriaFirst = criteriaFirst;
        this.criteriaSecond = criteriaSecond;
    }

    @Override
    public List<Person> meetCriteria(List<Person> personList) {
        List<Person> personList1 = criteriaFirst.meetCriteria(personList);
        List<Person> personList2 = criteriaSecond.meetCriteria(personList);
        for (Person p : personList1
        ) {
            if (!personList2.contains(p)) {
                personList2.add(p);
            }
        }
        return personList2;
    }
}

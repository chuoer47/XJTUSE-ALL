import java.util.List;

public class CriteriaAnd implements Criteria {
    Criteria criteriaFirst;
    Criteria criteriaSecond;

    public CriteriaAnd(Criteria criteriaFirst, Criteria criteriaSecond) {
        this.criteriaFirst = criteriaFirst;
        this.criteriaSecond = criteriaSecond;
    }

    @Override
    public List<Person> meetCriteria(List<Person> personList) {
        return criteriaSecond.meetCriteria(criteriaFirst.meetCriteria(personList));
    }
}

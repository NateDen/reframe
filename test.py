import pandas as pd
import pytest
import reframe

@pytest.fixture
def r1():
    d = {'cats': ['siamese', 'persian'], 'dogs': ['bulldog', 'pitbull']}
    df = pd.DataFrame(data=d)
    return Relation(df)
    

def case1():
    faculty = Relation('../faculty.csv')
    students = Relation('../students.csv')
    answer = pd.read_csv('case1.csv')
    sjoin = students.semi_join(faculty)
    assert answer.equals(sjoin)



def case2():
    married = Relation('../married.csv')
    homes = Relation('../homes.csv')
    answer = pd.read_csv('case2.csv')
    sjoin = married.semi_join(homes)
    assert answer.equals(sjoin)


if __name__ == "__main__":
    r1()
    case1()
    case2()
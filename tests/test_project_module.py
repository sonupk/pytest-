
import math

from my_project import project_module



def test_rolling_average():
    result = project_module.rolling_average([1,2,3,4,5,6],3)
    assert result == [2.0,3.0,4.0,5.0]



def test_sqrt():
    num = 25
    assert math.sqrt(num) == 5


    
    
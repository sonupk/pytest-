def add(a, b):
    return a + b
def test_add():
 assert add(1,2) == 3
 assert add(0,0) == 0
 assert add(-1,1) == 0

 print("Result of add(3,4):",add(3,4))


def count_letters(text):
    return len(text)
def test_count_letters():
    assert count_letters("Hello") == 5
    assert count_letters("welcome") == 7

    print("Test case 1:",count_letters("Hello"))
    print("Test case 2:",count_letters("welcome"))


def calculate_sum(a, b):
        return a + b
    
def test_calculate_sum():
    calculation = calculate_sum(4, 11)
    print(f"Calculation result:{calculation}")
    assert calculation == 15    
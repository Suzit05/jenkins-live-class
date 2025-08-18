from calculator import add,sub,multi

def test_add():
    assert add(2,3) == 5
    assert add(-1,1) == 0
    assert add(0,0) == 0

def test_sub():
    assert sub(5,3) == 2
    assert sub(0,4) == -4
    assert sub(1,4) == -3

def test_multi():
    assert multi(2,3) == 6
    assert multi(3,0) == 0
    assert multi(0,0) == 0

#install pip if not installed: pip install pytest
#run: pytest

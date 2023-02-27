import functions

def test_double():
  assert functions.double(2) == 4
  assert functions.double(0) == 0
  assert functions.double(-42) == -84

def test_double_first():
  assert functions.double_first(1, 2) == 2
  assert functions.double_first(34, 7) == 68

def test_big_double():
  assert functions.big_double(10, 8) == 20
  assert functions.big_double(67, 84) == 168

def test_repeat():
  assert functions.repeat("python", 3) == "pythonpythonpython"
  assert functions.repeat("hi", 5) == "hihihihihi"
  assert functions.repeat("hi", -1) == ""

def test_batman():
  assert functions.batman() == "nananananananananana batman"

def test_max():
  assert functions.max(10, 5) == 10
  assert functions.max(-10, 50) == 50
  assert functions.max(-5, -50) == - 5

def test_max_divide():
  assert functions.max_divide(10, 5) == 0.5
  assert functions.max_divide(28, 7) == 0.25

def test_max_string():
  assert functions.max_string("python", "java") == "python"
  assert functions.max_string("code", "sleep") == "sleep"
  assert functions.max_string("aa", "bb") == "aa"

def test_even():
  assert functions.even(10) == True
  assert functions.even(3) == False
  assert functions.even(-5) == False

def test_even_lower():
  assert functions.even_below(10) == [0, 2, 4, 6, 8]
  assert functions.even_below(-10) == []

def test_even_in():
  assert functions.even_in([0, 2, 4, 6, 8, 10]) == [0, 2, 4, 6, 8, 10]
  assert functions.even_in([0, 1, 2, 3, 4, 5]) == [0, 2, 4]
  assert functions.even_in([1, 3, 5, 7]) == []

def test_average():
  assert functions.average([2, 3, 4]) == 3
  assert functions.average([2]) == 2
  assert functions.average([100, 50]) == 75
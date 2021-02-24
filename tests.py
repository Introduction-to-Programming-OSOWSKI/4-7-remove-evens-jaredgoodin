#DO NOT TAMPER WITH THIS FILE
#ANY EDITS YOU MAKE TO THIS FILE WILL BE SAVED TO YOUR PUBLIC GITHUB HISTORY
#TAMPERING WITH THIS FILE WILL BE OBVIOUS AND WILL RESULT IN A ZERO

import main;
import datetime;

year = 2021
month = 2
day = 23

def test_code():
    assert main.removeEvens([0,0,2,2,4,10]) == [0, 0], "removeEvens([0,0,2,2,4,10]) == [0, 0] failed"
    assert main.removeEvens([1,2,3,4,5,6,7]) == [1, 3, 5, 7], "removeEvens([1,2,3,4,5,6,7]) == [1, 3, 5, 7] failed"

def test_late():
    assert datetime.datetime.now() < datetime.datetime(year, month, day + 1, 4, 0), "Submitted Late"

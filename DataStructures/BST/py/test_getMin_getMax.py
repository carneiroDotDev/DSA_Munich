import random
from main import *
from user import *
from utils import print_tree, format_tree_string

cases = [
    (5, "Blake#0", "Carrell#14"),
    (10, "Ricky#1", "Vennett#29"),
    (15, "Shelley#2", "George#42"),
]


def test(num_users, min_user, max_user):
    users = get_users(num_users)
    bst = BSTNode()
    for user in users:
        bst.insert(user)
    print("=====================================")
    print("Tree:")
    print("-------------------------------------")
    print_tree(bst)
    print("-------------------------------------\n")
    print(f"Expected min: {min_user}, max: {max_user}")
    try:
        actual_min = bst.get_min()
        actual_max = bst.get_max()
        print(f"Actual min: {actual_min.user_name}, max: {actual_max.user_name}")
        if actual_max.user_name == max_user and actual_min.user_name == min_user:
            print("Pass \n")
            return True
        print("Fail \n")
        return False
    except Exception as e:
        print(f"Error: {e}")
        return False


def test_getMin_getMax():
    passed = 0
    failed = 0
    for test_case in cases:
        correct = test(*test_case)
        if correct:
            passed += 1
        else:
            failed += 1
    if failed == 0:
        print("============= PASS ==============")
    else:
        print("============= FAIL ==============")
        quit('test_getMin_getMax.py failed')
    print("Test results:")
    print(f"{passed} passed, {failed} failed")

test_getMin_getMax()
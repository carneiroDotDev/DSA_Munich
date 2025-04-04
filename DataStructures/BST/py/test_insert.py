import random
from main import *
from user import *
from ref import *
from utils import print_tree, format_tree_string

cases = [
    (3),
    (5),
    (10)
]


def test(num_users):
    users = get_users(num_users)
    expected_bst = BSTNode()
    for user in users:
        ref_implementation(expected_bst, user)
    print("=====================================")
    print("Expecting Tree:")
    print("-------------------------------------")
    print_tree(expected_bst)
    print("-------------------------------------\n")
    actual_bst = BSTNode()
    for user in users:
        print(f"Inserting {user} into tree...")
        actual_bst.insert(user)
    print("\n")
    print("Actual Tree:")
    print("-------------------------------------")
    print_tree(actual_bst)
    print("-------------------------------------")
    if ref_inorder(actual_bst, []) == ref_inorder(expected_bst, []):
        print("Pass \n")
        return True
    print("Fail \n")
    return False


def test_insert():
    passed = 0
    failed = 0
    for test_case in cases:
        correct = test(test_case)
        if correct:
            passed += 1
        else:
            failed += 1
    if failed == 0:
        print("============= PASS ==============")
    else:
        print("============= FAIL ==============")
        quit('test_add_words.py failed')
    print("Test results:")
    print(f"{passed} passed, {failed} failed")

test_insert()

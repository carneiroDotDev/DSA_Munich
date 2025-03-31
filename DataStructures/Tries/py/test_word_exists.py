import json
from main import *

test_cases = [
    (["dev", "devops", "devs", "designer"], "devops", True),
    (["manager", "qa", "dev", "intern"], "ceo", False),
    (["engineer", "developer", "janitor"], "dev", False),
    (
        ["dev", "developer", "devops", "manager"],
        "hr",
        False,
    ),
    (["qa", "qaops", "qam"], "qaops", True),
]


def test(words, word_to_check, expected_output):
    print("---------------------------------")
    trie = Trie()
    for word in words:
        trie.add(word)
    print("Trie:")
    print(json.dumps(trie.root, sort_keys=True, indent=2))
    print(f'Checking if "{word_to_check}" exists:')
    print(f"Expecting: {expected_output}")
    try:
        actual = trie.exists(word_to_check)
        print(f"Actual: {actual}")
        if actual == expected_output:
            print("Pass \n")
            return True
        print("Fail \n")
        return False
    except Exception as e:
        print(f"Error: {e}")
        return False


def test_word_exists():
    passed = 0
    failed = 0
    for test_case in test_cases:
        correct = test(*test_case)
        if correct:
            passed += 1
        else:
            failed += 1
    if failed == 0:
        print("============= PASS ==============")
    else:
        print("============= FAIL ==============")
        quit('test_word_exists.py failed')
        
    print("Test results:")
    print(f"{passed} passed, {failed} failed")
    print("=================================")
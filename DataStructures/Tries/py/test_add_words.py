import json
from main import *

test_cases = [
    (
        ["dev", "devops", "devs"],
        {
            "d": {
                "e": {
                    "v": {"*": True, "o": {"p": {"s": {"*": True}}}, "s": {"*": True}}
                }
            }
        },
    ),
    (
        ["qa", "qaops", "qam"],
        {
            "q": {
                "a": {"*": True, "o": {"p": {"s": {"*": True}}}, "m": {"*": True}},
            }
        },
    ),
        (
        ["pm", "po", "pojo", "pope", "cs", "ce", "ceo", "cfo"],
        {
            "p": {
                "m": {"*": True},
                "o": {"*": True, "j": {"o": {"*": True}}, "p": {"e": {"*": True}}},
            },
            "c": {
                "s": {"*": True},
                "e": {"*": True, "o": {"*": True}},
                "f": {"o": {"*": True}},
            },
        },
    ),
]


def test(words, expected_trie):
    print("---------------------------------")
    print(f"Inputs:")
    print(f" * Words: {words}")
    print(" * Expected trie:")
    print(f"{json.dumps(expected_trie, sort_keys=True, indent=2)}")
    try:
        trie = Trie()
        for word in words:
            trie.add(word)
            print(f"Adding {word}...")
        print("Actual Trie:")
        print(json.dumps(trie.root, sort_keys=True, indent=2))
        if trie.root == expected_trie:
            print("Pass \n")
            return True
        print("Fail \n")
        return False
    except Exception as e:
        print(f"Error: {e}")
        return False


def test_add_words():
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
        quit('test_add_words.py failed')
    print("Test results:")
    print(f"{passed} passed, {failed} failed")
    print("=================================")

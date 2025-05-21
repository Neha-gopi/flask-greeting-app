import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app.greet import get_greeting


def test_get_greeting():
    assert get_greeting("Alice") == "Hello, Alice!"

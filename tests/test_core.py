import pytest
from ibterms import TERMS, find_terms, advice, explain


def test_single():
    assert find_terms("Find the zeros of f(x) = x^2 - 4.") == ["find"]


def test_order_of_appearance():
    assert find_terms("Solve 2x = 6. Hence write down x + 1.") == ["solve", "hence", "write down"]


def test_longer_term_hides_shorter():
    assert find_terms("Hence or otherwise, find the area.") == ["hence or otherwise", "find"]


def test_show_that_not_show():
    assert find_terms("Show that x = 2 is a root.") == ["show that"]


def test_case_and_spacing():
    assert find_terms("WRITE   DOWN the gradient") == ["write down"]


def test_no_term():
    assert find_terms("The sky is blue.") == []
    assert explain("The sky is blue.") == "No command term found."


def test_word_boundary():
    assert find_terms("The findings were drawn up") == []


def test_advice():
    assert advice("prove")["answer_must_show"].startswith("a complete argument")
    with pytest.raises(KeyError):
        advice("dance")


def test_every_term_has_two_texts_and_no_dashes():
    for t, (a, b) in TERMS.items():
        assert a and b
        assert chr(0x2014) not in a + b and chr(0x2013) not in a + b


def test_explain_lines():
    assert explain("Sketch the graph.").startswith("SKETCH:")

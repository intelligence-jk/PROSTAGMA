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
    assert advice("prove")["examiner_looks_for"].startswith("A complete argument")
    assert set(advice("prove")) == {"term", "examiner_looks_for", "working_to_show", "common_mistake"}
    with pytest.raises(KeyError):
        advice("dance")


def test_every_term_has_three_texts_and_no_dashes():
    for t, parts in TERMS.items():
        assert len(parts) == 3 and all(parts)
        text = "".join(parts)
        assert chr(0x2014) not in text and chr(0x2013) not in text


def test_readme_count_matches():
    import re
    m = re.search(r"(\d+) terms", open("README.md").read())
    assert m and int(m.group(1)) == len(TERMS) == 24


def test_disclaimer_in_readme_and_docstring():
    import ibterms.core as c
    sentence = ("This project is not affiliated with, endorsed by or produced by the International "
                "Baccalaureate Organization. It is not the official glossary of command terms. "
                "Check your subject guide for the official wording.")
    assert sentence in open("README.md").read()
    assert sentence in c.__doc__


def test_each_note_has_a_common_mistake_in_its_own_words():
    for t in TERMS:
        assert advice(t)["common_mistake"].endswith(".")

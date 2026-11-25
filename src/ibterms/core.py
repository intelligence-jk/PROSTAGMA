"""Detect the command terms in a maths question and say what the answer must show.

The wording below is our own plain-language guidance. It is not the
International Baccalaureate's official glossary; check your own syllabus
documents for the official definitions.
"""
import re

# term -> (what to do, what the written answer must contain)
TERMS = {
    "show that": ("reach the printed result by valid steps",
                  "every step from the given statement to the result; do not start from the result"),
    "hence or otherwise": ("use the earlier part if you can, though any valid method counts",
                           "a clear method and the final answer"),
    "hence": ("use the result of the earlier part",
              "a line that visibly uses the earlier result; a different method may not earn the marks"),
    "write down": ("give the answer with little or no working",
                   "the answer alone is enough"),
    "state": ("give a short answer with no working",
              "the answer alone is enough"),
    "find": ("get the answer using a method",
             "working that leads to the answer, then the answer"),
    "determine": ("get the answer using a method",
                  "working that leads to the answer, then the answer"),
    "calculate": ("work out a numerical answer",
                  "the working, the number and its units if any"),
    "solve": ("find every value that satisfies the equation",
              "the method, every solution, and a check if the question restricts the values"),
    "simplify": ("write in a shorter equivalent form",
                 "the steps and a final form with no further simplification possible"),
    "factorise": ("write as a product", "the product, which can be multiplied back to the start"),
    "differentiate": ("find the derivative", "the derivative, with the rule used visible"),
    "integrate": ("find the integral", "the integral, with the constant of integration for an indefinite one"),
    "sketch": ("draw the shape with the key features labelled",
               "the shape, the intercepts, turning points and asymptotes; scale is not required"),
    "draw": ("draw accurately, with a ruler or compass if needed", "an accurate, labelled drawing"),
    "plot": ("mark points on given axes", "points placed accurately on the scale"),
    "prove": ("show a statement is always true by logical steps",
              "a complete argument with a conclusion; examples alone are not a proof"),
    "justify": ("give reasons for a statement", "the statement and the reason that supports it"),
    "explain": ("give the reasons or causes", "a short written reason, in words"),
    "verify": ("check that a given value works", "the substitution and the matching result"),
    "estimate": ("give an approximate value", "a sensible rounded value and how it was reached"),
    "interpret": ("say what a number or result means in the context",
                  "a sentence that uses the context of the question"),
    "comment": ("give an observation about a result", "a short statement tied to the numbers"),
    "compare": ("say how two things are alike and different", "at least one statement about each side"),
}

_ORDER = sorted(TERMS, key=len, reverse=True)
_PATTERNS = {t: re.compile(r"\b" + t.replace(" ", r"\s+") + r"\b", re.I) for t in TERMS}


def find_terms(question):
    """Command terms in order of appearance. A longer term hides its shorter part
    (so 'hence or otherwise' is not also 'hence')."""
    taken, found = [], []
    for t in _ORDER:
        for m in _PATTERNS[t].finditer(question):
            if not any(m.start() < e and s < m.end() for s, e in taken):
                taken.append((m.start(), m.end()))
                found.append((m.start(), t))
    return [t for _, t in sorted(found)]


def advice(term):
    if term not in TERMS:
        raise KeyError(term)
    do, show = TERMS[term]
    return {"term": term, "do": do, "answer_must_show": show}


def explain(question):
    terms = find_terms(question)
    if not terms:
        return "No command term found."
    return "\n".join(f"{t.upper()}: {TERMS[t][0]}. Show: {TERMS[t][1]}." for t in terms)

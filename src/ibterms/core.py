"""Detect the command terms in a maths question and give a practical tutor's note for each.

This project is not affiliated with, endorsed by or produced by the International Baccalaureate Organization. It is not the official glossary of command terms. Check your subject guide for the official wording.

Every note below is our own teaching advice, written from how a tutor explains
the word to a student: what the examiner is looking for, how much working to
show, and one common mistake.
"""
import re

# term -> (what the examiner is looking for, how much working to show, a common mistake)
TERMS = {
    "show that": ("The route from the given start to the given end, with nothing skipped.",
                  "Every line. The end result is printed, so the marks are for the steps.",
                  "Working backwards from the printed result and calling it done."),
    "hence or otherwise": ("Usually the earlier part is meant to help, and any correct method is accepted.",
                           "Enough to see your method and the final answer.",
                           "Ignoring the earlier part and then getting stuck on a long route."),
    "hence": ("Use the result you just found. The examiner expects the earlier part to appear in your working.",
              "One clear line that points back to that result.",
              "Starting again with a new method that never touches the earlier answer."),
    "write down": ("A quick answer that you can read straight off or recall.",
                   "Usually none. If you are doing a long calculation, you have misread the question.",
                   "Spending five minutes on a one-mark question."),
    "state": ("The fact or value, said plainly.",
              "None beyond the answer itself.",
              "Adding a paragraph of reasons nobody asked for."),
    "find": ("The value or expression, reached by a method you can see.",
             "Enough steps that a reader could follow you, then the answer.",
             "Writing only the answer when the working was worth marks."),
    "determine": ("A result that is fully pinned down, not a rough idea.",
                  "The key steps and the exact result.",
                  "Stopping at an equation without solving it."),
    "calculate": ("A number, worked out from the data in the question.",
                  "The substitution, the arithmetic and the units.",
                  "Losing the units, or rounding in the middle of the calculation."),
    "solve": ("Every value that makes the statement true.",
              "The algebra, each solution, and a check against any limits in the question.",
              "Finding one root and forgetting the other."),
    "simplify": ("A tidier form that cannot be tidied further.",
                 "The main steps, then a clean final line.",
                 "Stopping while a common factor is still there."),
    "factorise": ("The expression written as a product.",
                  "A line or two showing how you found the factors.",
                  "Giving factors that do not multiply back to the original."),
    "differentiate": ("The derivative, with the right rule chosen.",
                      "The rule you used, then the result.",
                      "Forgetting the inner derivative in a chain rule question."),
    "integrate": ("The antiderivative, correctly built.",
                  "The setup and the result; for an indefinite integral, the constant.",
                  "Leaving out the + c."),
    "sketch": ("The overall shape and the features that matter, not a plotted accurate graph.",
               "Label the intercepts, turning points and asymptotes you know.",
               "Drawing a pretty curve with no labels."),
    "draw": ("A neat, careful diagram or graph.",
             "Use a ruler or compass when the shape needs it, and label what is given.",
             "Drawing freehand and getting the proportions wrong."),
    "plot": ("Points placed correctly on the axes you were given.",
             "A table of values first, then the points.",
             "Misreading the scale on one axis."),
    "prove": ("A complete argument that works for every case, not a few cases.",
              "Every logical step, with a short closing sentence.",
              "Trying a few numbers and calling that a proof."),
    "justify": ("A claim together with the reason that backs it.",
                "The claim, then the working or fact that supports it.",
                "Repeating the claim without a reason."),
    "explain": ("A reason in words that shows you know why, not only what.",
                "A sentence or two that uses the language of the question.",
                "Describing what happened instead of why."),
    "verify": ("A check that a given value really works.",
               "Put the value in and show both sides agree.",
               "Saying it works without substituting."),
    "estimate": ("A sensible rough value, not a precise calculation.",
                 "A line showing the rounding or approximation you used.",
                 "Giving an answer that is wildly off because the rounding was careless."),
    "interpret": ("What the number means for the real situation in the question.",
                  "One sentence that mentions the context and the units.",
                  "Giving the number again with no meaning attached."),
    "comment": ("A short remark that links to the numbers you found.",
                "A sentence, tied to a specific value or trend.",
                "A vague remark such as 'it is good' with no numbers."),
    "compare": ("Both things, set side by side.",
                "At least one point about each, and a link between them.",
                "Describing only one of the two."),
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
    looks_for, working, mistake = TERMS[term]
    return {"term": term, "examiner_looks_for": looks_for,
            "working_to_show": working, "common_mistake": mistake}


def explain(question):
    terms = find_terms(question)
    if not terms:
        return "No command term found."
    return "\n".join(
        f"{t.upper()}\n  Looks for: {TERMS[t][0]}\n  Working: {TERMS[t][1]}\n  Watch out: {TERMS[t][2]}"
        for t in terms)

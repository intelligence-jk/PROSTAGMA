# ib-command-terms

This project is not affiliated with, endorsed by or produced by the International Baccalaureate Organization. It is not the official glossary of command terms. Check your subject guide for the official wording.

Finds the command terms in a maths question (find, hence, sketch, show that and others) and gives a practical tutor's note for each.

## What it solves
Students lose marks by answering the wrong kind of question: giving a bare answer to a "show that", or using a new method when the question says "hence". This tool reads a question, lists each command term in order and gives a short practical note for each: what the examiner is looking for, how much working to show, and one common mistake. The notes are our own teaching advice, not definitions. Pure Python 3.10+, standard library only.

## Example
```bash
python -m ibterms "Find the roots of x^2 - 5x + 6 = 0. Hence sketch the graph."
```
```
FIND
  Looks for: The value or expression, reached by a method you can see.
  Working: Enough steps that a reader could follow you, then the answer.
  Watch out: Writing only the answer when the working was worth marks.
HENCE
  Looks for: Use the result you just found. The examiner expects the earlier part to appear in your working.
  Working: One clear line that points back to that result.
  Watch out: Starting again with a new method that never touches the earlier answer.
SKETCH
  Looks for: The overall shape and the features that matter, not a plotted accurate graph.
  Working: Label the intercepts, turning points and asymptotes you know.
  Watch out: Drawing a pretty curve with no labels.
```
(Output pasted from a real run.)

## The maths behind it
Detection is a whole-word, case-insensitive match. Longer terms are tried first and hide the shorter terms inside them, so "hence or otherwise" is not also reported as "hence", and the matches are returned in the order they appear in the question. There are 24 terms. The note for each is three short texts: what the examiner is looking for, how much working to show, and a common mistake. A test checks that this count equals the number of entries in the code.

## Install and run
```bash
python -m pip install -e .
python -m pytest
```

## Licence
MIT. Made by Math & Myth (mathandmyth.ae): one to one maths mentoring, online, across the UAE.

# ib-command-terms

Finds the command terms in a maths question (find, hence, sketch, show that and others) and says what the written answer must contain.

## What it solves
Students lose marks by answering the wrong kind of question: giving a bare answer to a "show that", or using a new method when the question says "hence". This tool reads a question, lists each command term in order and gives plain-language guidance. The wording is our own and is **not** the International Baccalaureate's official glossary; always check your own syllabus documents. Pure Python 3.10+, standard library only.

## Example
```bash
python -m ibterms "Find the roots of x^2 - 5x + 6 = 0. Hence sketch the graph."
```
```
FIND: get the answer using a method. Show: working that leads to the answer, then the answer.
HENCE: use the result of the earlier part. Show: a line that visibly uses the earlier result; a different method may not earn the marks.
SKETCH: draw the shape with the key features labelled. Show: the shape, the intercepts, turning points and asymptotes; scale is not required.
```
(Output pasted from a real run.)

## The maths behind it
Detection is a whole-word, case-insensitive match. Longer terms are tried first and hide the shorter terms inside them, so "hence or otherwise" is not also reported as "hence", and the matches are returned in the order they appear in the question. The guidance for each of the 23 terms is a pair of short texts: what to do, and what the answer must show.

## Install and run
```bash
python -m pip install -e .
python -m pytest
```

## Licence
MIT. Made by Math & Myth (mathandmyth.ae): one to one maths mentoring, online, across the UAE.

#!/bin/sh

if [ $1 = "--tree" ]; then
    python3 testsuite/q2/binaryTree.py
    python3 testsuite/q2/starTree.py
    python3 testsuite/q2/simpleTree.py
    python3 testsuite/q2/complexTree.py
elif [ $1 = "--approx" ]; then
    python3 testsuite/q3/binaryTree.py
    python3 testsuite/q3/starTree.py
    python3 testsuite/q3/simpleTree.py
    python3 testsuite/q3/simpleGraph.py
    python3 testsuite/q3/complexTree.py
    python3 testsuite/q3/complexGraph.py
elif [ $1 = "--compare-opti-tree" ]; then
    python3 testsuite/comparaison/completeTree.py
elif [ $1 = "--opti" ]; then
    python3 testsuite/q5/binaryTree.py
    python3 testsuite/q5/starTree.py
    python3 testsuite/q5/simpleTree.py
    python3 testsuite/q5/simpleGraph.py
    python3 testsuite/q5/complexTree.py
    python3 testsuite/q5/complexGraph.py
elif [ $1 = "--compare-approx-opti" ]; then
    python3 testsuite/comparaison/completeTest.py
fi

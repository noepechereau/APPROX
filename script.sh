if [ $1 = "q2" ]; then
    python3 testsuite/q2/binaryTree.py
    python3 testsuite/q2/starTree.py
    python3 testsuite/q2/simpleTree.py
    python3 testsuite/q2/complexTree.py
elif [ $1 = "q3" ]; then
    python3 testsuite/q3/binaryTree.py
    python3 testsuite/q3/starTree.py
    python3 testsuite/q3/simpleTree.py
    python3 testsuite/q3/simpleGraph.py
    python3 testsuite/q3/complexTree.py
    python3 testsuite/q3/complexGraph.py
fi


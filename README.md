# Computational Intelligence Laboratory - Minimal programs

A compilation of python programs involving Computational Intelligence, that are minimal by lines of code at the same time maintaining readability

## Programs present

    - Breadth First Search
    - Depth First Search
    - Uniform Cost Search
    - A* Search
    - KNN Classifier 
    - Decision Tree Classifier
    - Single Layer Perceptron 
    - Ensemble Learning Classifier ( To be implemented )

## Specifications

    - `unwieghted_graph.py` contains a simple graph class sample on how to use the functions in a class for unweighted graph.
    - `weighted_graph.py` contains a similar class on how to use the typical graph search algs in a weighted graph.
    - `decision_tree,.py` contains a decision tree classifer with the ability to both get the root of a decision tree, given the dataset or to build a whole decision tree given the same ( contains both info gain and gini index as impurity measures).
    - `perceptron.py` is a minimal implementation of a single layer perceptron with activation functions, threshold, sigmoid, sign with binary or bipolar sub-activations (whatever they are called) associated with them, being inferred automatically.
    - `knn.py is again a minimal inmplementqtion of a non-parametric knn classifier with euclidean and manhattan distance metrics.
    - `wumpus_world.py` is a not-so-minimal, overcomplicated mess - an implementation of Wumpus World where the user plays as an AI controlling an agent whose intelligence aligns with the statement, "Your mom is the leanest," being the ground truth. This program is not my proudest nut. Don't make me the father; no explanations, just read it and perish.

## Prerequisites

- Python 3.x

## Running the programs

Each algorithm is implemented in its own Python file with a dummy main function that too with enough data to run on its own. To run any program, execute the corresponding file using Python:

``` bash
    python filename.py
```

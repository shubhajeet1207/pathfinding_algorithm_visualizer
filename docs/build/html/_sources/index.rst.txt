.. Pathfinding Algorithm Visualizer documentation master file, created by
   sphinx-quickstart on Fri Apr 14 19:08:17 2023.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to Pathfinding Algorithm Visualizer's documentation!
===========================================================

.. toctree::
   :maxdepth: 2
   :caption: Contents:

``Path-finding Algorithm Visualizer`` is a GUI based toolbox for visualizing Pathfinding algorithms like A*, Breadth First Search etc. written in Python.
The toolbox bundles some shortest path finding algorithms to visualize Time Complexity and traversing style along with other additional feature of embedding obstacles.

   _pages/Introduction
   _pages/Motivation
   _pages/Contributions
   _pages/Methodology
   _pages/Results and Discussions
   _pages/Conclusion and future scope


Highlights
----------
This Python program computes...

-  ... shortest path from start node to final using A*, BFS, DFS, Dijkstra, Bidirectional & Best First Search.
-  ... shortest path even if obstacles are present.
-  ... total visited nodes.
-  ... total elapsed time taken for completion.

... and comes with variety of additional PFAV(Path-finding Algorithm Visualizer) tools, such as...

-  ... resetting the grid board again & again to visualize algorithms.
-  ... availability of Time Complexity and Space Complexity.

Installation
------------
Before the running this program, user must have `python3` installed on the machine.

Clone the repository by using the following command:

.. code:: bash
    $ git clone https://github.com/shubhajeet1207/pathfinding_algorithm_visualizer

After this open the project and activate the virtual environment:

.. code:: bash

    $ virtualenv venv

`Note: In place of venv user can use any other name for their virtual environment.`

Activate virtual environment using:

.. code:: bash

    $.\venv\Scripts\activate

In case, virtualenv is missing then use **Conda Environment** or can use:

.. code:: bash

    $ pip install virtualenv

For installing virtual environment.

After this the requirements can be installed using the `pip` tool:

.. code:: bash

    $ pip install -r requirements.txt

Then run the program:

.. code:: bash

    $ python3 run visualizer.py

Disclaimer & Context
--------------------

This project has initially (up to version 1.0) been developed within the scope of our Mini Project "Development of a GUI Python Application for Path-finding algorithm visualizer" at the ABV-Indian Institute of Information Technology, Gwalior, M.P., India.
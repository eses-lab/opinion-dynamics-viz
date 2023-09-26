

# Opinion Dynamics Visualization

This project aims to create an interactive simulation of opinion dynamics within a population of agents, visualized in a Jupyter notebook and integrated with GPT-3 to simulate realistic agent dialogues.


## Objective:
The objective is to understand and visualize how individual opinions within a population evolve over time through interactions, using models from computational social science. The integration of GPT-3 aims to bring in realism in agent dialogues, providing insights into nuanced perspectives and the complexity of opinion formation.

## Components:
1. opinion_dynamics.py
Agent Class: Represents agents with continuous multidimensional opinions.
Population Class: Manages a population of agents and their interactions.
Initialization Functions: Create agents with random initial opinions.
Evolve Method: Contains exchange rules and updates agent opinions based on interactions.
2. opinion_viz.py
This manages the opinion visualization using Matplotlib.
It provides a 2D projection of the opinion landscape from a higher-dimensional opinion space and animation over time as opinions evolve.
3. gpt_interface.py
This handles integration with the GPT-3 API.
It provides functions to prompt GPT-3 with context and arguments and to retrieve and process response text.
4. analysis.py
Contains analysis functions to study opinion convergence, clusters, polarity over time, and to quantify the complexity and variety of GPT-generated texts.
5. opinion_dynamics_notebook.ipynb
Serves as the hub of the project and main interface to generate, study, visualize and analyze opinion evolution, adjust parameters, and review insights.

## Usage

TODO - gifs or screenshots

## Built With

- Python
- NumPy 
- Matplotlib
- Jupyter

## Contributors

Eseoghene Efekodo

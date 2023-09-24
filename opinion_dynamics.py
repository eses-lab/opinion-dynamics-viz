
# imports
import random

# define and implement the agent class
# The agent class represents a single agent in the population. Each agent has an id, a set of opinions, and a method for updating opinions.

class Agent:
    def __init__(self, agent_id, opinions):
        
        self.agent_id = agent_id
        self.opinions = opinions

    def update_opinions(self, new_opinions):
        self.opinions = new_opinions


# define and implement the population class
# The Agent population class will manage a collection of agents and handle their interactions

class AgentPopulation:
    def __init__(self, num_of_agents, num_of_opinion_dimensions):
        self.agent_list = [] # this stores all the agent objects.

        self.num_of_agents = num_of_agents # this represents how many agents you want in your population. so, if num_of_agents = 5, it means your population will consist of 5 agents. etc

        self.num_of_opinion_dimensions = num_of_opinion_dimensions # this represents the number of dimensions in the opinion space of each agent. For example, if num_of_opinion_dimensions = 2, it means each agent will have opinions on two different dimensions/topics.

        self.initialize_population() # This will call the method to initialize the agents to create a population

    def initialize_population(self):
        for i in range(self.num_of_agents):
            opinions = [random.random() for _ in range(self.num_of_opinion_dimensions) ] # generate a random opinion for each dimension
            individual_agent = Agent(i, opinions) # Create a new Agent object with the generated opinions.
            self.agent_list.append(individual_agent) # Add the new Agent object to the agent_list


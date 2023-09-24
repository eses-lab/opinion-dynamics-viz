class Agent:
    def __init__(self, agent_id, opinions):
        
        self.agent_id = agent_id
        self.opinions = opinions

    def update_opinions(self, new_opinions):
        self.opinions = new_opinions

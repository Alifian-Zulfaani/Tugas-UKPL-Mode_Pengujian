class StateTransitionTest:
    def __init__(self, states, transitions, initial_state):
        self.states = states
        self.transitions = transitions
        self.initial_state = initial_state
        self.current_state = initial_state

    def reset(self):
        self.current_state = self.initial_state

    def get_current_state(self):
        return self.current_state

    def execute_transition(self, transition):
        if transition in self.transitions[self.current_state]:
            self.current_state = self.transitions[self.current_state][transition]
            return True
        else:
            return False

def state_transition_testing(states, transitions, initial_state):
    test_cases = []
    stt = StateTransitionTest(states, transitions, initial_state)
    
    # generate test cases for each transition
    for state in states:
        stt.current_state = state
        for transition in transitions[state]:
            stt.execute_transition(transition)
            test_cases.append((state, transition, stt.current_state))
        stt.reset()

    return test_cases
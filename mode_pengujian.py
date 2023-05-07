from boundary_value_analysis import boundary_value_analysis
from state_transition_testing import state_transition_testing

boundary_test_cases = boundary_value_analysis(1, 10, 20, 30, 100, 200)
print(boundary_test_cases)

states = ["off", "idle", "running"]
transitions = {
    "off": {"power_on": "idle"},
    "idle": {"start": "running", "power_off": "off"},
    "running": {"stop": "idle", "power_off": "off"}
}
initial_state = "off"

state_test_cases = state_transition_testing(states, transitions, initial_state)
print(state_test_cases)
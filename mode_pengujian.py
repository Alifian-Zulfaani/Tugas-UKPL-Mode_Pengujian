# Mengimport fungsi boundary_value_analysis dan state_transition_testing yang akan digunakan untuk pengujian
from boundary_value_analysis import boundary_value_analysis
from state_transition_testing import state_transition_testing

# Fungsi boundary_value_analysis dipanggil dengan argumen 1, 10, 20, 30, 100, 200 dan nilai kembaliannya disimpan dalam variabel boundary_test_cases.
boundary_test_cases = boundary_value_analysis(1, 10, 20, 30, 100, 200)
# Argumen boleh diisi sesuai keinginan, yang penting bertipe integer dan ada 6 argumen karena fungsi yang dibuat disetting menampung 6 argumen angka.

print(boundary_test_cases)

# Didefinisikan variabel states, transitions, dan initial_state yang merepresentasikan keadaan awal dan transisi antar keadaan yang ada pada suatu sistem.
states = ["off", "idle", "running"]
transitions = {
    "off": {"power_on": "idle"},
    "idle": {"start": "running", "power_off": "off"},
    "running": {"stop": "idle", "power_off": "off"}
}
initial_state = "off"

# Fungsi state_transition_testing dipanggil dengan argumen states, transitions, dan initial_state dan nilai kembaliannya disimpan dalam variabel state_test_cases.
state_test_cases = state_transition_testing(states, transitions, initial_state)
print(state_test_cases)
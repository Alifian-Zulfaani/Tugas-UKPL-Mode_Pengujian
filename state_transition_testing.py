class StateTransitionTest:
    # Fungsi __init__ digunakan untuk inisialisasi state yang akan dilakukan pengujian
    def __init__(self, states, transitions, initial_state):
        self.states = states
        self.transitions = transitions
        self.initial_state = initial_state
        self.current_state = initial_state

    # Fungsi reset digunakan untuk mengembalikan nilai dari current_state ke initial_state
    def reset(self):
        self.current_state = self.initial_state

    # Fungsi get_current_state digunakan untuk mengembalikan nilai dari current_state
    def get_current_state(self):
        return self.current_state

    #  fungsi execute_transition digunakan untuk mengecek apakah transisi yang akan dilakukan benar atau tidak
    def execute_transition(self, transition):
        if transition in self.transitions[self.current_state]:
            self.current_state = self.transitions[self.current_state][transition]
            return True
        else:
            return False


# Fungsi "state_transition_testing" yang menerima tiga parameter sebagai masukan yaitu "states", "transitions", dan "initial_state".
def state_transition_testing(states, transitions, initial_state):
    # Variabel "test_cases" dideklarasikan sebagai sebuah list kosong
    test_cases = []
    
    # Dibuat objek "StateTransitionTest" dengan menggunakan tiga parameter
    stt = StateTransitionTest(states, transitions, initial_state)
    
    # Pengujian dengan melakukan loop pada setiap state dan transition untuk menghasilkan kasus uji untuk setiap transisi
    for state in states:
        stt.current_state = state
        for transition in transitions[state]:
            stt.execute_transition(transition)
            # Hasil pengujian dihasilkan sebagai tuple yang berisi tiga nilai yaitu state awal, transisi yang diambil, dan state akhir.
            test_cases.append((state, transition, stt.current_state))
        # Setelah semua transisi pada setiap state selesai diuji, objek "StateTransitionTest" direset kembali ke state awal
        stt.reset()
        
    #  Test case yang dihasilkan di dalam loop akan dikembalikan sebagai hasil dari fungsi.
    return test_cases
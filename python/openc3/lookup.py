import os

class Lookup:
    # States are defined in an array: [RED_LOW, YELLOW_LOW, YELLOW_HIGH, RED_HIGH, GREEN_LOW, GREEN_HIGH]
    # where GREEN_LOW and GREEN_HIGH are optional e.g. [-80.0, -70.0, 60.0, 80.0]
    LIMITS_STATE_INDEX = { "RED_LOW": 0, "YELLOW_LOW": 1, "YELLOW_HIGH": 2, "RED_HIGH": 3, "GREEN_LOW": 4, "GREEN_HIGH": 5 }

    def __init__(self):
        self.stdout = ''

    def run(self, state, state_values):
        if Lookup.LIMITS_STATE_INDEX.get(state):
            self.stdout = state_values[Lookup.LIMITS_STATE_INDEX[state]]
        else:
            self.stdout = 'State not found'

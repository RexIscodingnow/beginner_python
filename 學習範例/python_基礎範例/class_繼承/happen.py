from score import Calculate
from decision import Decision

class HappenThing(Calculate, Decision):
    def someThing(scores):
        if scores == 200:
            return 1

        elif scores <= 150:
            return 2

        elif scores <= 100:
            return 3

        elif scores <= 60:
            return 4
from hstest.stage_test import *
from hstest.test_case import TestCase

CheckResult.correct = lambda: CheckResult(True, '')
CheckResult.wrong = lambda feedback: CheckResult(False, feedback)


class RPSTest(StageTest):

    def __init__(self, module_to_test: str):
        super().__init__(module_to_test)
        self.wins = 0
        self.draws = 0
        self.loses = 0

    def generate(self) -> List[TestCase]:
        options = ["rock", "paper", "scissors"]
        inputs = list()
        for option in options:
            [inputs.append(option) for _ in range(50)]
        tests = [TestCase(stdin=inp, attach=inp) for inp in inputs]
        tests.append(TestCase(stdin='rock', attach='rock', check_function=self.check_random))
        return tests

    def check_random(self, reply: str, attach) -> CheckResult:

        wrong_randomize = CheckResult.wrong("The results of the games: {} wins, {} draws and {} loses\n"
                                            "Looks like you don't use random module to choose random option!\n"
                                            "The number of wins, draws and loses should be approximately the same.\n"
                                            "Make sure you output the results of the games like in examples!\n"
                                            "If you pretty sure that you use random module try to rerun the tests!\n"
                                            .format(self.wins, self.draws, self.loses))
        if self.loses < 30:
            return wrong_randomize
        if self.draws < 30:
            return wrong_randomize
        if self.wins < 30:
            return wrong_randomize
        return CheckResult.correct()

    def check(self, reply: str, attach) -> CheckResult:

        wrong_result = CheckResult.wrong(
            "Seems like your answer (\"{}\") does not fit in given templates".format(reply))

        hits = {
            'rock': 'scissors',
            'scissors': 'paper',
            'paper': 'rock'
        }

        computer_option = 'not found'

        if 'scissors' in reply.lower():
            computer_option = 'scissors'
        elif 'paper' in reply.lower():
            computer_option = 'paper'
        elif 'rock' in reply.lower():
            computer_option = 'rock'

        if computer_option == 'not found':
            return wrong_result

        if hits[attach] == computer_option:
            result = 'well done'
        elif attach == computer_option:
            result = 'draw'
        else:
            result = 'sorry'

        if result not in reply.lower():
            return wrong_result

        if 'sorry' in reply.lower():
            self.loses += 1
        elif 'draw' in reply.lower():
            self.draws += 1
        elif 'well done' in reply.lower():
            self.wins += 1
        else:
            return wrong_result

        return CheckResult.correct()


RPSTest("rps.game").run_tests()

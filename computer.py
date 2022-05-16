import sys
from intcode import *

class Computer(Intcode):

    def run(self):
        #print("Computer running...")
        for i in range(0, len(self.CodeList)):
            self.initialize_operation()
            self.choose_computation()
            self.reset()
        return self.Output[0]

    def initialize_operation(self):
        self.set_opcode()
        self.set_size()
        self.set_chunk()
        self.set_destination()

    def choose_computation(self):
        #print("Computing chunk " + str(self.Chunk))
        if self.Opcode == 1:
            self.compute_math()
        elif self.Opcode == 2:
            self.compute_math()
        elif self.Opcode == 3:
            self.compute_input()
        elif self.Opcode == 4:
            self.compute_output()
        elif self.Opcode == 5:
            self.jump()
        elif self.Opcode == 6:
            self.jump()
        elif self.Opcode == 7:
            self.evaluate()
        elif self.Opcode == 8:
            self.evaluate()
        elif self.Opcode == 99:
            self.system_exit()
        else:
            print("System abort - Unexpected opcode: " + str(self.Opcode))

    def compute_math(self):
        self.set_modes()
        self.set_parameters()
        self.perform_operation()
        self.write_result()

    def compute_input(self):
        self.write_input()
        self.Turn = 1

    def compute_output(self):
        self.set_modes()
        self.set_parameters()
        self.write_output()

    def jump(self):
        self.set_modes()
        self.set_parameters()
        self.perform_operation()

    def evaluate(self):
        self.set_modes()
        self.set_parameters()
        self.perform_operation()
        self.write_result()

    def system_exit(self):
        fskdjl = 1
        """
        print()
        print("Computation complete.")
        print("Output: " + str(self.Output))
        """


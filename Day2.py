def perform_operation(opcode, num1, num2):
    switcher = {
        1: num1 + num2,
        2: num1 * num2
    }
    return switcher.get(opcode)

class Intcode:
    def __init__(self, initialList):
        self.FinalList = initialList.copy()
        self.ChunkSize = 4

    def replace_value(self, position, value):
        self.FinalList[position] = value

    def process_math_computation(self, computeList):
        opcode = computeList[0]
        result = perform_operation(opcode, computeList[1], computeList[2])
        position = computeList[3]
        
        self.replace_value(position, result)

    def computize(self):
        computeChunk = []
        count = 0
        index = 0

        for i in range(0, len(self.FinalList)):
            if (self.FinalList[i] == 99):
                return
            while (count < self.ChunkSize):
                computeChunk.append(self.FinalList[i + count])
                count += 1

            computeList[1] = self.FinalList[computeList[1]]
            computeList[2] = self.FinalList[computeList[2]]
            self.process_math_computation(computeList)
            computeList = []
            count = 0

def run_range(start, finish, goal):
    noun = start
    verb = start
    finished = 0
    while (noun <= finished):
        while (verb <= finished):
            program = Intcode()
            program.computize()
            if (program.FinalList[0] == goal):
                finished = 1
            else:
                verb += 1
        verb = 0
        noun += 1
    return (noun, verb)

#final = run_range(0, 99, 19690720)
#print(100 * final[0] + final[1])


initList = []

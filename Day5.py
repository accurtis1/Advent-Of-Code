import sys

class Intcode:
    def __init__(self, origList, initInput):
        self.Program = origList
        self.Input = initInput
        self.Outputs = []
        self.Finished = 0

    def replace_value(self, position, value):
        self.Program[position] = value

    def get_param_values(self, instructions, initialParams):
        finalParams = []
        instructions.remove(instructions[0])
        if instructions == []:
            for p in initialParams:
                parameter = self.calculate_param_mode(0, p)
                finalParams.append(parameter)
        else:
            if len(instructions) < len(initialParams):
                instructions.extend([0, 0, 0])
            for i in range(0, len(initialParams)):
                parameter = self.calculate_param_mode(instructions[i], initialParams[i])
                finalParams.append(parameter)
        return finalParams

    def calculate_param_mode(self, mode, parameter):
        if mode == 0:
            return self.Program[parameter]
        else:
            return parameter

    def compute_operation(self, instructions, paramList):
        opSwitcher = {
            1: self.add_params,
            2: self.multiply_params,
            3: self.input_param,
            4: self.output_param
        }
        zoom = opSwitcher.get(instructions[0])
        zoom(instructions, paramList)
        
    # Hate the way I ended up doing this...but am done with it
    def add_params(self, instructions, paramList):
        dest = paramList[-1]
        paramList.pop()
        params = self.get_param_values(instructions, paramList)
        result = params[0] + params[1]
        self.replace_value(dest, result)

    def multiply_params(self, instructions, paramList):
        dest = paramList[-1]
        paramList.pop()
        params = self.get_param_values(instructions, paramList)
        result = params[0] * params[1]
        self.replace_value(dest, result)

    def input_param(self, instructions, paramList):
        self.replace_value(paramList[-1], self.Input)

    def output_param(self, instructions, paramList):
        param = self.get_param_values(instructions, paramList)
        self.Outputs.append(param[0])

def split_instructions(instString):
    if instString == "99":
        stop_program()
    else:
        opcode = [instString[:1]]
    parameters = [ instString[i:i+1] for i in range(2, len(instString)) ]
    instStringList = opcode + parameters
    return instStringList

def get_instruction_list(origInst):
    instString = ''.join(reversed(str(origInst)))
    instStringList = split_instructions(instString)
    instFinalList = [ int(string) for string in instStringList ]
    return instFinalList

def get_chunk_size(opcode):
    chunkSwitcher = {
        1: 4,
        2: 4,
        3: 2,
        4: 2
    }
    return chunkSwitcher.get(opcode)

def stop_program():
    global TEST
    print("Diagnostic tests complete.")
    print(TEST.Outputs)
    sys.exit()


puzzleInput = [3,225,1,225,6,6,1100,1,238,225,104,0,1102,78,40,225,1102,52,43,224,1001,224,-2236,224,4,224,102,8,223,223,101,4,224,224,1,224,223,223,1,191,61,224,1001,224,-131,224,4,224,102,8,223,223,101,4,224,224,1,223,224,223,1101,86,74,225,1102,14,76,225,1101,73,83,224,101,-156,224,224,4,224,102,8,223,223,101,6,224,224,1,224,223,223,1102,43,82,225,2,196,13,224,101,-6162,224,224,4,224,102,8,223,223,101,5,224,224,1,223,224,223,1001,161,51,224,101,-70,224,224,4,224,102,8,223,223,1001,224,1,224,1,224,223,223,102,52,187,224,1001,224,-832,224,4,224,102,8,223,223,101,1,224,224,1,224,223,223,1102,19,79,225,101,65,92,224,1001,224,-147,224,4,224,1002,223,8,223,101,4,224,224,1,223,224,223,1102,16,90,225,1102,45,44,225,1102,92,79,225,1002,65,34,224,101,-476,224,224,4,224,102,8,223,223,1001,224,5,224,1,224,223,223,4,223,99,0,0,0,677,0,0,0,0,0,0,0,0,0,0,0,1105,0,99999,1105,227,247,1105,1,99999,1005,227,99999,1005,0,256,1105,1,99999,1106,227,99999,1106,0,265,1105,1,99999,1006,0,99999,1006,227,274,1105,1,99999,1105,1,280,1105,1,99999,1,225,225,225,1101,294,0,0,105,1,0,1105,1,99999,1106,0,300,1105,1,99999,1,225,225,225,1101,314,0,0,106,0,0,1105,1,99999,107,226,226,224,1002,223,2,223,1005,224,329,1001,223,1,223,1007,226,226,224,102,2,223,223,1005,224,344,101,1,223,223,1008,226,226,224,102,2,223,223,1005,224,359,1001,223,1,223,8,226,677,224,102,2,223,223,1006,224,374,101,1,223,223,1107,226,677,224,1002,223,2,223,1006,224,389,101,1,223,223,1108,226,677,224,102,2,223,223,1005,224,404,101,1,223,223,107,677,677,224,102,2,223,223,1006,224,419,1001,223,1,223,7,677,226,224,102,2,223,223,1005,224,434,101,1,223,223,1007,677,677,224,102,2,223,223,1005,224,449,1001,223,1,223,108,226,677,224,102,2,223,223,1005,224,464,1001,223,1,223,108,226,226,224,102,2,223,223,1006,224,479,101,1,223,223,107,226,677,224,102,2,223,223,1006,224,494,1001,223,1,223,7,226,226,224,1002,223,2,223,1006,224,509,101,1,223,223,1108,677,226,224,102,2,223,223,1005,224,524,101,1,223,223,1107,677,226,224,102,2,223,223,1005,224,539,101,1,223,223,1008,677,226,224,102,2,223,223,1005,224,554,101,1,223,223,1008,677,677,224,1002,223,2,223,1006,224,569,101,1,223,223,1107,677,677,224,102,2,223,223,1006,224,584,1001,223,1,223,1108,226,226,224,1002,223,2,223,1006,224,599,101,1,223,223,7,226,677,224,102,2,223,223,1006,224,614,101,1,223,223,108,677,677,224,1002,223,2,223,1006,224,629,101,1,223,223,1007,677,226,224,102,2,223,223,1006,224,644,101,1,223,223,8,677,677,224,1002,223,2,223,1006,224,659,101,1,223,223,8,677,226,224,102,2,223,223,1005,224,674,101,1,223,223,4,223,99,226]
testInput = [1002,4,3,4,33]
TEST = Intcode(puzzleInput, 1)

index = 0
while not TEST.Finished:
    instructions = get_instruction_list(TEST.Program[index])
    opcode = instructions[0]
    chunkSize = get_chunk_size(opcode)
    parameters = TEST.Program[index+1 : index+chunkSize]
    TEST.compute_operation(instructions, parameters)
    index += chunkSize








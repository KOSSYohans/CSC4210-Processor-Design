class RegisterFile:
    def __init__(self):
        # Initialize registers t0 through t6 to 0
        self.registers = {f"t{i}": 0 for i in range(7)}

    def read(self, reg_a, reg_b):
        return self.registers[reg_a], self.registers[reg_b]

    def write(self, reg_dest, value, write_enable):
        if write_enable:
            self.registers[reg_dest] = value & 0xFFFFFFFF
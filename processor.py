from alu import ALU
from register_file import RegisterFile
from control_unit import ControlUnit

class SingleCycleProcessor:
    def __init__(self):
        self.rf = RegisterFile()
        self.alu = ALU()
        self.cu = ControlUnit()
        self.program = [
            "and  t4, t0, t1",   # t4 = A & B
            "andn t6, t5, t3",   # t6 = (~C) & D
            "or   t0, t4, t6",   # t0 = final Y
        ]

    def run(self, A, B, C, D):
        # Load initial register values
        self.rf.registers['t0'] = A
        self.rf.registers['t1'] = B
        self.rf.registers['t2'] = C
        self.rf.registers['t3'] = D
        self.rf.registers['t5'] = C

        print(f"Executing: Y = ({A} & {B}) | (~{C} & {D})")

        for instr in self.program:
            dest, s1, s2, ctrl = self.cu.decode(instr)
            val1, val2 = self.rf.read(s1, s2)
            result = self.alu.execute(val1, val2, ctrl["alu_op"], ctrl["invert_a"])
            self.rf.write(dest, result, ctrl["reg_write"])

            print(f"\nInstr: {instr.strip()}")
            print(f"Signals: {ctrl}")
            print(f"Reg Update: {dest} = {bin(result)}")

        print(f"\nFinal Result (Y): {bin(self.rf.registers['t0'])}")

if __name__ == "__main__":
    cpu = SingleCycleProcessor()
    cpu.run(A=0b1, B=0b1, C=0b0, D=0b1)
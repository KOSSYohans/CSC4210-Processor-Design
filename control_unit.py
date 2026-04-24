class ControlUnit:
    # Generates control signals: ALU Op, Inversion Flag, and RegWrite.
    def decode(self, instruction):
        parts = instruction.replace(',', '').split()
        op_name = parts[0].lower()
        dest, src1, src2 = parts[1], parts[2], parts[3]
        is_and_not = (op_name == "andn")
        signals = {
            "alu_op": "OR" if op_name == "or" else "AND",
            "invert_a": is_and_not,
            "reg_write": True
        }

        return dest, src1, src2, signals
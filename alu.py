class ALU:
    def execute(self, val_a, val_b, alu_op, invert_a):
        # Use & 0xFFFFFFFF to keep results within 32-bit unsigned range.
        a_input = (~val_a & 0xFFFFFFFF) if invert_a else val_a
        if alu_op == "AND":
            return (a_input & val_b) & 0xFFFFFFFF
        elif alu_op == "OR":
            return (a_input | val_b) & 0xFFFFFFFF
        return 0
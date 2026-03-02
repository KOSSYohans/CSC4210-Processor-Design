# Name: Yohans Desalgne
# Task 1: Data Systems

def process_data(input_str, format_sel):
    # Define 32-bit signed boundaries
    
    MIN_INT = -2147483648   
    MAX_INT = 2147483647    
    
    # Parse decimal signed integer
    val = int(input_str)
    overflow = 0
    saturated = 0
    
    # Detect overflow and apply saturation logic
    if val > MAX_INT:
        val = MAX_INT     
        overflow = 1      
        saturated = 1  
    elif val < MIN_INT:
        val = MIN_INT
        overflow = 1
        saturated = 1

    # internal 32-bit Two's Complement representation
    # Masking with 0xFFFFFFFF for a fixed 32-bit bit-width
    internal_bits = val & 0xFFFFFFFF
    
    # Convert to binary string
    binary_str = f"{internal_bits:032b}"
    
    # Binary -> Decimal conversion logic 
    if binary_str[0] == '1':
        decimal_val = int(binary_str, 2) - (1 << 32)
    else:
        decimal_val = int(binary_str, 2)
    
    # Binary -> Hexadecimal conversion logic
    hex_str = f"{int(binary_str, 2):08X}"
    
    # Format output based on selector {DEC, BIN, HEX}
    if format_sel == "DEC":
        value_out = str(decimal_val)
    elif format_sel == "BIN":
        value_out = binary_str
    elif format_sel == "HEX":
        value_out = hex_str
    else:
        raise ValueError("Invalid format selector")
        
    
    return value_out, overflow, saturated   # Return converted value, overflow flag, and saturated flag


# Testing
if __name__ == "__main__":
    tests = [
        ("123", "DEC"),
        ("0", "BIN"),
        ("-123", "HEX"),         
        ("2147483647", "DEC"),   
        ("-2147483648", "HEX"),  
        ("2147483648", "BIN"),   # MAX_INT32 + 1 (Overflow)
        ("-2147483649", "DEC")   # MIN_INT32 - 1 (Overflow)
    ]

    print(f"{'Input':<12} {'Fmt':<5} {'Value Out':<35} {'OVF':<4} {'SAT':<4}")
    for inp, fmt in tests:
        v, o, s = process_data(inp, fmt)

        print(f"{inp:<12} {fmt:<5} {v:<35} {o:<4} {s:<4}")

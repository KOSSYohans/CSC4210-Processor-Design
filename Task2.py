# Name: Yohans Desalgne
# Task 2: Truth Table & K-Map Simplification

import itertools
from sympy import symbols, SOPform, POSform, simplify_logic
import re

def format_boolean(expr):
    # Converts SymPy internal symbols to standard Boolean notation (A'B + C)
    # Convert AND (&) to nothing (AB), OR (|) to (+), and NOT (~) to (')
    s = str(expr).replace(' & ', '').replace(' | ', ' + ')
    # Formats NOT (~A) as Prime (A')
    return re.sub(r'~([A-Z])', r"\1'", s)

def run_task2():
    print("--- Task 2: Boolean Logic Simplification ---")
    
    try:
        n = int(input("Enter the number of variables (n >= 2): "))
        if n < 2: return
    except ValueError: return

    num_rows = 2**n
    print(f"Enter {num_rows} binary digits (the output column):")
    outputs_str = input("> ").strip()

    if len(outputs_str) != num_rows:
        print(f"Error: Need exactly {num_rows} bits.")
        return
    
    outputs = [int(c) for c in outputs_str]
    var_names = [chr(65 + i) for i in range(n)]
    vars_sym = symbols(var_names)
    
    # Output Truth Table
    print("\n[1] Truth Table:")
    print(" | ".join(var_names) + " | Y")
    print("-" * (n * 4 + 5))
    table_rows = list(itertools.product([0, 1], repeat=n))
    for i, row in enumerate(table_rows):
        print(" | ".join(map(str, row)) + f" | {outputs[i]}")

    # Canonical Form
    choice = input("\nChoose form (SOP or POS): ").strip().upper()
    minterms = [int(i) for i, val in enumerate(outputs) if val == 1]
    maxterms = [int(i) for i, val in enumerate(outputs) if val == 0]

    if choice == "SOP":
        if not minterms:
            print("\n[2] Canonical SOP: 0 (Always False)")
            simplified = 0
        else:
            canonical = SOPform(vars_sym, minterms)
            # Use 'dnf' for SOP simplification
            simplified = simplify_logic(canonical, form='dnf')
            print(f"\n[2] Canonical SOP: {format_boolean(canonical)}")
            print(f"[3] Minterms: Σm({', '.join(map(str, minterms))})")
    else:
        if not maxterms:
            print("\n[2] Canonical POS: 1 (Always True)")
            simplified = 1
        else:
            canonical = POSform(vars_sym, maxterms)
            # Use 'cnf' for POS simplification
            simplified = simplify_logic(canonical, form='cnf')
            print(f"\n[2] Canonical POS: {format_boolean(canonical)}")
            print(f"[3] Maxterms: ΠM({', '.join(map(str, maxterms))})")

    # Simplified Expression (Simulated K-Map result)
    if simplified in [0, 1]:
        print(f"\n[4 & 5] Simplified Boolean Expression: {simplified}")
    else:
        print(f"\n[4 & 5] Simplified Boolean Expression: {format_boolean(simplified)}")

    # Validation
    all_pass = True
    for i, row in enumerate(table_rows):
        val_map = {vars_sym[j]: bool(row[j]) for j in range(n)}
        if simplified in [0, 1]:
            res = simplified
        else:
            res = int(bool(simplified.subs(val_map)))
        
        if res != outputs[i]:
            all_pass = False
    
    print(f"\n[6] Validation: {'PASS' if all_pass else 'FAIL'}")

if __name__ == "__main__":
    run_task2()
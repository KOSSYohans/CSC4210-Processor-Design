By: Yohans Desalgne 

Processor Design Project

Course: CSC4210 - Computer Architecture  



**Task 1 Data Systems**

Process 32-bit signed integers, implementing Two's Complement representation and overflow/saturation logic.
Supports Decimal, Binary, and Hexadecimal formatting.

How to run the code:
Make sure python 3 is installed.



**Task 2 Boolean Logic Simplification:**

Short Description:

Python code that automates the creation and simplification of Boolean logic. It takes a truth table and converts it into both Canonical and Simplified Boolean expressions (SOP/POS), simulating the process of K-Map grouping.



Needed to run the Code without Error:

Python 3.x

SymPy library 

Command to install SymPy: (`pip install sympy`)



How To Run the Code:

1\. Run `python task3.py.`

2\. Enter the number of variables.

3\. Provide the output column of your truth table as a binary string (ex: `00010111`).

4\. Select your preferred output form (SOP or POS).



**Task 3 Memory Hierarchy Simulation**:



Models a Samsung-inspired memory subsystem (SSD → DRAM → L3 → L2 → L1)

Tracks total latency for every access.

Data must move through every level.

Implements First-In, First-Out replacement for full caches.

Uses hexadecimal patterns (0xAAAAAAAA) for tracking.


Ensure Python 3 is installed To run the code.

Can video recordings be uploaded to YouTube? I prefer not.

**Task 4 Single-Cycle Processor Design (AND / OR)**

Input values are set inside processor.py in the run() call at the bottom:
cpu.run(A=0b1, B=0b1, C=0b0, D=0b1)
Change A, B, C, D to any 32-bit values to test different inputs.

Expected Output: Instruction execution trace, Control signals per instruction, Register value after each instruction, Final result Y stored in t0.

(NOT operation is not a separate instruction)
The andn instruction sets an invert_a control signal in the ALU, which inverts the first operand before the AND operation.

How to run:
Requirement-Python 3.x (no library needed)
python processor.py / just put all the files in one folder and open inside vscode and run processor.



# Name: Yohans Desalgne
# Task 3: Memory Hierarchy Simulation

class MemoryLevel:
    def __init__(self, name, size, latency):
        self.name = name
        self.size = size #Instructions only
        self.latency = latency #Clock cycles
        self.storage = [] 

    def contains(self, instr):
        return instr in self.storage

    def add(self, instr):
        #FIFO eviction policy
        if len(self.storage) >= self.size:
            self.storage.pop(0)
        self.storage.append(instr)

class MemoryHierarchy:
    def __init__(self, s_size, d_size, l3_size, l2_size, l1_size):
        # Hierarchy SSD > DRAM > L3 > L2 > L1
        self.levels = [
            MemoryLevel("L1 Cache", l1_size, 2),
            MemoryLevel("L2 Cache", l2_size, 10),
            MemoryLevel("L3 Cache", l3_size, 20),
            MemoryLevel("DRAM", d_size, 50),
            MemoryLevel("SSD", s_size, 100)
        ]
        self.total_cycles = 0

    def display_config(self):
        print("- [1] Memory Configuration -")
        for lvl in self.levels:
            print(f"{lvl.name}: {lvl.size} Instr, {lvl.latency} Cycles")

    def read_op(self, instr):
        #Read operation (Fetch)
        print(f"\n[2] Read Access: {instr}")
        found_at = -1
        
        #Hierarchical search
        for i, lvl in enumerate(self.levels):
            self.total_cycles += lvl.latency
            if lvl.contains(instr):
                print(f"  Hit: {lvl.name} (+{lvl.latency} cycles)")
                found_at = i
                break
            print(f"  Miss: {lvl.name} (+{lvl.latency} cycles)")

        # movement: SSD -> DRAM -> L3 -> L2 -> L1
        if found_at > 0:
            print(f"[3] Hierarchical Movement:")
            for i in range(found_at - 1, -1, -1):
                self.levels[i].add(instr)
                print(f"  -> {instr} cached in {self.levels[i].name}")

    def write_op(self, instr):
        # Write operation
        print(f"\n[2] Write Access: {instr}")
        for lvl in self.levels:
            lvl.add(instr)
        print(f"  -> Written to all levels.")

    def final_state(self):
        print(f"\n- [5] Final Memory State -")
        print(f"Total Cycles: {self.total_cycles}")
        for lvl in self.levels:
            print(f"{lvl.name}: {lvl.storage}")

if __name__ == "__main__":
    sim = MemoryHierarchy(s_size=10, d_size=5, l3_size=3, l2_size=2, l1_size=1)
    
    #SSD 32-bit instructions
    sim.levels[4].storage = ["0xAAAAAAAA", "0xFFFFFFFF", "0x00000000"]
    
    sim.display_config()
    sim.read_op("0xAAAAAAAA") #Fetch
    sim.read_op("0xAAAAAAAA") #Cache Hit
    sim.write_op("0xBBBBBBBB") #Write-back
    sim.final_state()
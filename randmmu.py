from mmu import MMU, PTE
import random


class RandMMU(MMU):
    def __init__(self, frames):
        super().__init__(frames)

    def _get_evicted_frame(self):
        if self.frame_count == 0:
            raise ValueError("No item to evict")
        active_index = [i for i in range(self.frames) if self.memory[i] != -1]
        remove_index = random.randint(0, len(active_index) - 1)
        evicted_frame = self.memory[active_index[remove_index]]
        self.log(f"Select frame: {evicted_frame} for removal")
        return evicted_frame


if __name__ == "__main__":
    mmu = RandMMU(3)
    mmu.read_memory(1)
    mmu.read_memory(2)
    mmu.read_memory(3)
    mmu.write_memory(1)
    mmu.write_memory(2)
    mmu.write_memory(3)
    mmu.read_memory(4)
    mmu.read_memory(5)
    mmu.read_memory(6)
    mmu.read_memory(7)
    mmu.read_memory(8)
    mmu.read_memory(9)
    mmu.read_memory(10)
    mmu.read_memory(11)
    mmu.read_memory(12)
    print(f"Write to disk count: {mmu.disk_writes}")
    print(f"Read to disk count: {mmu.disk_reads}")
    print("End")

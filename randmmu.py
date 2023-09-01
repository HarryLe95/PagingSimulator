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


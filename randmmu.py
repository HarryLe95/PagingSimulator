from mmu import MMU, PTE
import random


class RandMMU(MMU):
    def __init__(self, frames):
        super().__init__(frames)
        self.active_frames = []

    def _post_evict_frame_hook(self, page_numer):
        self.active_frames.remove(page_numer)

    def _post_add_frame_hook(self, page_number):
        self.active_frames.append(page_number)

    def _get_evicted_frame(self):
        if self.frame_count == 0:
            raise ValueError("No item to evict")
        frame_id = random.randint(0, self.frame_count - 1)
        return self.active_frames[frame_id]

if __name__ == "__main__":
    mmu = RandMMU(10)
    mmu.read_memory(1)
    mmu.read_memory(2)
    mmu.read_memory(3)
    mmu.read_memory(4)
    mmu.read_memory(5)
    mmu.read_memory(6)
    mmu.read_memory(7)
    mmu.read_memory(8)
    mmu.read_memory(9)
    mmu.read_memory(10)
    mmu.read_memory(11)
    mmu.read_memory(12)
    print("End")
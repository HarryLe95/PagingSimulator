from mmu import MMU


class LruMMU(MMU):
    def __init__(self, frames):
        # TODO: Constructor logic for LruMMU
        super().__init__(frames)
        self.active_frames = []

    def _post_evict_frame_hook(self, page_numer):
        self.active_frames.remove(page_numer)

    def _post_add_frame_hook(self, page_number):
        if page_number in self.active_frames:
            self.active_frames.remove(page_number)
        self.active_frames.append(page_number)

    def _get_evicted_frame(self):
        if len(self.active_frames) != 0:
            return self.active_frames[0]
        raise ValueError("Memory is empty")

if __name__ == "__main__":
    mmu = LruMMU(10)
    mmu.read_memory(1)
    mmu.read_memory(2)
    mmu.read_memory(3)
    mmu.read_memory(4)
    mmu.read_memory(5)
    mmu.read_memory(6)
    mmu.read_memory(7)
    mmu.read_memory(8)
    mmu.read_memory(9)
    mmu.write_memory(1)
    mmu.write_memory(2)
    mmu.read_memory(4)
    mmu.read_memory(11)
    mmu.read_memory(12)
    mmu.read_memory(13)
    mmu.read_memory(14)
    print("End")

from mmu import MMU


class LruMMU(MMU):
    def __init__(self, frames):
        # TODO: Constructor logic for LruMMU
        super().__init__(frames)
        self.page_queue = []

    def access_page(self, page_number, caller_method):
        super().access_page(page_number, caller_method)

        # Only add new page to queue once previous once was removed
        if page_number in self.page_queue:
            self.page_queue.remove(page_number)
        self.page_queue.append(page_number)
        self.log(f"Page queue: {self.page_queue}")

    def _get_evicted_frame(self):
        if len(self.page_queue) != 0:
            return self.page_queue.pop(0)
        raise ValueError("Memory is empty")


if __name__ == "__main__":
    mmu = LruMMU(3)
    mmu.read_memory(0)
    mmu.read_memory(1)
    mmu.read_memory(2)
    mmu.read_memory(0)
    mmu.read_memory(1)
    mmu.read_memory(3)
    mmu.read_memory(0)
    mmu.read_memory(3)
    mmu.read_memory(1)
    mmu.read_memory(2)
    mmu.read_memory(1)
    print("End")

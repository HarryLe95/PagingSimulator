from mmu import MMU


class FifoMMU(MMU):
    def __init__(self, frames):
        # TODO: Constructor logic for LruMMU
        super().__init__(frames)
        self.page_queue = []

    def access_page(self, page_number, caller_method):
        super().access_page(page_number, caller_method)

        # Only add new page to queue once previous once was removed
        if not(page_number in self.page_queue):
            self.page_queue.append(page_number)

    def _get_evicted_frame(self):
        if len(self.page_queue) != 0:
            return self.page_queue.pop(0)
        raise ValueError("Memory is empty")



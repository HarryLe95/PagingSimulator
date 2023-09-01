from mmu import MMU


class ClockMMU(MMU):
    def __init__(self, frames):
        # TODO: Constructor logic for EscMMU
        super().__init__(frames)
        self.second_chance = [0] * self.frames
        self.clock_pointer = 0

    def _get_evicted_frame(self):
        while self.page_table[self.memory[self.clock_pointer]].ACCESS is True:
            self.page_table[self.memory[self.clock_pointer]].ACCESS = False
            self.clock_pointer = (self.clock_pointer + 1) % self.frames
        return_address = self.memory[self.clock_pointer]
        self.log(f"Select frame: {self.memory[self.clock_pointer]} for removal")
        self.clock_pointer = (self.clock_pointer + 1) % self.frames
        return return_address

    def _print_access(self):
        access = [int(self.page_table[item].ACCESS) if item != -1 else -1 for item in self.memory]
        self.log(f"Memory: {self.memory}\tAccess: {access}\tClock: {self.clock_pointer}")


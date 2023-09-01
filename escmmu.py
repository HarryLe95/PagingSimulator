from mmu import MMU


class EscMMU(MMU):
    def __init__(self, frames):
        # TODO: Constructor logic for EscMMU
        super().__init__(frames)
        self.second_chance = [0] * self.frames
        self.clock_pointer = 0

    def write_memory(self, page_number):
        super().write_memory(page_number)
        self.page_table[page_number].SECOND = True

    def _get_evicted_frame(self):
        while ((self.page_table[self.memory[self.clock_pointer]].ACCESS is True) or
               (self.page_table[self.memory[self.clock_pointer]].SECOND is True)):
            if self.page_table[self.memory[self.clock_pointer]].SECOND is True:
                self.page_table[self.memory[self.clock_pointer]].SECOND = False
            else:
                self.page_table[self.memory[self.clock_pointer]].ACCESS = False
            self.clock_pointer = (self.clock_pointer + 1) % self.frames
        return_address = self.memory[self.clock_pointer]
        self.log(f"Select frame: {self.memory[self.clock_pointer]} for removal")
        self.clock_pointer = (self.clock_pointer + 1) % self.frames
        return return_address

    @property
    def second(self):
        return [int(self.page_table[item].SECOND) if item != -1 else -1 for item in self.memory]

    def _print_access(self):
        self.log(f"Memory: {self.memory}\tAccess: {self.access}\tSecond: {self.second}\tClock: {self.clock_pointer}")

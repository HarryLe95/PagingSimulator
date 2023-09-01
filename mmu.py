'''
* Interface for Memory Management Unit.
* The memory management unit should maintain the concept of a page table.
* As pages are read and written to, this changes the pages loaded into the
* the limited number of frames. The MMU keeps records, which will be used
* to analyse the performance of different replacement strategies implemented
* for the MMU.
*
'''
import datetime
from dataclasses import dataclass

VPN = int


@dataclass
class PTE:
    DIRTY: bool = False  # Whether the page is dirty - has been modified since read
    ACCESS: bool = False  # Whether the page has been accessed


class MMU:

    def __init__(self, frames: int, *args, **kwargs):
        self.DEBUG = True
        self.disk_reads = 0
        self.disk_writes = 0
        self.page_faults = 0
        self.frames = frames
        self.frame_count = 0
        self.pointer = 0
        self.memory = [-1] * self.frames
        self.page_table: dict[VPN, PTE] = {}

    def _get_evicted_frame(self):
        return -1

    def _evict_frame(self, page_number: int):
        """
        Remove a frame from main memory. Writes back to disk if dirty.

        Reset ACCESS, DIRTY bits, reduce frame_count, and perform
        post_evict_frame_hook

        :param page_number: page id to evict
        :return:
        """
        self.log(f"CACHE FULL: remove page: {page_number} from memory")
        entry = self.page_table[page_number]
        entry.ACCESS = False
        if entry.DIRTY:
            entry.DIRTY = False
            self.log(f"DIRTY LINE: write page: {page_number} to disk")
            self.disk_writes += 1
        self.pointer = self.memory.index(page_number)
        self.memory[self.pointer] = -1
        self.frame_count -= 1

    def _add_frame(self, page_number: int):
        """
        Add a new frame to memory by reading from disk.

        New entry has PRESENT bit set to 1, also increments page_fault, disk_read, frame_count
        and perform post_add_frame hook

        :param page_number: page number of new entry
        :return:
        """
        # Create a new entry in page table
        self.page_table[page_number] = self.page_table.get(page_number, PTE())
        self.page_table[page_number].ACCESS = True

        # Find unallocated slot to put memory inside
        original_ptr = self.pointer
        while self.memory[self.pointer] != -1:
            self.pointer = (self.pointer + 1) % self.frames
            # No free slot, evict frame
            if original_ptr == self.pointer:
                page_to_remove = self._get_evicted_frame()
                self._evict_frame(page_to_remove)

        # Place page to memory and advance pointer
        self.memory[self.pointer] = page_number
        self.pointer = (self.pointer + 1) % self.frames
        self._print_access()
        # Update counters
        self.page_faults += 1
        self.disk_reads += 1
        self.frame_count += 1

    def access_page(self, page_number, caller_method):
        """
        Create a page table entry in memory by either reading from disk
        or referencing an existing entry.

        If the entry is not present, read from disk and increment disk reads,
        page faults, and frame count. If frame count exceeds maximum count
        evict a page from disk, increase disk_writes and reduce frame count.

        If the entry is present, do nothing.

        :param caller_method: READ/WRITE
        :param page_number: access page number
        """
        if page_number in self.memory:
            self.pointer = self.memory.index(page_number)
            self.log(f"{caller_method}_MEM: CACHE HIT: {page_number}")
            self.page_table[page_number].ACCESS = True
            self._print_access()

        else:  # Page fault event
            self.log(f"{caller_method}_MEM: CACHE MISS. Reading from disk: {page_number}")
            self._add_frame(page_number)

    # Default Interface
    def read_memory(self, page_number):
        self.access_page(page_number, "READ")

    def write_memory(self, page_number):
        self.access_page(page_number, "WRITE")
        self.page_table[page_number].DIRTY = True

    def set_debug(self):
        self.DEBUG = True

    def reset_debug(self):
        self.DEBUG = False

    def get_total_disk_reads(self):
        return self.disk_reads

    def get_total_disk_writes(self):
        return self.disk_writes

    def get_total_page_faults(self):
        return self.page_faults

    def _set_access(self):
        for page_number in self.memory:
            if page_number != -1:
                self.page_table[page_number].ACCESS = False

    @property
    def access(self):
        return [int(self.page_table[item].ACCESS) if item != -1 else -1 for item in self.memory]

    def _print_access(self):
        self.log(f"Memory: {self.memory}\tAccess: {self.access}")

    def log(self, message):
        if self.DEBUG:
            ts = datetime.datetime.now().strftime("%Y-%m-%dT%H:%M:%S")
            name = self.__class__.__name__
            print(f"{ts}|{name}|DEBUG - {message}")

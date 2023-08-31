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
    PRESENT: bool = False  # Whether on disk or has been swapped out
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
        self.memory: dict[VPN, PTE] = {}

    def _get_evicted_frame(self):
        return -1

    def _print_memory(self, active: bool = True):
        self.log("Displaying memory content: ")
        if len(self.memory) == 0:
            print("")
        if active:
            valid_mem = {k: v for k, v in self.memory.items() if v.PRESENT}
        else:
            valid_mem = self.memory
        for k, v in valid_mem.items():
            print(f"VPN: {k}: {v}")

    def _post_add_frame_hook(self, page_numer):
        pass

    def _post_evict_frame_hook(self, page_numer):
        pass

    def _evict_frame(self, page_number: int):
        """
        Remove a frame from main memory. Writes back to disk if dirty.

        Reset PRESENT, ACCESS, DIRTY bits, reduce frame_count, and perform
        post_evict_frame_hook

        :param page_number: page id to evict
        :return:
        """
        self.log(f"CACHE FULL: remove page: {page_number} from memory")
        entry = self.memory[page_number]
        entry.PRESENT = False
        entry.ACCESS = False
        if entry.DIRTY:
            self.log(f"DIRTY LINE: write page: {page_number} to disk")
            self.disk_writes += 1
            entry.DIRTY = False
        self.frame_count -= 1
        self._post_evict_frame_hook(page_number)

    def _add_frame(self, page_number: int):
        """
        Add a new frame to memory by reading from disk.

        New entry has PRESENT bit set to 1, also increments page_fault, disk_read, frame_count
        and perform post_add_frame hook

        :param page_number: page number of new entry
        :return:
        """
        entry = self.memory[page_number]
        entry.PRESENT = True
        self.page_faults += 1
        self.disk_reads += 1
        self.frame_count += 1
        self._post_add_frame_hook(page_number)

    def access_page(self, page_number, caller_method):
        """
        Create a page table entry in memory by either reading from disk
        or referencing an existing entry.

        If the entry is not present, read from disk and increment disk reads,
        page faults, and frame count. If frame count exceeds maximum count
        evict a page from disk, increase disk_writes and reduce frame count.

        If the entry is present, do nothing.

        :param page_number: access page number
        """
        # Create new entry or get existing entry
        self.memory[page_number] = self.memory.get(page_number, PTE())
        entry = self.memory[page_number]
        entry.ACCESS = True

        # Read entry from disk if not present in memory
        if entry.PRESENT:
            self.log(f"MEM_{caller_method} page {page_number}. CACHE HIT.")
        else:
            self.log(f"MEM_{caller_method} page {page_number}. CACHE MISS. Reading from disk")
            self._add_frame(page_number)

        # Evict a page from memory if page full:
        if self.frame_count > self.frames:
            remove_page = self._get_evicted_frame()
            self._evict_frame(remove_page)

    # Default Interface
    def read_memory(self, page_number):
        self.access_page(page_number, "READ")

    def write_memory(self, page_number):
        self.access_page(page_number, "WRITE")
        self.memory[page_number].DIRTY = True

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

    def log(self, message: str):
        if self.DEBUG:
            ts = datetime.datetime.now().strftime("%Y-%m-%dT%H:%M:%S")
            name = self.__class__.__name__
            print(f"{ts}|{name}|DEBUG - {message}")

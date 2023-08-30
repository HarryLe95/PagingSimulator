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


class MMU:
    def __init__(self, *args, **kwargs):
        self.DEBUG = True
        self.disk_reads = 0
        self.disk_writes = 0
        self.page_faults = 0

    def read_memory(self, page_number):
        pass

    def write_memory(self, page_number):
        pass

    def set_debug(self):
        self.DEBUG = True

    def reset_debug(self):
        self.DEBUG = False

    def get_total_disk_reads(self):
        self.log("Get total disk reads")
        return self.disk_reads

    def get_total_disk_writes(self):
        self.log("Get total disk writes")
        return self.disk_writes

    def get_total_page_faults(self):
        self.log("Get total page faults")
        return self.page_faults

    def log(self, message: str):
        if self.DEBUG:
            ts = datetime.datetime.now().strftime("%Y-%m-%dT%H:%M:%S")
            name = self.__class__.__name__
            print(f"{ts}|{name}|DEBUG - {message}")

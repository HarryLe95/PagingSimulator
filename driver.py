from clockmmu import ClockMMU
from lrummu import LruMMU
from randmmu import RandMMU
from escmmu import EscMMU
from fifommu import FifoMMU
import argparse
import os
import matplotlib.pyplot as plt

PAGE_OFFSET = 12


def get_args():
    parser = argparse.ArgumentParser(
        prog="Driver",
        description="Program to generate performance of different cache management algorithms.",
        epilog="Example: python driver.py --dir data --files gcc.trace bzip.trace sixpack.trace swim.trace"
    )
    parser.add_argument("--dir", default="data", help="location of trace files")
    parser.add_argument("--files", action="append", help="trace files as list", required=True)
    return parser.parse_args()


def generate_plot(directory: str, file: str):
    print(f"Processing: {file}")
    frame_counts = [2, 4, 6]
    mmu_dict = {
        "lru": [LruMMU(frames=frame) for frame in frame_counts],
        "clock": [ClockMMU(frames=frame) for frame in frame_counts],
        "esc": [EscMMU(frames=frame) for frame in frame_counts],
        "fifo": [FifoMMU(frames=frame) for frame in frame_counts],
        "random": [RandMMU(frames=frame) for frame in frame_counts]
    }

    input_file = os.path.join(directory, file)
    no_events = 0

    with open(input_file, 'r') as trace_file:
        for trace_line in trace_file:
            trace_cmd = trace_line.strip().split(" ")
            logical_address = int(trace_cmd[0], 16)
            page_number = logical_address >> PAGE_OFFSET

            # Process read or write
            if trace_cmd[1] == "R":
                for _, mmu_list in mmu_dict.items():
                    for mmu in mmu_list:
                        mmu.read_memory(page_number)
            elif trace_cmd[1] == "W":
                for _, mmu_list in mmu_dict.items():
                    for mmu in mmu_list:
                        mmu.write_memory(page_number)
            else:
                print(f"Badly formatted file. Error on line {no_events + 1}")
                return

            no_events += 1

    # Plotting
    hit_rate = {k: [1 - mmu.get_total_page_faults() / no_events for mmu in v] for k, v in mmu_dict.items()}
    fig = plt.figure(figsize=(12, 8))
    for plot_type, plot_item in hit_rate.items():
        plt.plot(frame_counts, plot_item, marker="x", label=plot_type)
    plt.title(f"Plot of Hit Rate vs Frame Count for {file}")
    plt.ylabel("Hit Rate")
    plt.xlabel("Frames")
    plt.legend()
    print(f"Save plot: {file}")
    plt.savefig(f"plots/{file}.png")
    plt.close(fig)


if __name__ == "__main__":
    args = get_args()
    if isinstance(args.files, list):
        for file in args.files:
            generate_plot(args.dir, file)
    else:
        generate_plot(args.dir, args.files)

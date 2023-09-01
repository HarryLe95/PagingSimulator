# How to run this project:

## How to install the dependencies

Before running, make sure you have all the dependencies set up. Firstly, make sure that you are using Python 3.10.

Install poetry:

```bash
pip3 install poetry
```

Install the required packages:

```commandline
poetry install 
```

Enter the virtual environment:

```commandline
poetry shell
```

## Project structure:

Trace data is put in `data/` folder

Unit tests are put in `tests/` folder

## To run the program:

```commandline
python memsim.py <data file> <frames number> <mmu mode> <debugmode>
```

- data file is path to trace file
- frame numbers is the number of frames in virtual memory
- mmu modes - one of lru, clock, fifo, esc
- debug mode - one of debug, quiet

## Testing

To run the trace tests for lru:

```commandline
make lru
```

For clock

```commandline
make clock
```

To run tests in the folder `tests/`

```commandline
make pytest <item>
```

Where item can be clock, esc, fifo, lru 
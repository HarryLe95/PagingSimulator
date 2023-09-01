import pytest

from clockmmu import ClockMMU


@pytest.fixture(scope="function")
def mmu_youtube_stage_1():
    mmu = ClockMMU(11)
    mmu.reset_debug()
    mmu.read_memory(1)
    mmu.read_memory(2)
    mmu.read_memory(3)
    mmu.read_memory(4)
    mmu.read_memory(5)
    mmu.read_memory(6)
    mmu.read_memory(7)
    mmu.read_memory(8)
    mmu.read_memory(9)
    mmu.read_memory(10)
    mmu.read_memory(11)
    mmu._set_access()
    mmu.read_memory(1)
    mmu.read_memory(3)
    mmu.read_memory(6)
    mmu.read_memory(55)
    yield mmu


@pytest.fixture(scope="function")
def mmu_youtube_stage_2(mmu_youtube_stage_1):
    mmu = mmu_youtube_stage_1
    mmu.read_memory(4)
    mmu.read_memory(5)
    mmu.read_memory(77)
    yield mmu


@pytest.fixture(scope="function")
def mmu_texas():
    mmu = ClockMMU(4)
    mmu.reset_debug()
    mmu.read_memory('a')
    mmu.read_memory('b')
    mmu.read_memory('c')
    mmu.read_memory('d')
    yield mmu


@pytest.fixture(scope="function")
def mmu_texas_stage_5(mmu_texas):
    mmu = mmu_texas
    mmu.read_memory('e')
    yield mmu


@pytest.fixture(scope="function")
def mmu_texas_stage_6(mmu_texas_stage_5):
    mmu = mmu_texas_stage_5
    mmu.read_memory('b')
    yield mmu


@pytest.fixture(scope="function")
def mmu_texas_stage_7(mmu_texas_stage_6):
    mmu = mmu_texas_stage_6
    mmu.read_memory('a')
    yield mmu


@pytest.fixture(scope="function")
def mmu_texas_stage_8(mmu_texas_stage_7):
    mmu = mmu_texas_stage_7
    mmu.read_memory('b')
    yield mmu


@pytest.fixture(scope="function")
def mmu_texas_stage_9(mmu_texas_stage_8):
    mmu = mmu_texas_stage_8
    mmu.read_memory('c')
    yield mmu


@pytest.fixture(scope="function")
def mmu_texas_stage_10(mmu_texas_stage_9):
    mmu = mmu_texas_stage_9
    mmu.read_memory('d')
    yield mmu

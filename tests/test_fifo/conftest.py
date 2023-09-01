from fifommu import FifoMMU
import pytest


@pytest.fixture(scope="function")
def mmu_0():
    mmu = FifoMMU(3)
    mmu.reset_debug()
    mmu.read_memory(0)
    mmu.read_memory(1)
    mmu.read_memory(2)
    yield mmu


@pytest.fixture(scope="function")
def mmu_1(mmu_0):
    mmu = mmu_0
    mmu.read_memory(0)
    yield mmu


@pytest.fixture(scope="function")
def mmu_2(mmu_1):
    mmu = mmu_1
    mmu.read_memory(1)
    yield mmu


@pytest.fixture(scope="function")
def mmu_3(mmu_2):
    mmu = mmu_2
    mmu.read_memory(3)
    yield mmu


@pytest.fixture(scope="function")
def mmu_4(mmu_3):
    mmu = mmu_3
    mmu.read_memory(0)
    yield mmu


@pytest.fixture(scope="function")
def mmu_5(mmu_4):
    mmu = mmu_4
    mmu.read_memory(3)
    yield mmu


@pytest.fixture(scope="function")
def mmu_6(mmu_5):
    mmu = mmu_5
    mmu.read_memory(1)
    yield mmu


@pytest.fixture(scope="function")
def mmu_7(mmu_6):
    mmu = mmu_6
    mmu.read_memory(2)
    yield mmu


@pytest.fixture(scope="function")
def mmu_8(mmu_7):
    mmu = mmu_7
    mmu.read_memory(1)
    yield mmu

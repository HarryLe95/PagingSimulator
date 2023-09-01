from lrummu import LruMMU
import pytest


@pytest.fixture(scope="function")
def mmu_4():
    mmu = LruMMU(4)
    mmu.reset_debug()
    mmu.read_memory('a')
    mmu.read_memory('b')
    mmu.read_memory('c')
    mmu.read_memory('d')
    mmu.read_memory('c')
    mmu.read_memory('a')
    mmu.read_memory('d')
    mmu.read_memory('b')
    yield mmu


@pytest.fixture(scope="function")
def mmu_5(mmu_4):
    mmu = mmu_4
    mmu.read_memory('e')
    yield mmu


@pytest.fixture(scope="function")
def mmu_6(mmu_5):
    mmu = mmu_5
    mmu.read_memory('b')
    yield mmu


@pytest.fixture(scope="function")
def mmu_7(mmu_6):
    mmu = mmu_6
    mmu.read_memory('a')
    yield mmu


@pytest.fixture(scope="function")
def mmu_8(mmu_7):
    mmu = mmu_7
    mmu.read_memory('b')
    yield mmu


@pytest.fixture(scope="function")
def mmu_9(mmu_8):
    mmu = mmu_8
    mmu.read_memory('c')
    yield mmu


@pytest.fixture(scope="function")
def mmu_10(mmu_9):
    mmu = mmu_9
    mmu.read_memory('d')
    yield mmu

import pytest

@pytest.mark.skip(reason="Incompatible with the assignment")
def test_youtube_video_stage1(mmu_youtube_stage_1):
    mmu = mmu_youtube_stage_1
    memory = [1, 55, 3, 4, 5, 6, 7, 8, 9, 10, 11]
    access = [0, 1, 1, 0, 0, 1, 0, 0, 0, 0, 0]
    clock = 1
    assert memory == mmu.memory
    assert access == mmu.access
    assert clock == mmu.clock_pointer


@pytest.mark.skip(reason="Incompatible with the assignment")
def test_youtube_video_stage2(mmu_youtube_stage_2):
    mmu = mmu_youtube_stage_2
    memory = [1, 55, 3, 4, 5, 6, 77, 8, 9, 10, 11]
    access = [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0]
    clock = 6
    assert memory == mmu.memory
    assert access == mmu.access
    assert clock == mmu.clock_pointer


def test_texas_init(mmu_texas):
    mmu = mmu_texas
    memory = ['a', 'b', 'c', 'd']
    access = [1, 1, 1, 1]
    clock = 0
    assert memory == mmu.memory
    assert access == mmu.access
    assert clock == mmu.clock_pointer


def test_texas_5(mmu_texas_stage_5):
    mmu = mmu_texas_stage_5
    memory = ['e', 'b', 'c', 'd']
    access = [1, 0, 0, 0]
    clock = 1
    assert memory == mmu.memory
    assert access == mmu.access
    assert clock == mmu.clock_pointer


def test_texas_6(mmu_texas_stage_6):
    mmu = mmu_texas_stage_6
    memory = ['e', 'b', 'c', 'd']
    access = [1, 1, 0, 0]
    clock = 1
    assert memory == mmu.memory
    assert access == mmu.access
    assert clock == mmu.clock_pointer


def test_texas_7(mmu_texas_stage_7):
    mmu = mmu_texas_stage_7
    memory = ['e', 'b', 'a', 'd']
    access = [1, 0, 1, 0]
    clock = 3
    assert memory == mmu.memory
    assert access == mmu.access
    assert clock == mmu.clock_pointer


def test_texas_8(mmu_texas_stage_8):
    mmu = mmu_texas_stage_8
    memory = ['e', 'b', 'a', 'd']
    access = [1, 1, 1, 0]
    clock = 3
    assert memory == mmu.memory
    assert access == mmu.access
    assert clock == mmu.clock_pointer


def test_texas_9(mmu_texas_stage_9):
    mmu = mmu_texas_stage_9
    memory = ['e', 'b', 'a', 'c']
    access = [1, 1, 1, 1]
    clock = 0
    assert memory == mmu.memory
    assert access == mmu.access
    assert clock == mmu.clock_pointer


def test_texas_10(mmu_texas_stage_10):
    mmu = mmu_texas_stage_10
    memory = ['d', 'b', 'a', 'c']
    access = [1, 0, 0, 0]
    clock = 1
    assert memory == mmu.memory
    assert access == mmu.access
    assert clock == mmu.clock_pointer

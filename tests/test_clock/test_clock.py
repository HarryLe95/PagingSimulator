import pytest


@pytest.mark.parametrize(
    "mmu, memory, access, clock",
    [
        ("mmu_texas", ['a', 'b', 'c', 'd'], [1, 1, 1, 1], 0),
        ("mmu_texas_stage_5", ['e', 'b', 'c', 'd'], [1, 0, 0, 0], 1),
        ("mmu_texas_stage_6", ['e', 'b', 'c', 'd'], [1, 1, 0, 0], 1),
        ("mmu_texas_stage_7", ['e', 'b', 'a', 'd'], [1, 0, 1, 0], 3),
        ("mmu_texas_stage_8", ['e', 'b', 'a', 'd'], [1, 1, 1, 0], 3),
        ("mmu_texas_stage_9", ['e', 'b', 'a', 'c'], [1, 1, 1, 1], 0),
        ("mmu_texas_stage_10", ['d', 'b', 'a', 'c'], [1, 0, 0, 0], 1)
    ]
)
def test_texas(mmu, memory, access, clock, request):
    mmu_instance = request.getfixturevalue(mmu)
    assert mmu_instance.memory == memory
    assert mmu_instance.access == access
    assert mmu_instance.clock_pointer == clock

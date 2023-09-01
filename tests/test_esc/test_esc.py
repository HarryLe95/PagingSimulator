import pytest


@pytest.mark.parametrize(
    "mmu, memory, access, second, clock",
    [
        ("mmu_4", ['a', 'b', 'c', 'd'], [1, 1, 1, 1], [1, 1, 0, 0], 0),
        ("mmu_5", ['a', 'b', 'e', 'd'], [0, 0, 1, 0], [0, 0, 0, 0], 3),
        ("mmu_6", ['a', 'b', 'e', 'd'], [0, 1, 1, 0], [0, 0, 0, 0], 3),
        ("mmu_7", ['a', 'b', 'e', 'd'], [1, 1, 1, 0], [1, 0, 0, 0], 3),
        ("mmu_8", ['a', 'b', 'e', 'd'], [1, 1, 1, 0], [1, 0, 0, 0], 3),
        ("mmu_9", ['a', 'b', 'e', 'c'], [1, 1, 1, 1], [1, 0, 0, 0], 0),
        ("mmu_10", ['a', 'd', 'e', 'c'], [0, 1, 0, 0], [0, 0, 0, 0], 2)
    ]
)
def test_esc(mmu, memory, access, second, clock, request):
    mmu_instance = request.getfixturevalue(mmu)
    assert mmu_instance.memory == memory
    assert mmu_instance.access == access
    assert mmu_instance.clock_pointer == clock
    assert mmu_instance.second == second
import pytest


@pytest.mark.parametrize(
    "mmu, queue",
    [
        ("mmu_1", [0, 1, 2]),
        ("mmu_2", [0, 1, 2]),
        ("mmu_3", [1, 2, 3]),
        ("mmu_4", [2, 3, 0]),
        ("mmu_5", [2, 3, 0]),
        ("mmu_6", [3, 0, 1]),
        ("mmu_7", [0, 1, 2]),
        ("mmu_8", [0, 1, 2]),
    ]
)
def test_fifo(mmu, queue, request):
    mmu_instance = request.getfixturevalue(mmu)
    assert mmu_instance.page_queue == queue

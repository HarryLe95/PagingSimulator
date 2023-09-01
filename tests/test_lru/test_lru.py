import pytest


@pytest.mark.parametrize(
    "mmu, queue",
    [
        ("mmu_4", ['c', 'a', 'd', 'b']),
        ("mmu_5", ['a', 'd', 'b', 'e']),
        ("mmu_6", ['a', 'd', 'e', 'b']),
        ("mmu_7", ['d', 'e', 'b', 'a']),
        ("mmu_8", ['d', 'e', 'a', 'b']),
        ("mmu_9", ['e', 'a', 'b', 'c']),
        ("mmu_10", ['a', 'b', 'c', 'd']),
    ]
)
def test_lru(mmu, queue, request):
    mmu_instance = request.getfixturevalue(mmu)
    assert mmu_instance.page_queue == queue

from seedcase_soil.functionals import flat_fmap, fmap, keep, pairwise_fmap


def test_fmap_applies_function_to_each_item():
    assert fmap([1, 2, 3], lambda x: x * 2) == [2, 4, 6]


def test_keep_keeps_matching_items():
    assert keep([1, 2, 3, 4], lambda x: x % 2 == 0) == [2, 4]


def test_flat_fmap_maps_and_flattens_once():
    assert flat_fmap([1, 2, 3], lambda x: [x, x + 10]) == [1, 11, 2, 12, 3, 13]


def test_pairwise_fmap_repeats_singleton_second_list():
    assert pairwise_fmap([1, 2, 3], [10], lambda a, b: a + b) == [11, 12, 13]


def test_pairwise_fmap_pairs_lists_when_same_length():
    assert pairwise_fmap([1, 2, 3], [10, 20, 30], lambda a, b: a + b) == [11, 22, 33]

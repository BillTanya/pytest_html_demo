def test_sample():
    """This is a sample test description."""
    assert 1 == 1


def test_addition():
    """Testing addition operation."""
    assert 1 + 1 == 2


def test_subtraction():
    """Testing subtraction operation."""
    assert 2 - 1 == 1


def test_with_fixture(sample_data):
    """Test using fixture data."""
    assert sample_data["value"] == 42


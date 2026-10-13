"""
    This file is a trivial test case, used only to ensure taht pytest is installed and working as intended.
"""

import pytest

class TestPyTestInstalled:
    # Utility Functions
    def raise_test(self):
        raise SystemExit(1)

    # Test Functions
    def test_one(self):
        """Test assert"""
        assert (3 + 1) == 4

    def test_two(self):
        """Test catching raise"""
        with pytest.raises(SystemExit):
            self.raise_test()

    def test_three(self):
            """Test approx float values"""
            assert (0.1 + 0.2) == pytest.approx(0.3)
    
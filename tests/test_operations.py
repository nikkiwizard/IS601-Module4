import pytest
from app.operations import Operations

# parametrized using Operations static methods
@pytest.mark.parametrize("func,a,b,expected", [
    (Operations.addition, 1, 1, 2),
    (Operations.subtraction, 1, 1, 0),
    (Operations.multiplication, 2, 3, 6),
    (Operations.division, 6, 2, 3),
])
def test_operations(func, a, b, expected):
    assert func(a, b) == expected


def test_division_by_zero():
    """Test division by zero."""
    with pytest.raises(ValueError, match="Division by zero is not allowed."):
        Operations.division(1, 0)
"""
Pytest configuration for shared test helpers.

This module enables assertion rewriting for reusable test utilities
so that helper-level assertions produce pytest-friendly error output.
"""

import pytest

pytest.register_assert_rewrite("test.unit.utils.validator")

"""
A placeholder example of an integration test.
"""

# Core python imports
import logging

# 3rd party imports
import mock
import pytest

# Imports of code-under-test
import {{ cookiecutter.project_module_name }}

# Module variables
_LOGGER = logging.getLogger(__name__)
pytestmark = pytest.mark.integration


def test_no_op():
    """
    Example no-op test
    """
    _LOGGER.debug("Begin test")
    assert True
    _LOGGER.debug("Finished test")

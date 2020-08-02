import pytest
from automation import __version__
from automation.automation import gold_pan


def test_version():
    assert __version__ == '0.1.0'


def test_gold_pan_exists():
    assert gold_pan



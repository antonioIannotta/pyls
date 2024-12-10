import pytest
from utils import format_bytes

def test_format_bytes_kilobytes():
    assert format_bytes(1024) == "1.00 KB"
    assert format_bytes(2048) == "2.00 KB"
    assert format_bytes(1536) == "1.50 KB"

def test_format_bytes_megabytes():
    assert format_bytes(1048576) == "1.00 MB"
    assert format_bytes(1572864) == "1.50 MB"

def test_format_bytes_gigabytes():
    assert format_bytes(1073741824) == "1.00 GB"
    assert format_bytes(1610612736) == "1.50 GB"

def test_format_bytes_terabytes():
    assert format_bytes(1099511627776) == "1.00 TB"
    assert format_bytes(1649267441664) == "1.50 TB"

def test_format_bytes_large_numbers():
    assert format_bytes(1125899906842624) == "1.00 PB"
    assert format_bytes(1688849860263936) == "1.50 PB"

def test_format_bytes_edge_cases():
    assert format_bytes(1023 * 1024) == "1023.00 KB"  # Just under 1 MB
    assert format_bytes(1024 * 1024) == "1.00 MB"     # Exactly 1 MB

def test_format_bytes_negative_values():
    with pytest.raises(ValueError):
        format_bytes(-1)

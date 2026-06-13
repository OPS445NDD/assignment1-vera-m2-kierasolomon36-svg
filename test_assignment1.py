#!/usr/bin/env python3
"""
Author: kiera solomon
"""
import pytest
from assignment1 import day_of_week, leap_year, mon_max, after, valid_date, day_count

def test_leap_year():
    """Test the leap_year function."""
    assert leap_year(2020) is True
    assert leap_year(2021) is False
    assert leap_year(2000) is True
    assert leap_year(1900) is False

def test_mon_max():
    """Test the mon_max function."""
    assert mon_max(1, 2025) == 31
    assert mon_max(2, 2025) == 28
    assert mon_max(2, 2024) == 29  # Leap year February
    assert mon_max(4, 2025) == 30

def test_after():
    """Test the after function."""
    assert after('2025-01-31') == '2025-02-01'
    assert after('2025-02-28') == '2025-03-01'
    assert after('2024-02-29') == '2024-03-01'
    assert after('2025-12-31') == '2026-01-01'

def test_valid_date():
    """Test the valid_date function."""
    assert valid_date('2025-01-01') is True
    assert valid_date('2025-02-30') is False
    assert valid_date('bad-date-str') is False
    assert valid_date('2025-13-01') is False

def test_day_count():
    """Test the day_count function."""
    # May 18, 2023 to June 4, 2023 contains 6 weekend days
    assert day_count('2023-05-18', '2023-06-04') == 6
    # Works when dates are reversed
    assert day_count('2023-06-04', '2023-05-18') == 6

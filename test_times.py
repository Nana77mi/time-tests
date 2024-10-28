
import pytest
import times

# 12
def test_given_input():
    large = times.time_range("2010-01-12 10:00:00", "2010-01-12 12:00:00")
    short = times.time_range("2010-01-12 10:30:00", "2010-01-12 10:45:00", 2, 60)
    result = times.compute_overlap_time(large, short)
    expected = [("2010-01-12 10:30:00", "2010-01-12 10:37:00"), ("2010-01-12 10:38:00", "2010-01-12 10:45:00")]
    assert result == expected

def test_given_input_not_overlap():
    large = times.time_range("2010-01-12 10:00:00", "2010-01-12 12:00:00")
    short = times.time_range("2010-01-12 12:30:00", "2010-01-12 12:45:00", 2, 60)
    result = times.compute_overlap_time(large, short)
    print(result)
    expected = []
    assert result == expected

def test_given_input_each_several_interval():
    large = times.time_range("2010-01-12 10:00:00", "2010-01-12 12:00:00", 3, 45)
    short = times.time_range("2010-01-12 10:30:00", "2010-01-12 10:45:00", 2, 60)
    result = times.compute_overlap_time(large, short)
    expected = [('2010-01-12 10:30:00', '2010-01-12 10:37:00'),
                ('2010-01-12 10:38:00', '2010-01-12 10:39:30'),
                ('2010-01-12 10:40:15', '2010-01-12 10:37:00'),
                ('2010-01-12 10:40:15', '2010-01-12 10:45:00'),
                ('2010-01-12 11:20:30', '2010-01-12 10:37:00'),
                ('2010-01-12 11:20:30', '2010-01-12 10:45:00')]
    assert result == expected

def test_given_input_end_equal_start():
    large = times.time_range("2010-01-12 10:00:00", "2010-01-12 12:00:00")
    short = times.time_range("2010-01-12 12:00:00", "2010-01-12 12:45:00")
    result = times.compute_overlap_time(large, short)
    expected = [('2010-01-12 12:00:00', '2010-01-12 12:00:00')]
    assert result == expected

# bug fixed
def test_given_input1():
    large = times.time_range("2010-01-12 10:00:00", "2010-01-12 12:00:00")
    short = times.time_range("2010-01-12 10:30:00", "2010-01-12 10:45:00", 2, 60)
    result = times.compute_overlap_time_fixed(large, short)
    expected = [("2010-01-12 10:30:00", "2010-01-12 10:37:00"), ("2010-01-12 10:38:00", "2010-01-12 10:45:00")]
    assert result == expected

def test_given_input_not_overlap1():
    large = times.time_range("2010-01-12 10:00:00", "2010-01-12 12:00:00")
    short = times.time_range("2010-01-12 12:30:00", "2010-01-12 12:45:00", 2, 60)
    result = times.compute_overlap_time_fixed(large, short)
    print(result)
    expected = []
    assert result == expected

def test_given_input_each_several_interval1():
    large = times.time_range("2010-01-12 10:00:00", "2010-01-12 12:00:00", 6, 120)
    short = times.time_range("2010-01-12 10:30:00", "2010-01-12 10:45:00", 2, 60)
    result = times.compute_overlap_time_fixed(large, short)
    expected = [('2010-01-12 10:30:00', '2010-01-12 10:37:00'),
                ('2010-01-12 10:38:00', '2010-01-12 10:38:40'),
                ('2010-01-12 10:40:40', '2010-01-12 10:45:00')]
    assert result == expected

def test_given_input_end_equal_start1():
    large = times.time_range("2010-01-12 10:00:00", "2010-01-12 12:00:00")
    short = times.time_range("2010-01-12 12:00:00", "2010-01-12 12:45:00")
    result = times.compute_overlap_time_fixed(large, short)
    expected = [('2010-01-12 12:00:00', '2010-01-12 12:00:00')]
    assert result == expected

def test_time_range_start_after_end():
    flag = True
    test_time = ("2010-01-12 10:00:00", "2010-01-12 08:00:00")
    pytest.raises(ValueError, times.time_range, test_time, flag)
    try:
        test_time = times.time_range_fixed("2010-01-12 10:00:00", "2010-01-12 08:00:00")
    except ValueError:
        print(ValueError)
        flag = False
    assert flag

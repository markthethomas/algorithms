import re
import unittest

"""
Given a time in AM/PM format, convert it to military (24-hour) time.
Note: Midnight is 12:00:00AM on a 12-hour clock and 00:00:00 on a 24-hour clock. Noon is 12:00:00PM on a 12-hour clock and 12:00:00 on a 24-hour clock.
"""


def convertToStandardTime(time):
    time = time.split(':')
    hours = int(time[0])
    minutes = time[1].zfill(2)
    seconds = time[2][:2].zfill(2)
    amPM = time[2][2:]

    match = re.search(amPM, 'PM')
    if match:
        hours += 0 if hours == 12 else 12
    # Account for weirdness of 12:00:00AM
    elif hours == 12:
        hours -= 12

    return str.format('{0}:{1}:{2}', str(hours).zfill(2), minutes, seconds)


class TestTimeConversion(unittest.TestCase):
    """TestTimeConversion"""

    def test_conversion(self):
        self.assertEqual(convertToStandardTime('01:00:00AM'), '01:00:00')
        self.assertEqual(convertToStandardTime('01:00:00AM'), '01:00:00')
        self.assertEqual(convertToStandardTime('07:05:45PM'), '19:05:45')
        self.assertEqual(convertToStandardTime('11:59:59PM'), '23:59:59')
        self.assertEqual(convertToStandardTime('12:45:54PM'), '12:45:54')
        self.assertEqual(convertToStandardTime('12:00:00AM'), '00:00:00')
if __name__ == '__main__':
    unittest.main()

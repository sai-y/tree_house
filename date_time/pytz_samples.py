#!/usr/bin/python3
"""
	Datetime example
"""

import datetime
import pytz


if __name__=="__main__":
	fmt = "%Y %m %d %H:%M"
	current_time = datetime.datetime(2017, 1, 5, 9, 35, 44)
	timezone = pytz.timezone('US/Pacific')

	localized_time = timezone.localize(current_time)

	print(localized_time.astimezone(pytz.timezone('US/Central')).strftime(fmt))
	print(localized_time.astimezone(pytz.timezone('US/Eastern')).strftime(fmt))
	print(localized_time.astimezone(pytz.timezone('Asia/Calcutta')).strftime(fmt))
	print(localized_time.astimezone(pytz.timezone('Europe/Amsterdam')).strftime(fmt))
	print(localized_time.astimezone(pytz.timezone('Australia/Sydney')).strftime(fmt))
	print(localized_time.astimezone(pytz.timezone('America/St_Johns')).strftime(fmt))
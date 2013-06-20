#!/usr/bin/env python
import os
import sys

if __name__ == "__main__":

	#LIVE:
	os.environ.setdefault("DJANGO_SETTINGS_MODULE", "vendors.settings")
	#TEST:
	#os.environ.setdefault("DJANGO_SETTINGS_MODULE", "vendors.TESTsettings")

	from django.core.management import execute_from_command_line
	execute_from_command_line(sys.argv)

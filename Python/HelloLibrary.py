import os.path
import subprocess
import sys

class HelloLibrary(object):

	def __init__(self):
		self.path = os.path.join(os.path.dirname(__file__),'Hello.py')
		self.status = ''
		
	def status_should_be(self, expected_status):
		if expected_status != self.status:
			raise AssertionError("Expected status to be '%s' but was '%s'." % (expected_status, self.status))
								 
	def get_response(self, num):
		command = [sys.executable, self.path, num]
		process = subprocess.Popen(command, universal_newlines=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
		self.status = process.communicate()[0].strip()
from __future__ import print_function
import sys

class Message(object):
    def __init__(self, num):
        self.num = num
				
    def response(self):
       	if self.num == '1':
            return "HELLO WORLD!"
        elif self.num == '2':
            return "HELLO MARS!"
        else:
            return "NO COMMENT!"
			
def get_response(num):
	msg = Message(num)
	print(msg.response())
		
if __name__ == '__main__':
	try:
		get_response(sys.argv[1])
	except IndexError:
		print("No input argument!")
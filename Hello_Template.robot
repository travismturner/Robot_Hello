*** Settings ***
Library		OperatingSystem
Library		HelloLibrary.py


*** Test Cases ***
Test All
	[Template]	Test Response
	1		HELLO WORLD!
	2		HELLO MARS!
	3		NO COMMENT!
		
*** Keywords ***
Test Response
	[Arguments]			${input}	${response}
	Get Response		${input}
	Status Should Be	${response}
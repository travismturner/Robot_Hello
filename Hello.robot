*** Settings ***
Library		OperatingSystem
Library		HelloLibrary.py

*** Test Cases ***
Say Hello World
	Input of one	1

Say Hello Mars
	Input of two	2

Say No Comment
	Other Input 	3
		
*** Keywords ***
Input of one
	[Arguments]			${one}
	Get Response		${one}
	Status Should Be	HELLO WORLD!
	
Input of two
	[Arguments]			${two}
	Get Response		${two}
	Status Should Be	HELLO MARS!
	
Other Input
	[Arguments]			${three}
	Get Response		${three}
	Status Should Be	NO COMMENT!
	
	
	

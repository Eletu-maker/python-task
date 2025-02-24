<<<<<<< HEAD
from typing import List
print("MBTI Personality Test")


answer: List[str] = []  
number: List[int] = []
name = input("what is your name: ")
ans = 'q'
troversion = 'q'
introversion =0
extroversion =0
focus = 'q'
sensing = 0
Intuition =0
dMaking = 'q'
thinking = 0
feeling =0
lifestyle = 'q'
judging = 0
perceiving = 0
question =  [
"0.A: expend energy, enjoy groups  |B: conserve energy, enjoy one-on-one ",
"1.A: interpret literally |B: look for meaning and possibilities ",
"2.A: logical, thinking, questioning |B: empathetic, feeling, accommodating",
"3.A: organized, orderly |B: flexible, adaptable ",
"4.A: more outgoing, think out loud |B: more reserved, think to yourself ", 
"5.A: practical, realistic, experiential |B: imaginative, innovative, theoretical",
"6.A: candid, straight forward, frank |B: tactful, kind, encouraging",
"7.A: plan, schedule |B: unplanned, spontaneous",
"8.A: seek many tasks, public activities, interaction with others |B: seek private, solitary activities with quiet to  concentrate ",
"9.A: Standard, usual, conventional |B: different, novel, unique",
"10.A: firm, tend to criticize, hold the line |B: gentle, tend to appreciate, conciliate", 
"11.A: regulated, structured |B: easygoing, 'live' and 'let live'",
"12.A: external, communicative, express yourself |B: internal, reticent, keep to yourself",
"13.A: focus on here-and-now |B: look to the future, global perspective, 'big picture'",
"14.A: tough-minded, just |B: tender-hearted, merciful", 
"15.A: preparation, plan ahead |B: go with the flow, adapt as you go", 
"16.A: active, initiate |B: reflective, deliberate",
"17.A: facts, things, 'what is' |B: ideas, dreams, 'what could be,' philosophical",
"18.A: matter of fact, issue-oriented |B: sensitive, people-oriented, compassionate", 
"19.A: control, govern |B: latitude, freedom"]
for x in range (20):
	
	print(question[x])
	ans=input()
	first_letter = ans[0]
	while len(ans) > 1:
		print("input a single digit: either enter A or B")
		ans=input()
		first_letter = ans[0]
	while first_letter not in ['A' , 'B','a','b']:
		print("wrong option: either enter A or B")
		ans=input()
		first_letter = ans[0]
	answer.append(first_letter)
	


for x in range(0,20,4):
	if answer[x] in ['A','a']:
		extroversion +=1
		
	elif answer[x] in ['B','b'] : 
		introversion +=1
		
for x in range(1,20,4):
	if answer[x] in ['A','a']:
		sensing +=1
		
	elif answer[x] in ['B','b'] : 
		Intuition +=1

for x in range(2,20,4):
	if answer[x] in ['A','a']:
		thinking +=1
		
	elif answer[x] in ['B','b'] : 
		feeling +=1
for x in range(3,20,4):
	if answer[x] in ['A','a']:
		judging +=1
		
	elif answer[x] in ['B','b'] : 
		perceiving +=1
if extroversion > introversion:
	troversion = 'E'
else :
	troversion = 'I'
if sensing > Intuition:
	focus = 'S'
else : 
	focus = 'N'
if thinking > feeling:
	dMaking = 'T'
else :
	dMaking = 'F'
if judging > perceiving:
	lifestyle = 'J'
else : 
	lifestyle = 'P'


personality = troversion + focus + dMaking + lifestyle
print(personality)
=======
from typing import List
print("MBTI Personality Test")


answer: List[str] = []  
number: List[int] = []
name = input("what is your name: ")
ans = 'q'
troversion = 'q'
introversion =0
extroversion =0
focus = 'q'
sensing = 0
Intuition =0
dMaking = 'q'
thinking = 0
feeling =0
lifestyle = 'q'
judging = 0
perceiving = 0
question =  [
"0.A: expend energy, enjoy groups  |B: conserve energy, enjoy one-on-one ",
"1.A: interpret literally |B: look for meaning and possibilities ",
"2.A: logical, thinking, questioning |B: empathetic, feeling, accommodating",
"3.A: organized, orderly |B: flexible, adaptable ",
"4.A: more outgoing, think out loud |B: more reserved, think to yourself ", 
"5.A: practical, realistic, experiential |B: imaginative, innovative, theoretical",
"6.A: candid, straight forward, frank |B: tactful, kind, encouraging",
"7.A: plan, schedule |B: unplanned, spontaneous",
"8.A: seek many tasks, public activities, interaction with others |B: seek private, solitary activities with quiet to  concentrate ",
"9.A: Standard, usual, conventional |B: different, novel, unique",
"10.A: firm, tend to criticize, hold the line |B: gentle, tend to appreciate, conciliate", 
"11.A: regulated, structured |B: easygoing, 'live' and 'let live'",
"12.A: external, communicative, express yourself |B: internal, reticent, keep to yourself",
"13.A: focus on here-and-now |B: look to the future, global perspective, 'big picture'",
"14.A: tough-minded, just |B: tender-hearted, merciful", 
"15.A: preparation, plan ahead |B: go with the flow, adapt as you go", 
"16.A: active, initiate |B: reflective, deliberate",
"17.A: facts, things, 'what is' |B: ideas, dreams, 'what could be,' philosophical",
"18.A: matter of fact, issue-oriented |B: sensitive, people-oriented, compassionate", 
"19.A: control, govern |B: latitude, freedom"]
for x in range (20):
	
	print(question[x])
	ans=input()
	first_letter = ans[0]
	while len(ans) > 1:
		print("input a single digit: either enter A or B")
		ans=input()
		first_letter = ans[0]
	while first_letter not in ['A' , 'B','a','b']:
		print("wrong option: either enter A or B")
		ans=input()
		first_letter = ans[0]
	answer.append(first_letter)
	


for x in range(0,20,4):
	if answer[x] in ['A','a']:
		extroversion +=1
		
	elif answer[x] in ['B','b'] : 
		introversion +=1
		
for x in range(1,20,4):
	if answer[x] in ['A','a']:
		sensing +=1
		
	elif answer[x] in ['B','b'] : 
		Intuition +=1

for x in range(2,20,4):
	if answer[x] in ['A','a']:
		thinking +=1
		
	elif answer[x] in ['B','b'] : 
		feeling +=1
for x in range(3,20,4):
	if answer[x] in ['A','a']:
		judging +=1
		
	elif answer[x] in ['B','b'] : 
		perceiving +=1
if extroversion > introversion:
	troversion = 'E'
else :
	troversion = 'I'
if sensing > Intuition:
	focus = 'S'
else : 
	focus = 'N'
if thinking > feeling:
	dMaking = 'T'
else :
	dMaking = 'F'
if judging > perceiving:
	lifestyle = 'J'
else : 
	lifestyle = 'P'


personality = troversion + focus + dMaking + lifestyle
print(personality)
>>>>>>> 2184dc57dc7539e7209df1e7152358ab642e28f7

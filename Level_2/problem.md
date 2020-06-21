# Lovely Lucky LAMBs

Being a henchman isn't all drudgery. Occasionally, when Commander Lambda is feeling generous,
she'll hand out Lucky LAMBs (Lambda's All-purpose Money Bucks). Henchmen can use Lucky LAMBs to buy things like a second pair of socks,
a pillow for their bunks, or even a third daily meal! However, actually passing out LAMBs isn't easy.
Each henchman squad has a strict seniority ranking which must be respected - 
or else the henchmen will revolt and you'll all get demoted back to minions again!

There are 4 key rules which you must follow in order to avoid a revolt:
       - The most junior henchman (with the least seniority) gets exactly 1 LAMB. (There will always be at least 1 henchman on a team.)
       - A henchman will revolt if the person who ranks immediately above them gets more than double the number of LAMBs they do.
       - A henchman will revolt if the amount of LAMBs given to their next two subordinates combined is more than the number of LAMBs they get.
	(Note that the two most junior henchmen won't have two subordinates, so this rule doesn't apply to them. The 2nd most junior henchman would require at least as many LAMBs as the most junior henchman.)
       - You can always find more henchmen to pay - the Commander has plenty of employees. If there are enough LAMBs left over such that another henchman could be added as the most senior
	while obeying the other rules, you must always add and pay that henchman.

Note that you may not be able to hand out all the LAMBs.
A single LAMB cannot be subdivided. That is, all henchmen must get a positive integer number of LAMBs.

Write a function called answer(total_lambs), where total_lambs is the integer number of LAMBs in the handout you are trying to divide.
It should return an integer which represents the difference between the minimum and maximum number of henchmen who can share the LAMBs
(that is, being as generous as possible to those you pay and as stingy as possible, respectively) while still obeying all of the above rules to avoid a revolt.

For instance, if you had 10 LAMBs and were as generous as possible, you could only pay 3 henchmen (1, 2, and 4 LAMBs, in order of ascending seniority),
whereas if you were as stingy as possible, you could pay 4 henchmen (1, 1, 2, and 3 LAMBs). Therefore, answer(10) should return 4-3 = 1.
To keep things interesting, Commander Lambda varies the sizes of the Lucky LAMB payouts: you can expect total_lambs to always be between 10 and 1 billion (10 ^ 9).



# Please Pass the Coded Messages

You need to pass a message to the bunny prisoners, but to avoid detection, the code you agreed to use is... obscure, to say the least.
The bunnies are given food on standard-issue prison plates that are stamped with the numbers 0-9 for easier sorting,
and you need to combine sets of plates to create the numbers in the code. The signal that a number is part of the code is that it is divisible by 3.
You can do smaller numbers like 15 and 45 easily, but bigger numbers like 144 and 414 are a little trickier.
Write a program to help yourself quickly create large numbers for use in the code, given a limited number of plates to work with.

You have L, a list containing some digits (0 to 9). Write a function answer(L) which finds the largest number that can be made from some or 
all of these digits and is divisible by 3. If it is not possible to make such a number, return 0 as the answer. L will contain anywhere from 1 to 9 digits. 
The same digit may appear multiple times in the list, but each element in the list may only be used once.

Test cases

Inputs: (int list) l = [3, 1, 4, 1] Output: (int) 4311

Inputs: (int list) l = [3, 1, 4, 1, 5, 9] Output: (int) 94311

 
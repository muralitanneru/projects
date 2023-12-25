# Minimal-cost-to-reach-step-N

TASKS:
Minimal cost for climbing a tower.
Problem Description:
You are climbing a tower which is n steps high from the ground. To climb the tower
from ground to the top, you have to pay and costi is the cost you have to pay when you
climb from step i. Once costi is paid, you can choose 1 or 2 steps to take forward.
Initially, you can start from either step 0 or step 1. If you are aware of the price list at
each step, please design and implement a program returning the minimal cost to arrive at
the top of the tower, which is step n.
For example:
n=9
cost0=1 cost6=1
cost1=100 cost7=1
cost2=1 cost8=80
cost3=1 cost9=1
cost4=1
cost5=90
The minimal cost is 6.
Solution:
Start from step 0;
Pay 1, and take 2 steps, reaches step2;
Pay 1, and take 2 steps, reaches step4;
Pay 1, and take 2 steps, reaches step6;
Pay 1, and take 1 step, reaches step7;
Pay 1, and take 2 steps, reaches step9;
Pay 1, and take 1 step, reaches the top.
Total cost: 6

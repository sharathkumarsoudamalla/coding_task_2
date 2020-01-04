# Coding Task 2
*merge.py* consists of the function which merges the overlapping intervals.
*test_merge.py* contains the unit test for the 'merge_interval' function.
## Solution idea
First the input interval list is flattened to specific bound and connected them with integer that identifies if the bound is upper or lower. Sorting operation is performed on this list. Items are pushed into stack if they are lower bound and are popped out when upper bound item arrives. When the stack is empty merged interval is obtained.

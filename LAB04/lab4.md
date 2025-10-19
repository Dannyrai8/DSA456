Team Members: Danny Rai and Nima Angdick Bhtoea
# Part A 
## Q1
:- The speaker was talking about improving the the standard library sort which is a hybrid sorting algorithim that uses Quicksort, Heapsort and Insertion sort.

## Q2
:- VS performs a simpler sort algorithm instead of continuing to partition at 16 elements.

## Q3
:- GNU performs a simpler sort algorith instead of continuing partition at 32 elements.

## Q4
:- Switching to binary search does not improve insertion sort because the cost of insertion comes from moving elements and not comparing them. 

## Q5
:- It is the CPU optimization that tries to guess the outcome of conditional branches to keep the instruction pipeline full and avoid delays. Here branch refers to the if, for or while loops where it needs to decide which path to take and branch prediction is the CPU feature where it avoids waiting for the condition to end by predicting a result.

## Q6
:- Infromational entropy refers to the amount of uncertainty or unpredictability in a set of data. Where low entropy refers to an almost sorted or true conditions where as high entropy where high entropy refers to a random array where any given condition may or maynot be true hindering the predictability of the cpu.

## Q7
:- ungaurded_insertion_sort is a faster version of insertion sort because insertion sort must check wheather it has reached the start of the array while inserting elements these conditions add extra branches that slow down execution. so by first calling make_heap() it creates a guard element that is smaller than all other elements which will make sure that the insertion loop never goes out of bounds so the boundry checks are no longer needed.

## Q8
:- The speaker is telling us to avoid using if statements by using mathematical or bitwise operations instead which will remove unpredictable branches, which will help the CPU's branch predictor work mroe efficiently.
example : if(a < b) swap (a, b);
instead we use 
bool cond = (a < b);
a = cond ? b : a;
b = cond ? a : b;


## Q9
:- The bug in GNU's implementaiton of std::sort happens due to how the algorithm switched between sorting methods at small partitions. Under some conditions the transition was not handled correctly. It is beacuse it used unguarded insertion sort without a proper guard element which caused out of bounds behavior.

## Q10
:- The graphs measured metrics like number of comparisions, number of moves and execution of time. But the missing metric that was suggested by the graphs was the branch misprediction rate. He found about about using the blended cost after increasing threshold which also include the distance two array axises.

## Q11
:- It means that fast code tends to follow predictable branches mainly favouring one common path of execution ptah which minimizes branch predictions, keeping the cpu pipeline efficient and the algorithm faster overall.

## Q12
:- Here the hot code refers to the code that is run very constantly like code inside a loop and cold refers the code that is run very rarely. he suggsets that using them seperately improves cpu cache effeciency, branch prediction accuracu, and overall program speed.

# Part B 

## Q1
:- The most challenging part for me was about first getting to know what was happening as it was showing graphs and was talking about cpu, branch, boundries and many others which I overcame after going through the video multiple times.

## Q2
:- The most surpring thing that I witnessed was how deeply all the professors have studied in this field. Although, I have worked with pixels, and mathematical expresions in c code but getting to know how the cpu works and how it is constantly trying to figure out ways to find faster and better ways to solve problems really surprised me.

## Q3
:- Yes, I learned that on top of all the algorithamic forms ther are other key forms like cpu predictions and code tendencies to follow bit wise operators for condiitonal statements.

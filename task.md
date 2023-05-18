# Find closest answer to 0

The goal of this challenge is to find a sequence of the numbers given in the input (__*numbers.txt*__) that after calculations the result is closest or equal to 0, where:  
- Number with even index is summed
- Number with odd index is substracted

Example:

## Input
```
1
3
5
6
10
13
20
30
40
60
```
## Example answer
```
30
10
40
20
6
3
5
1
13
60
```
## Explanation:
```
30-10+40-20+6-3+5-1+13-60 = 0
```
## Assumptions:
The input is provided in the `numbers.txt`. The sequence is not sorted. There is no one correct answer. The result of the calculation does not has to be equal to 0, but the closest to it wins. 

## Results 
The correctness of the answer can be verified with the script `test.py`

usage:
```
python test.py results_file.txt
```

Results send to the email: [p.guzik@falconvsystems.com](p.guzik@falconvsystems.com). The answer shall include:
- code that generates output
- file with the output sequence, please use your nickname as a file name

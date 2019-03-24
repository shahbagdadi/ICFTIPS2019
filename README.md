# ICFTIPS2019
Code repository for algorithm and data structure problems discussed during ICF TIPS 2019 Spring session

## Repository Structure
    1. Each section is checked in under corresponding folder ex "recursion" , "trees", "arrays etc.
    2. Each problem is filed under the corresponding section with its name.
    3. Every problem has a README with the problem details and and sample input. Note : Not all possible cases may be covered by these input. You are encouraged to try your solution with all possible inputs.
    4. The master branch will only have the questions. Students have to create a branch with their name and commit code to that branch. If you code in java then put your solution in java/src/main.java. If you code in python then put your source code in python/src/main.py
    
## Steps to submit code for review
1. Clone the repo (initial)
2. Get the latest from master.
``` 
git checkout master   
git pull 
```
3. Create a branch with your name. The branch should follow the Naming Convention : **YourName**. 
``` git checkout -b <YourName>
    example - git checkout -b shahnawaz
 ```
4. Work on the problem and commit code to your branch. **Include the time and space complexity as a comment in your source code** like below
```     
    // T - O(n) where n is the number of elements
    // S - O(log n) where n is the number of elements
```
Commit the code to your branch. Make sure your code is compilable and successfully executes at least all the test cases given with the problem.
```
git status
git add <some-file>
git commit -m <A meaningful message>
git push origin <YourName>
```
5. Share the link to your main source file in Google Classroom so it can be reviewed.

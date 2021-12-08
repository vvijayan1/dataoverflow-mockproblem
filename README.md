# Data Overflow Mock Problem
Data overflow contest mock problem.
## Location Aggregation
We have a TSV(Tab Separated value) file containing user_id and location_id in each line, the goal of this task is to aggregate the user visitation into a output TSV file containing user_id and the location_ids in a single line without any duplicates

**Note** :  user_id and location_id are integers, user_id represents a user and location_id represents a location.

### Input File(s)
```
USER_ID LOCATION_ID
1234    1
1234    2
1245    6
1293    7
1234    4
1245    5
1293    4
2345    1
1234    1
```
  
### Output File
```
1234    1,2,4
1245    6,5
1293    7,4
2345    1
```

The code will be tested against test cases.
For performance we are testing the code with a file having 1million records, 10 million records and 100 million records
### Hardware Requirement:
 1GB RAM, 2 core CPU
 

## How to get started with the repository?
* Login to github and visit the [repository](https://github.com/affinityanswers/dataoverflow-mockproblem/).
* Fork the repository by clicking the fork button.
![Fork](images/fork.png)
* [Clone](https://git-scm.com/book/en/v2/Git-Basics-Getting-a-Git-Repository#_git_cloning) the forked respository to the local machine.
![Clone](images/clone.png)
* Start writing your code by updating the `location_aggregation` function in the `code/script.py`  feel free add/modify the code.
* If your code is using additional libraries please mention it in the `requirements.txt`.
* Run the basic test cases by running.
  
  ```python3 wrapper.py test```
  
  This tests your code with basic test cases.
* To run your code with the given sample input file, please run

```python3 wrapper.py run -i {input_file_1} {input_file_2} -o output_file.tsv```
* Once you are happy with the code, commit the code
* Submit your github repository link along with the commit id in our [website](https://dataoverflow.affinityanswers.com).

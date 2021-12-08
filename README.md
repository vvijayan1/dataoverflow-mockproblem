# Data Overflow Mock Problem
Data overflow contest mockprobem and solution.
## Location Aggregation
We have a TSV(Tab Separated value) file containing user_id and location_id in each line, the goal of this task is to aggregate the user visitation into a output TSV file containing user_id and the location_ids in a single line without any duplicates
Note: user_id and location_id are integers, user_id represents a user and location_id represents a location.

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
 
## Best Practices.
* Follow the PEP8 style guide from [here](https://www.python.org/dev/peps/pep-0008/)
* Write modular code so that functions are easy to test and resuse.

## How to get started with the repository?
* Login to github and visit the [repository](https://github.com/affinityanswers/dataoverflow-mockproblem/).
* Fork the repository by clicking the fork button.
* [Clone](https://git-scm.com/book/en/v2/Git-Basics-Getting-a-Git-Repository#_git_cloning) the forked respository to the local machine
* Start writing your code by updating the `script.py` in `location_aggregation` function feel free add/modify the code, do not modify the main function and the exisitng import statements.
* If your code is using additional libraries please mention it in the `requirements.txt`.
* Run the basic test cases by running.
  ```python3 script.py test```
  This tests your code with basic test cases.
* Once you are happy with the code, commit the code
* Submit your github repository link along with the commit id in our [website](https://dataoverflow.affinityanswers.com).

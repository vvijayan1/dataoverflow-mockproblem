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

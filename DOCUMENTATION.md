# Circular Societies Visualization Tool

## Documentation

### Creating a circular society object:

`CircularSociety( name, modulo, isUniform = 0, tick = 0.5 )`

+ `name`: string, a name for this society
+ `modulo`: positive integer, the circular society will have [0, `modulo`] as its spectrum, with 0 and `modulo` identified
+ `tick`: (Optional) numerical; the default is 0.5.   This determines the x-axis tickmark in the visualization

### Methods for the `CircularSociety` object:

#### Methods for displaying basic information of the circular society
+ `.listApprovalSets()`: listing the approval sets in this society
+ `.printSocietyInfo()`: displaying the circular society's information (name, is it uniform, the spectrum, number of voters, list of approval sets) 
+ `.listSetEndpoints( )`: method to list the endpoints of the set, starting from the left-most (from 0).

#### Methods for finding, editing, adding, removing approval sets from the circular society:
+ `.addApprovalSet( setName, left_endpt, right_endpt )`
    + `setName`: string, name for the new set
    + `left_endpt`: numerical, the left endpoint of the new set (does not have to be smaller than `right_endpt`)
    + `right_endpt`: numerical, the right endpoint of the new set
+ `.removeApprovalSet( setName )`: removing an existing approval set/voter
    + `setName`: string, name of the set to be removed.  If setName is not found in the list of sets, an error message will be displayed
+ `.editApprovalSet( setName, newleft_endpt, newright_endpt )`: editing an existing approval set
    + `setName`: string, name of the set to be edited.  If setName is not found in the list of sets, an error message will be displayed
    + `newleft_endpt`: numerical, the new left endpoint of the set
    + `right_endpt`: numerical, the new right endpoint of the set

#### Methods for finding agreement and piercing numbers
+ `.checkAgreeability( k, m)`: method that returns (1) a True or False value (true if the society is (k, m)-agreeable), and (2) a list of "bad collections of m approval sets"--if the society is (k, m)-agreeable, then this is empty
+ `.findAgreementNumber( )`: method that returns (1) the agreement number of the society and (2) the location where it is attained (if there are multiple locations, only the leftmost will be returned).  This method only checks points that are also endpoints of an approval set
+ `.findPiercingNumber( )`: method that finds the piercing number of the society.  The candidates for piercing points are endpoints of the approval sets.  The method formulates the problem as an integer linear program, solved using the `cvxpy` library.  Outputs:
  + `piercingNumber`: the piercing number
  + `piercingSet`: the set of points that pierce the approval sets 
  + `x.value`: the optimal solution of the integer linear programming problem
  + `Mat`: the `A` matrix involved in the integer linear programming formulation
+ `.piercingAlgorithm( startingPoint = 0 )`: an implementation of the linear society piercing set algorithm
  + Input: `startingPoint` is where we want to start the algorithm (a reference point for "leftmost". The default value is 0.
  + Output: a piercing set 

#### Methods related to Hardin's transformation (containment, LR-alternation)
+ `.checkContainmentPair( setPair )`: method that returns True if one of the sets in the given pair is contained in the other.  The input `setPair` is a list containing the string names of the two sets
+ `.checkContainmentAll( findContainmentPairs = False )`: method that check if there is any containment among all approval sets in the circular society.
  + If `findContainmentPairs = False`, then the method returns True if there is a containment and False otherwise.
  + If `findContainmentPairs = True`, then the method returns two outputs: the first is True/False indicating if there is containment; the second output is a list that contains pairs of sets (one of the sets in each pair is contained in the other one)
+ `.eliminateContainmentPair( containmentPair  )`: method that switches the right endpoints of two sets where one was contained in the other.
    + `containmentPair `: list of two approval sets' string names 
+ `.eliminateContainmentAll( )`: loops over all pairs of approval sets and check pairwise containment
+ `.is_LR_alt( findRRL )`: method that 
  1. returns `True` or `False`, checking if the set is left-right alternating or not and 
  2. if `findRRL` is True, also returns a list containing lists of 3 approval  sets that attain RRL endpoints (if the set is LR alternating, this list is empty).  The default is `findRRL=False`
+ `.eliminateRRLTriple( RRLsets )`: method that switches the right endpoints of the RL set in an RRL triple, to create an RLR triple
  + `RRLsets`: a list of three set names that attains the RRL endpoints (in order)
+ `.eliminateRRLAll( maxIt )`: method that eliminates all RRL triples, achieving a LR-alternating society, up to a given number of iterations.  If maximum iteration is achieved without achieving LR-alternation, a message indicating this is displayed.
  + `maxIt`: max number of iteration.  The default is 100.
+ `.uniformize()`: calls `.eliminateContainmentAll( )` followed by `.eliminateRRLAll( )`, transforming society into Hardin's uniform society.



#### Methods for visualizing the circular society
+ `.visualize( )`: visualizing the sets in this circular society; each set is plotted horizontally (different y coordinates for different sets)

### Function to create Hardin's Uniform Society:
+ `generateUniformCircularSociety( societyname, N, h, epsilon = 0.5 )`:
    + `societyname`: string, name of the society
    + `N`: positive integer, number of approval sets
    + `h`: positive integer, length of the sets, also the agreement number of the socity
    + `epsilon`: (Optional), numerical, the default is 0.5; perturbs the right endpoint (instead of having the right endpoint of the interval be open)
	
### Functions to randomly generate a circular society:
+ `generateRandomSociety( societyname, N, modulo, epsilon = 0.5, mode = 1, a = 1, b = 1 )`:
    + `societyname`: string, name of the society
    + `N`: positive integer, number of approval sets
    + `modulo`: positive integer, the circular society will have [0, `modulo`] as its spectrum, with 0 and `modulo` identified
   + `mode`: (Optional) lets us choose how the approval sets are generated
      + `mode = 1`: for each set, left and right endpoints are chosen uniformly at random from [0, `modulo`]
      + `mode = 2`: for each set, left endpoint is chosen uniformly at random from [0, `modulo`]; the length is chosen from `modulo` * beta distribution with parameters `a`, `b`.  The default values are `a = 1` and `b = 1`,  which reduces to the uniform distribution  

  + `epsilon`: (Optional), numerical, the default is 0.5; perturbs the right endpoint (instead of having the right endpoint of the interval be open)

+ `generateRandomFixedLengthSociety( societyname, N, modulo, p, tick = 0.5 )`:
  + `N` is number of voters
  + `modulo` is the circumference of the circular society
  + `p` is a fraction between 0 and 1 that controls the length of approval sets
    + the length of each set is `p` times `modulo`
  + `tick`: controls tick marks in the visualization.  The default value is 0.5


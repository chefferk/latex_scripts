# <img src="https://github.com/chefferk/latex_scripts/blob/master/Notes/latex.png?raw=true" height="30px"/> Scripts

Some Python scipts to better work with [TAMU Logic Daemon](http://logic.tamu.edu/daemon.html)

## Working definitions
<kbd><img src="http://logic.tamu.edu/Images/lop.gif"/></kbd>

## Prerequisites

Regular expression module (embedded inside Python)

```
import re
```
## Getting started


## Known problems
* The program changes 'v's in annotations to ' \vee '
  * FIX: just change the LaTex back to 'v'
  * TODO(1) : only want this to apply to sentences
```
Uni \vee ersal Instantiation
```
* The program will overwrite annotaions, similar problem as above 
  * FIX: change the LaTex back to correct, this one is a little harder to notice sometimes
  * TODO(2) : only want this to apply to annotations
  * Could possibly use regex to parse two spaces as boundary for sentences
```
Reductio ad Premisebsurdum
```
* Needs to be in *correct* form
  * No spaces in sentences (spaces are fine in first line)
    * TODO : leverage regex better to parse sentences and not have to remove spaces
  * Space between annotaion set and annotaion
    * TODO : this should be easy to split
  * Cannot have empy assumption set (e.g. axioms)
    * FIX: add a chracter place holder (e.g. 'x') and remove it later
    * TODO : find a fix for this

```
P v Q, ~P v R |- Q v R
1       (1)   PvQ        A
2       (2)   ~PvR       A
1       (3)   ~Q->P      1 v->
2       (4)   P->R       2 v->
1,2     (5)   ~Q->R      3,4 HS
1,2     (6)   QvR        5 v->
```

## Contributing

Please read [CONTRIBUTING.md](https://gist.github.com/PurpleBooth/b24679402957c63ec426) for details on our code of conduct, and the process for submitting pull requests to us.

## Authors

* **Keaton Cheffer** - *Initial work*

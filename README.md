# <img src="https://github.com/chefferk/latex_scripts/blob/master/Notes/latex.png?raw=true" height="30px"/> Scripts

Some Python scripts to better work with [TAMU Logic Daemon](http://logic.tamu.edu/daemon.html)

## Working definitions
<kbd><img src="http://logic.tamu.edu/Images/lop.gif"/></kbd>

## Prerequisites

Regular expression module (embedded inside Python)

```
import re
```
## Getting started
Howdy!

I started this as a fun way to save some time but found it to be quite [valuable](https://github.com/chefferk/latex_scripts/blob/master/Notes/proofs_tex.pdf). I want to pass this on to anyone who is interested as there are several things that could be improved and added. I, unfortunately, do not have as much free time as I would like to work on this, so this is the perfect way to get some of those features added!

There are several files but I have mainly been working on the `logic_to_latex.py` as that is the most beneficial right now. I created a file for `latex_to_logic.py` which could be useful and the `scripts.py` which would be used as a command line interface with options.

The `logic_to_latex.py` opens the `logic.txt` file where I just copy and paste the logic text that I want to convert. It also imports `logicDB.py` which has the rules and conversions in it.

I'm sure there are better ways of doing almost all of this so I am excited to see what comes out of it. If you have any questions, let me know! My email is chefferk@tamu.edu

## Known problems
* Needs to be in *correct* form
  * No spaces in sentences (spaces are fine in first line)
    * TODO : leverage regex better to parse sentences and not have to remove spaces
  * Space between annotation set and annotation
    * TODO : this should be easy to split
  * Cannot have empty assumption set (e.g. axioms)
    * FIX: add a character place holder (e.g. 'x') and remove it later
    * TODO : find a fix for this
  * Top line should be: Premises (comma separated)	|-	Conclusion

```
P v Q, ~P v R |- Q v R
1       (1)   PvQ        A
2       (2)   ~PvR       A
1       (3)   ~Q->P      1 v->
2       (4)   P->R       2 v->
1,2     (5)   ~Q->R      3,4 HS
1,2     (6)   QvR        5 v->
```


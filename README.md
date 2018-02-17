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
* Cannot have spaces in sentences
  * FIX: delete spaces in sentences in text file prior to improt
* Need to have space between annotations and numbers
* Cannot have empy assumption set (e.g. axioms)
  * FIX: add a chracter place holder (e.g. 'x') and remove it later

```
Give the example
```

## Contributing

Please read [CONTRIBUTING.md](https://gist.github.com/PurpleBooth/b24679402957c63ec426) for details on our code of conduct, and the process for submitting pull requests to us.

## Authors

* **Billie Thompson** - *Initial work* - [PurpleBooth](https://github.com/PurpleBooth)

See also the list of [contributors](https://github.com/your/project/contributors) who participated in this project.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

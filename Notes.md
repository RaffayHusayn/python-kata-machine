## How imports work:
There are two type of imports 
- Absolute Imports (Only looks for module in the list of paths in the sys.path list)
- Relative Imports (can only work when running the program as a module using python -m)

## Absolute Imports:

Absolute imports requires the full path of your module starting from the root of the package that exists in the sys.path list
so for example:

```
python-kata-machine         (package)
├── __init__.py             [needed to make it a package]
├── src
│   ├── BinarySearch.py     (module)
│   ├── __init__.py         [needed to make it a package]
└── tests
    ├── BinarySearch.py     (module)
    └── __init__.py         [needed to make it a package]
```


In this case If I wanted to import a function from the module BinarySearch I would have to do the following:
    1. import the full path of the module: 
        `from src.BinarySearch import binary_search`
    2. To make the import work I have to make sure that python knows that It has to look into src directory. Because by default it will look into the current directory that the file would be in. In this case that would be tests/ . But to make sure that python can also look into src directory we have to do the following:
```python
import sys 
sys.path.append(`/Users/raffay/python-kata-machine`)
```


# Relative Imports:
This is kinda strange because it confuses me but I think I have a good way to explain it now.

First thing you need to know is relative imports only work when running as a module not as a script. Because a file is run as a module it's name is `package.subpackage.{module-name}` but when it is run as a stand alone script it's name is `__main__`.

To run a file as a module use:
`python -m package.module`

To run a file as a script use:
`python filename.py`

#### Examples for Relative Imports (And Errors):
1. You have a structure like:
```
python-kata-machine         (package)
├── __init__.py             [needed to make it a package]
├── src
│   ├── BinarySearch.py     (module)
│   ├── __init__.py         [needed to make it a package]
└── tests
    ├── BinarySearch.py     (module)
    └── __init__.py         [needed to make it a package]
```
And in the `tests/BinarySearch` module I try to import something from `src/BinarySearch` like this:

```python
# tests/BinarySearch.py
from ..src.BinarySearch import binary_search
```  

And I try to run from the root of the package like:
```bash
# bash script
~/algo/(python-kata-machine)  python -m tests.BinarySearch
```

This will throw an error saying:
`ImportError: attempted relative import beyond top-level package`

This is because `..src.BinarySearch` in the import means going up two levels.
```
python-kata-machine         (.. Takes you here) [..]
├── __init__.py             
├── src
│   ├── BinarySearch.py
│   ├── __init__.py
└── tests           (. Keeps you in the same Directory) [.]
    ├── BinarySearch.py (You are HERE) 
    └── __init__.py 
```
so to make this work, we can go back one directory which is essentially outside of our package and run this command
```bash
~/(algo)  python -m python-kata-machine.tests.BinarySearch
```
### Tip for Relative Imports
1. You basically want to make sure that the number of dots in the relative import statement at the start are same or less than the depth of the package, sub package.

- eg: `from ..src.BinarySearch` has 2 dots so the depth of where it is being called should have atleast 2 dots like:
`python -m python-kata-machine.<dot#1>tests.<dot#2>BinarySearch`

But obviously you can atmost go one level out of the package so 
```bash
# this is the most depth you can have
python -m <package-root>.<sub-package-director>...
```


# PIP Module Scanner
[![Build Status](https://travis-ci.org/Paradoxis/PIP-Module-Scanner.svg?branch=master)](https://travis-ci.org/Paradoxis/PIP-Module-Scanner)
[![Code Coverage](https://codecov.io/gh/Paradoxis/PIP-Module-Scanner/branch/master/graph/badge.svg)](https://codecov.io/gh/Paradoxis/PIP-Module-Scanner)

Scans your Python project for all installed third party pip libraries that are used and generates a requirements.txt based output.

## Installation
Installing the scanner is easy, either clone the repository and run the script or install it via pip like so:

```shell
$ pip install pip-module-scanner
```

## Usage
Using the scanner is incredibly simple. Open a terminal and navigate to your project folder, run the script and watch magic happen before your eyes. Example:

```shell
$ cd ~/projects/my-awesome-project/
$ pip-module-scanner
foo==1.0.0
bar==2.1.0
baz==0.0.1
```    

### Specifying a custom path
You can specify a custom path in which you want to run the script with the `-p` or `--path` argument. Example:

```shell
$ pip-module-scanner --path ~/projects/my-awesome-project/
foo==1.0.0 
bar==2.1.0
baz==0.0.1
```

### Writing the output to a file
You can write the output of the script to a file by using the `-o` or `--out` argument. Example:

```shell
$ cd ~/projects/my-awesome-project/
$ pip-module-scanner -o requirements.txt
$ cat requirements.txt
foo==1.0.0
bar==2.1.0
baz==0.0.1
```

## Integrating the code in your project
You can easily integrate the scanner code in your own project so you can get the output of the scanner yourself or modify the class to suit your own needs. To do this, you can use it like so:

```python
from pip_module_scanner.scanner import Scanner

scanner = Scanner()
scanner.run()

# do whatever you want with the results here
# example:
for lib in scanner.libraries_found:
    print ("Found module %s at version %s" % (lib.key, lib.version))
```

Specifying a path would work like so, make sure to also import the `ScannerException` as it will check if the path you specified is actually a real path:

```python
from pip_module_scanner.scanner import Scanner, ScannerException

try:
   scanner = Scanner(path="~/projects/my-awesome-project/")
   scanner.run()
   
   # do whatever you want with the results here
   # example:
   for lib in scanner.libraries_found:
       print ("Found module %s at version %s" % (lib.key, lib.version))
   
except ScannerException as e:
    print("Error: %s" % str(e))
```

For the one-liner junkies out there (like me) you can also get all libraries with this nifty little one-liner (I'm so considerate)

```python
from pip_module_scanner.scanner import Scanner

libs = Scanner().run().libraries_found # Isn't it beautiful?
```

## Class definitions

### pip_module_scanner.scanner.Scanner([string path [, string output]])

| Method              | Argument | Type    | Required | Description                                          |
| ------------------- | -------- | ------- | -------- | ---------------------------------------------------- |
| \_\_init\_\_        | path     | string  | no       | Directory to recursively scan through, defaults to current working directory. |
|                     | output   | string  | no       | Output path to write the resutlts from `output()` to |
| run                 |          |         |          | Runs the scan, output will be stored in `libraries_found` |
| output              |          |         |          | Writes the output to the console or a path specified in the constructor |


| Property            | Type                                                | Description  |
| ------------------- | --------------------------------------------------- | ------------ |
| libraries_found     | list<pip._vendor.pkg_resources.EggInfoDistribution> | List of all found pip libraries in your project, result from `Scanner.run()`.


## License
MIT License

Copyright (c) 2016 Luke Paris

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

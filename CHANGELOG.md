
# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [1.0.1] - 2020-02-07

 ### Added
 - added building of wheels and uploading them to the pypi server

 ### Removed
 - don't build and upload sdist package anymore, because a wheel is also a source package
   and is better because it contains the requirements in metadata of the package,
   which one can fetch from the pypi server before downloading a package. 
 

## [1.0.0] - 2020-02-06

### ADDED
- First production release which can be use with the thonny-ev3dev plugin in the Thonny IDE version 3. 
- Added README with documentation. 

### CHANGED
- created new project  https://github.com/ev3dev-python-tools/ev3devrpyc
  by splitting of ev3devrpyc python library from the thonny-ev3dev project at its
  old website https://github.com/harcokuppens/thonny-ev3dev/
- for CHANGELOG before 1.0.0 look at the old website at https://github.com/harcokuppens/thonny-ev3dev/


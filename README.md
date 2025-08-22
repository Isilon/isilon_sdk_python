# Isilon Software Development Kit (isi-sdk)
Language bindings for the OneFS API and tools for building them

This repository is part of the Isilon SDK.  It includes language bindings for easier programmatic access to the OneFS API for cluster configuration (on your cluster this is the REST API made up of all the URIs underneath `https://[cluster]:8080/platform/*`, also called the "Platform API" or "PAPI"). The SDK also includes language bindings for the OneFS RAN (i.e. RESTful Access to Namespace) interface, which provides access to the OneFS filesystem namespace.

You can download the language bindings for Python from the "releases" page of this repo (the link is on the main "code" tab on the bar of links just below the project description). If you just want to access PAPI more easily from your Python programs, these language bindings may be all you need, and you can follow the instructions and example below to get started.

This repository also includes tools to build PAPI bindings yourself for a large range of other programming languages. For more info see the [readme.dev.md](readme.dev.md) file in this directory.

### Installing the pre-built Python PAPI bindings

#### Prerequisites

* [Python](https://www.python.org/downloads/) 2.7 or later
* [pip](https://pip.pypa.io/en/stable/installing/)

Installation
------------

``pip install isilon_sdk``

Example program
---------------

Please select the subpackage as applicable to the OneFS version of your
cluster by referring to the below table:


OneFS Version and respective package names are as:

============= ==================
OneFS Release Package Name      
9.5.0.0       isilon_sdk.v9_5_0 
9.6.0.0       isilon_sdk.v9_6_0 
9.7.0.0       isilon_sdk.v9_7_0 
9.8.0.0       isilon_sdk.v9_8_0 
9.9.0.0       isilon_sdk.v9_9_0 
9.10.0.0      isilon_sdk.v9_10_0
9.11.0.0      isilon_sdk.v9_11_0
9.12.0.0      isilon_sdk.v9_12_0
============= ==================

### Basic Usage

See the generated packages on PyPI for example code:

[isilon\_sdk](https://pypi.org/project/isilon-sdk)

### Bindings Documentation

The most up-to-date documentation for the language bindings is included in the root directory of your downloaded release package (or of your own generated bindings if you've generated your own using the instructions at [readme.dev.md](readme.dev.md)). It is a set of markdown files starting with the README.md in the root directory of the package. Otherwise, the documentation for the Python language bindings can be found in the [isilon_sdk_python](https://github.com/Isilon/isilon_sdk_python) repository where the branch names are associated with the OneFS release that the bindings were built against.

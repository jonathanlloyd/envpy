# envpy

## Overview
Python library for loading config from environment variables.

## Getting Started

### Installation
To install use pip:
```
$> pip install envpy
```
    
Requirements before installation:
 * python3
 * pip3

### Usage
```
"""Basic usage script for envpy"""

import envpy

CONFIG = envpy.get_config({
    # This will raise an error if it cannot be found in the environment
    # because no default has been set.
    'SECRET_KEY': envpy.Schema(value_type=str),
    # This has a default value and as such won't raise an error if it cannot
    # be found in the environment. However, the value type is set to 'int'
    # which means that an error will be raised if a value is present in the
    # environment but cannot be parsed as an integer.
    'NUM_WORKERS': envpy.Schema(value_type=int, default=4),
})

if __name__ == '__main__':
    print('Secret Key:', config['SECRET_KEY'])
    print('Number of workers:', config['NUM_WORKERS'])
```

## Value Types

**str**

No parsing is applied and the string is returned directly from the environment.

**int**

The value will be parsed as an integer. Must match: ^[0-9]+$.

**float**

The value will be parsed as a float. Must match: ^[0-9]+\.[0-9]+$.

**bool**

The value will be parsed as a boolean. Must be one of the following:
 - "1" (True)
 - "0" (False)
 - "true" (True, case insensitive)
 - "false" (False, case insensitive)


## Development

### Installation
This project makes use of virtual environments to provision your development environment. Once the following requirements have been met further installation is managed automatically by the Makefile.

Requirements before provisioning:
 * python3
 * pip3
 * virtualenv
 * make

### Usage
The following commands will create a virtual environment (if not already present) for the application and will install the necessary dependencies there before running the requested command.

Run the package:
```
$> make
```
Run the unit tests:
```
$> make test
```
Run the linter: 
```
$> make lint
```

Rebuild your virtual environment:
```
$> make rebuild_venv
```

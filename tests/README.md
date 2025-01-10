# Run the test suites

There are multiple tests available to check the compliance of openc2lib with the Language Specification, concerning data types, serialization, and message exchange.

## Data types
A first set of tests concerns the correct instantiation of data, including both data, targets, args, artifacts, and commands.
To run these tests, enter the ```types``` folder and run:
```
# pytest
```

## Encoding/Deconding messages
This is a more complete set of tests concerning the correct decoding and encoding of json messages taken from a third party site.
To run the test, enter the ```json``` folder and run:
```
# pytest test_commands.py
# pytest test_response.py
```
To perform these tests, a Consumer must run and answer to requests from the Producer, which is emulated in the tests. The Consumer will likely use dumb actuators because the commands usually does not make sense for a real function.

# Runnig the test suites

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

## Performance analysis 
The following procedure describes how to collect performance measures when running both the Producer and the Consumer on localhost. This makes perfect sense for this kind of analysis, to avoid counting the random effects of network traversal.

First, remove existing log files, if any.
```
# rm -rf controller.log server.log
```
Run the server:
```
# ../../examples/server.py
```

Then run the simulation (change the number of trials in the Producer according to your needs):
```
# ./controller.py
```

Collect log file from the server
```
# cp ../../examples/server.log .
```

Collect statistics:
```
# awk -f server.awk server.log  | gawk -f stat-server.awk > server.txt
# awk -f controller.awk controller.log  | gawk -f stat-controller.awk > controller.txt
```

For network traces:
- Use wireshark to capture, display filter "HTTP", View -> Time from previous displayed.
- Export packet dissection as txt.
- Run the following awk filter:
  ```
  # grep "HTTP/1.1"  nettrace.txt| grep -v "POST" | awk 'BEGIN{ tot=0; count=0; min=99999; max=0} { tot+=$2; count++; if( $2 < min ) min=$2; if (max < $2) max=$2;} END{printf("Tot\tAvg\tMin\tMax\n"); printf("%s\t%s\t%s\t%s\n",count, tot/count, min, max);}'
  ```
  

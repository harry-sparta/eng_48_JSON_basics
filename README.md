# JSON Basics

## Definition of JSON
JavaScript Object Notation
--> is usually a **Dictionary**

However, confusingly an object in JavaScript is the Data Type for both lists (arrays) and dictionaries (hashes.

## Create a JSON file

### json.dumps(obj) --> string json

### json.dump(obj, file) --> writes json in file

## Make POST request with JSON
you need:
- path
- json
- headers

## Task

Make a small program that requests 3 postcodes and returns something like:
````
> 1 - Postcode: xyzpto with nhs location at: xyz
> 2 - Postcode: xyzpto2 with nhs location at: xyz
> 3 - (...)
````

JSON dumps and dump
To convert dictionary into strings that could be sent off faster.
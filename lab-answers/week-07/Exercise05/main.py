"""
Write a Python 3 function named mergeJSONObjects() that accepts two JSON string as arguments and performs the following action:

The function should merge the two JSON strings into a single JSON string. 
If a key exists in both JSONs, the value from the second JSON should overwrite the value from the first.

Assume that the function will always be called with correct arguments. Please refer to the example table for input and output details.
"""

import json

def mergeJSONObjects(json_str1, json_str2):
    obj1 = json.loads(json_str1)
    obj2 = json.loads(json_str2)
    
    merge = {**obj1, **obj2}
    
    return merge

print(mergeJSONObjects('{"a": 1, "b": 2}', '{"c": 3, "d": 4}'))	
print(mergeJSONObjects('{"a": 1, "b": 2}', '{"b": 100, "c": 3}'))	
print(mergeJSONObjects('{"user": {"name": "Alice", "age": 25}, "active": true}', '{"user": {"name": "Bob"}, "active": false}'))
print(mergeJSONObjects('{}', '{"x": 10}'))	
print(mergeJSONObjects('{"nums": [1, 2, 3]}', '{"nums": [4, 5]}'))	
print(mergeJSONObjects('{"value": 42}', '{"value": "forty-two"}'))
print(mergeJSONObjects('{"config": {"theme": "light", "settings": {"volume": 50}}}', '{"config": {"settings": {"volume": 100}}}'))
print(mergeJSONObjects('{"a": 1, "b": {"c": 2, "d": 3}}', '{"b": 42, "e": [1, 2, 3]}'))
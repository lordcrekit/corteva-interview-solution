# corteva-interview-solution

Program takes csv file(s) and converts them to standardized json format in a single file.

# Usage
```bash
# Run program
python3 main.py --input [input file(s)] --output [output file]

# Help
python3 main.py --help

# Tests
python3 -m unittest discover
```


# Format
## Input schema
```csv
title,title
FIRST LAST,EMAIL
FIRST LAST,EMAIL
FIRST LAST,EMAIL
```

## Output schema
```json
{
   "user_list_size": "integer, length of the user _list",
   "user_list": [
      {
         "list_id": "integer, sequence number for this user in the file starting at 1",
         "first name": "string, first name of this user",
         "last name": "string, last name of this user",
         "email": "string, email address of this user"
      }
   ]
}
```

## Output example
```json
{
   "user_list_size": 3,
   "user_list": [
      {
         "list_id": 1,
         "first name": "John",
         "last name": "Doe",
         "email": "john.doe@gmail.com"
      },
      {
         "list_id": 2,
         "first name": "Jane",
         "last name": "Smith",
         "email": "jane.smith@yahoo.com"
      },
      {
         "list_id": 3,
         "first name": "Peter",
         "last name": "Drucker",
         "email": "the_pd@gmail.com"
      }
   ]
}
```

# Extension
Implement the `_miss` function.

# Auto Generate and Insert data into MongoDB

> This code only use for research purpose.  Any problem, please report to cuocchie@gmail.com.

## General Idea
- Get an insight about the performance difference between SQL (MySQL) and No-SQL (MongoDB).
- Create a simple schema which has a table/collection contain 1 mil records/documents.
- This code only focus on auto generate data and optimize insertion into MongoDB database.

## About Schema
### MySQL
#### Students
|student_id | name | class id| grade_id |
|------------|--------|------|------|
|19020000  |"Nguyễn Thế Sơn"| 1| 1|
|19020000  |"Hồ Tịnh Lâm"| 1| 2|
#### Grade
|grade_id|lang|math|
|------|------|------|
|1|6|10|
|2|5|8|
#### Classes
|class_id|name|is_specialized|
|------|------|------|
|1|K64Y|True|
|2|K62E|False|

### MongoDB
#### Students
```
{
    "student_id": 19000000,
    "name": "Nguyễn Thế Sơn",
    "class_id": {
        "$oid": "6197cc03ff22ce22bb58c37d"
    },
    "grades": {
        "math": 7,
        "lang": 3
    }
}
```

#### Classes
```
{
    "name": "K60E",
    "is_specialized": true
}
```

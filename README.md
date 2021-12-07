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

### Connection

All the connection use database driver, [sqlconnector](https://www.mysql.com/products/connector/) in MySQL and [mongoengine](http://mongoengine.org/) in MongoDB.

### Data generation

`class id`, `grade_id` was created increasingly from 0, except `student id` starts from '19000000`

`Name` was created by combining `first name` and `last name`.
`first name` was randomly choosen from [name_list.txt](https://github.com/cuocchie/MongoDB_proj/blob/ff5a592f1b2af35c0b9d83a296eb86a57e1bcb59/MongoDB/last_name_list.txt). There are 2036 total first names.
`last name` was randomly choosen from [last_name_list.txt](https://github.com/cuocchie/MongoDB_proj/blob/ff5a592f1b2af35c0b9d83a296eb86a57e1bcb59/MongoDB/last_name_list.txt). Lastname was picked from the (top 10 popular Vietnamese last name)[https://vi.wikipedia.org/wiki/H%E1%BB%8D_ng%C6%B0%E1%BB%9Di_Vi%E1%BB%87t_Nam#C%C3%A1c_h%E1%BB%8D_ph%E1%BB%95_bi%E1%BA%BFn_c%E1%BB%A7a_ng%C6%B0%E1%BB%9Di_Vi%E1%BB%87t].

`math` and `lang` in grades was randomly generate used [`randint()`](https://docs.python.org/3/library/random.html?highlight=randint#random.randint). The grades was created in range `(0, 10)`.

`class name` starts with `K` append to `60 + i%20` with i in range `(0, NUMBER_OF_CLASS)` and next is a random uppercase character.
`is_specialized` is `boolean` so random between two values `1` and `0`.

*Foreign Key* in `students`
**In MySQL**

- One student has one grade, `grade id` will be increased accordingly to `grade_id` in Grades.
- One class has many student, `class id` in student will be randomly pick from list of `class id`

**In MongoDB**

- `grades` will emmbed grade value in a student document.
- `class id` in student will be randomly pick from list of `class id`

### Insertion

#### MongoDB

1. Connect to MongoDB server using connection string.

    ```python
        client = MongoClient(DB_URI)
    ```

2. Create db instance

    ```python
        db = client.school_db
    ```

3. Create student Collection and classes Collection.

    ```python
        students = db.students
        classes = db.classes
    ```

4. Create `1000` classes then append into a class list.

5. Insert `1000` classes into `classes` document use bulk insert. Then get 1000 `class id` into a list.

    ```python
        class_id = classes.insert_many(
        class_list).inserted_ids
    ```

6. Read all the name from file, put first name and last name in two lis

7. Loops 100 times. Each loop will created `1,000,000` students. All `1,000,000` students will be bulk insert into student document.

#### MySQL

1. Connect to MySQL database server using connection string.

    ```python
        mydb_con = mysql.connector.connect(
            host="******",
            user="***",
            password="******",
            database="school_db")
    ```

2. Create all 3 three table and set foreign key.

    ```python
        cur.execute(
            f"CREATE TABLE classes (class_id INT AUTO_INCREMENT PRIMARY KEY NOT NULL, name VARCHAR(255), is_specialized BOOL)"
        )
        ...
        sql = "ALTER TABLE %s ADD FOREIGN KEY (%s) REFERENCES %s (%s)"
        students_grades = (Students.tablename, Students.grade_id, Grades.tablename, Grades.grade_id)
        ...
        cur.execute(sql % students_grades)
    ```

3. Create 1000 class, using execute many.

    ```python
        sql = "INSERT INTO classes (name, is_specialized) VALUES (%s, %s)"
        val_list = []
        ...
        cur.executemany(sql, val_list)
    ```

4. Read all the name from file, put first name and last name in two list

5. Loop 400 times. Each loop create 1 grade and 1 student which will append that `grade_id`.
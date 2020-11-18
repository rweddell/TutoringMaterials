# Database basics



## History
- Files used to be manually managed
- Data is now too large and moves too quickly for this to be possible
- Data is now stored in large file systems
- The files can be linked to each other using data that is represented in both sides of the link



## DataBase Management System (DBMS)
- An DBMS is a system that allows a user to interact with data in storage
- Secure connections in terms of data loss prevention as well as transactional security
- Data creation/deletion without needing to interact directly with files
    
    
    
## Components of DBMSs

### Databases
- A database is essentially a folder in a file system
- Databases allow tables to be compartmentalized based on use-case or relationships
- It also adds a level of security by adding a layer of access authentication for the underlying tables

### Tables
- A table is essentially a file in a file system
- They can be stored directly within the file system (DBMS), but should be created within a database
- Tables are the structure which actually stores the data

### Columns
- Columns are individual fields within a table

### Keys
- A unique column within a table that is used as the identifier for a particular row
    - Names
    - Locations
    - Dates or times
- Can also be a combination of columns for a row
    - Purchased item + date
    - Job Title + Company name
- Used to connect data in separate table

### Views
- Views are routines which behave much the same way as tables, but are not actual structures
- Views are a subset of information within one or more databases
    - Subsection of a table
    - Several talbes or parts of tables bundled together
    
### Schema
- The architecture of a DBMS
    - Database
    - Table/View
    - Columns/Keys

### UDFs
- User Defined Functions
- These are custom routines that can be created and scheduled to automatically process data
    
    
## Transactions
- A transaction is an interaction with data
    - Reading 
    - Writing
    - Deleting

    Consider this scenario:
    >    - Users A and B both work at a manufacturing firm
    >    - In their database is a table holding the total number of items sold in a given period
    >    - A needs to write a report that shows this number to present to management in a planning meeting
    >    - B needs to enter some last-minute entries
    >    - What happens if they both access the information at the same time
    
    
## Queries
- Statements made in SQL are called 'queries'
- The most typical query will begin with a 'select' clause
    - This is when a user is looking for information
    - They are 'selecting' information from storage for review


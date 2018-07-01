# Subby

---
## Design Document

1. **[Introduction](#1introduction)**  
  1.1. [Purpose](#11purpose)  
  1.2. [Intended Audience](#12intendedaudience)  
  ...more  
2. **[Major Features](#2majorfeatures)**  
  2.1. [Create Sublet Listings](#21createsubletlistings)  
  2.2. [Browse/Search Sublet Listings](#22browsesearchsubletlistings)  
  ... more  
3. **[Design Considerations](#3designconsiderations)**  
4. **[Development Policies](#developmentpolicies)**  
  4.1. [Technical Standards and Guidelines](#41technicalstandardsandguidelines)  
  4.1.1. [General Guidelines](#411generalguidelines)  
  4.1.2. [Technical Standards](#412technicalstandards)  
5. **[Project Testing](#5projecttesting)**  
  5.1. [Testing Strategies](#51testingstrategies)  
6. **[Project Architecture](#6projectarchitecture)**  
  6.1. [Class Diagram](#61classdiagram)  
  6.2. [Package Details](#61packagedetails)  
  6.2.1. [User Package](#621userpackage)  
  6.2.2. [Sublet Package](#622subletpackage)  
  6.2.3. [Rating Package](#623ratingpackage)  
  6.2.4. [Favorite Package](#624favoritepackage)  
  6.2.5. [Report Package](#625reportpackage)  
7. **[Data Dictionary](#7datadictionary)**  
8. **[Revision History](#8revisionhistory)**  

# 1. Introduction
## 1.1. Purpose
## 1.2. Intended Audience

# 2. Major Features
## 2.1. Create Sublet Listings
## 2.2. Browse/Search Sublet Listings

# 3. Design Considerations

# 4. Development Policies
## 4.1. Technical Standards and Guidelines
### 4.1.1. General Guidelines
* In general, problem-solving strategy and code formatting should follow the idiomatic approach of the language and tools used.

### 4.1.2. Technical Standards
* Code should be easily readable and as self-documenting as possible to enable ease of future maintenance.
  * Code should be DRY; functionality should be abstracted, rather than repeated, to avoid issues in maintenance.
* Methods that perform non-trivial operations should have a short comment with a description of their side-effects.
* Blocks within methods that are complex should have a short comment explaining their purpose.
* Frontend HTML and CSS must be in compliance with the established W3C standards.

## 4.2 Project Deployment
* The deployment process will support starting the application on virtual server instances on Heroku. However it could run on a server using any OS that supports Python 3, as this is the runtime that Subby will use.
* Depending on the deployment configuration, the hosting server will also need to support a local Postgres database; alternatively, a separate server with a networked Postgres instance must be provided and reachable by the application server.

# 5. Project Testing

# 6. Project Architecture
## 6.1. Class Diagram
## 6.2. Package Details
## 6.2.1 User Package
![UserPackage](https://i.imgur.com/zEhaUms.jpg)

### User Class
#### Methods
* Contructor (public)
    * User(options: map) - Class Constructor. Options parameter is a key-value object with the attributes of the desired User. Only non-null fields are enforced.
        * Options: (email: string, password: string, lastname: string, firstname: string, phonenumber: string)

* Getters (public)
    * get\_user\_id():int
    * get\_email():string
    * get\_created\_at():datetime
    * get\_updated\_at():datetime
    * get\_is\_admin():boolean
    * get\_last\_name():string
    * get\_first\_name():string
    * get\_phone\_number():string

* Setters (public)
    * set\_email(email: string)
    * set\_created\_at(date: datetime)
    * set\_updated\_at(date: datetime)
    * set\_is\_admin(is_admin: boolean)
    * set\_password\_from_plaintext(plain_password: string) - Generates hashed password and sets the salt attribute on the user.
    * set\_first\_name(firstname: string)
    * set\_last\_name(lastname: string)
    * set\_phone\_number(phonenumber: string)

* Helpers (public)
    * test\_password(password: string) - Tests the given plaintext password against the user's salted and hashed password.

* Helpers (private)
    * **Static:** hash_password(password: string) - Salts and hashes the given plaintext password.
    * validate\_password(password: string) - Ensure password meets specifications (e.x. 8 character minimum limit).
    * validate\_phone\_number(phonenumber: string) - Ensure that the phone number is of valid length and format.
    * validate\_email(email: string) - Validates the format of the given email.

* Relation Helpers (public)
    * save() - Runs the validation helpers, returning errors if present, and saves the User if it is valid.
    * reviews() - Returns an array of Reviews created by the User.
    * favorites() - Returns an array of Favorites created by the User.
    * sublets() - Returns an array of Sublets created by the User.
    * reports() - Returns and array of Reports created by the User.

## 6.2.2 Sublet Package
## 6.2.3 Rating Package
## 6.2.4 Favorite Package
## 6.2.5 Report Package

### Report Class
#### Methods
* Contructor (public)
    * Report(user_id: int, sublet_id: int, issue: string, description: string) – Class Constructor. All non-null fields are enforced except datetime frields, which are recorded by system automatically.

* Getters (public): only available for admins
    * get\_report\_id():int
    * get\_created\_at():datetime
    * get\_updated\_at():datetime
    * get\_issue():string
    * get\_user\_id():int
    * get\_description():string

* Setters (public): only available for admins
    * set_report_id(report_id: int)
    * set_created_at(date: datetime)
    * set_updated_at(date: dateime)
    * set_issue(issue: string)
    * set_description(description: string)
    * set_user_id(user_id: int)


* Helpers (private):
    * test\_description(description: string) – Tests the descriptions user has entered. Reject the report if the description is not valid. For example: a series of punctuations, Non english letters, a series of random letters.


* Relation Helpers (public):
    * save() - Saves the Report if no error is presented by the prviate helper methods.
    * users() - Returns an array of User who has been reported. Only available for admins.
    * sublets() - Returns an array of Sublets that has been reported. Only available for admins.

# 7. Data Dictionary

# 8. Revision History
## Version 1.0
* **Section 4**
  *  Alex Kirsopp [4.1] [2018-06-20]

* **Section 6**
  *  Alex Kirsopp [6.2.1] [2018-06-27]
  *  Xiaochao Luo [6.2.5] [2018-07-01]

* **Other**
    * Alex Kirsopp - Layout, initial outline, markdown, etc

# Subby

---
## Design Document

1. **[Introduction](#1introduction)**  
  1.1. [Purpose](#11purpose)  
  1.2. [Intended Audience](#12intendedaudience)  
  1.3. [Product Scope](#13productscope)  
  1.4. [Referencing Documents](#14referencingdocuments)  
2. **[Major Features](#2majorfeatures)**  
  2.1. [Create Sublet Listings](#21createsubletlistings)  
  2.2. [Browse/Search Sublet Listings](#22browsesearchsubletlistings)  
  ... more  
3. **[Design Considerations](#3designconsiderations)**  
  3.1. [Assumptions and Dependencies](#31assumptionsanddependencies)  
  3.2. [End-user Characteristics](#32endusercharacteristics)  
  3.3. [General Constraints](#33generalconstraints)  
  3.4. [Goals and Guidelines](#34goalsandguidelines)  
  3.5. [Development Methods](#35developmentmethods)  
4. **[Development Policies](#developmentpolicies)**  
  4.1. [Technical Standards and Guidelines](#41technicalstandardsandguidelines)  
  4.1.1. [General Guidelines](#411generalguidelines)  
  4.1.2. [Technical Standards](#412technicalstandards)  
  4.1.3. [Data Storage](#413datastorage)  
  4.1.4. [Data Security](#414datasecurity)  
  4.1.5. [Control Flow](#415controlflow)  
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
In the Design Phase we consider the behaviour of the system and detail its design.
Here, the software architecture is established, providing the framework of the various subsystems and the interaction between them. Building on the Analysis Phase, the Architecture Design introduces the corresponding interfaces of the predefined modules outlined in the previous phases. Additionally, this phase incorporates the Detailed Design which outlays the algorithms and data structures responsible for the operation of the product modules. 

## 1.1. Purpose
The Design Phase seeks to capture and document the specific data structures and workflows of the system in order to provide a detailed description of the project's design and automation. Once completed, the development team may proceed with a reliable forecast of the project’s time line and design for the Implementation Phase.  
 

## 1.2. Intended Audience
The intended audience for Subby includes students in the Waterloo region who are either looking to sublet a place or are looking to rent their place out for a specified amount of time. 

## 1.3. Product Scope
The scope of Subby is driven by the need for a “one-stop shop” for Waterloo sublets. This will be done by creating, advertising and maintaining a sing website dedicated for finding and selling sublets. Achieving this will simplify an individual’s search to find a place for the school year while also aiding in an individual’s search for a renter. The finished product will be simple to use and easy to navigate through its various filters.  

## 1.4. Referencing Documents
* [Requirements Documentation for Subby](https://rawgit.com/Kuresov/CP317-W2018-G3/master/documents/Subby-Requirements.md.html)
* [Analysis Documentation for Subby](https://rawgit.com/Kuresov/CP317-W2018-G3/master/documents/Subby-Analysis.md.html)

# 2. Major Features
## 2.1. Create Sublet Listings
* Registered users can create sublet listings
  * Users can add details, such as the location and a description, of the listing and choose to upload photos as well
  * Users can also add filters to their listing, enabling their listing to be included in more refined searches.
  
## 2.2. Browse/Search Sublet Listings
* Users can browse listings created by users
  * Browsing is not limited to registered users and listings are accessible to public users 
  * Users can browse listings using a list, or by manipulating an interactive map
* Search functions enable public and registered users to specify postings by location or address
  * Filters can be applied by users to refine searches using criteria such as, price range, size, number of rooms available, and duration of stay
  * Users can sort search results using price, date, and ratings

## 2.3. Contact Sublet Owners
* Users can contact sublet owners through the subby platform
  

# 3. Design Considerations
## 3.1. Assumptions and Dependencies
* Users will have basic knowledge of how to use a computer, more specifically webiste navigation 
* Users will have a university or college email to register
* Google Maps API will be available for use

## 3.2. End-user Characteristics
* The ability for administrators to fix, update and maintain the website
* Users have the ability to filter their searches based on their needs
* Users are able to view available sublets on a map 
* Users can post their rooms for rent in addition to posting “wanted” ads 
* Users can rate other users based on their experiences
* Users are able to place a bid on properties they are interested in 

## 3.3. General Constraints
* Google Maps API Budget 
  * Daily free limit of 25,000 map loads 
	* $0.50 USD per 1,000 map loads over the daily free limit up to a maximum of 100,000 map loads
  * Subby administrators are trying to make the site as cost-effective as possible which will limit the site to a daily limit of 25,000 map loads 

## 3.4. Goals and Guidelines
* Comments will be used when coding
* All features in the design and analysis documents will be adhered to
* Any feature changes made to Subby will be documented
* All work done for the project will have SQA performed on them 

## 3.5. Development Methods
* Utilizing UML to organize and guide the code
* Performing SQA throughout the project to ensure correctness and thoroughness

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

### 4.1.3. Data Storage  
*	All objects will be organized into logical groups within one or more schemas in the database to maintain data organization and manageability. 
*	Objects within one schema should be accessible within another schema, assuming access is permitted. 
*	Permit flexible and robust implementation of user defined objects, such as functions, data types, indexes and operators
*	Support a variety of data types, such as:
    * Boolean
    * Binary
    * Text (varchar, chart, text)
    * Date/Time
    * Enum
    * Array
    * User defined data type
    
    
### 4.1.4. Data Security 
*	Database must maintain the security and integrity of data housed with in it on several levels:
    * Access Control: 
        * Postgres ensures all files stored are protected from reading by any accounts other than the Admin.
        * Access is granted or revoked on any object all the way down the column level.
        * User authentication is performed by backend server and postmaster, who sanction permissions to users requesting access to data.
        * Each Postgres user account is assigned a username and is further secured with a password.
        * Write access is limited to the Admin by default.
    * Data Integrity:
        * Foreign Keys
        * Primary Keys
        * Column constraints
        * Row Checks
        * UNIQUE, NOT NULL
        * Explicit Locks, Advisory Locks 
    * Data Recovery: 
        * Online backup
        * Point-in-time recovery using write-ahead logging 
        * Tablespaces
    * Concurrency Control:
        * Concurrency is managed through multi-version concurrency control (MVCC) and immunity to dirty reads.
        * Ensures each transaction is not visible to other transactions until committed.
        * Uphold ACID principles:
              * Three levels of transaction isolation are offered: read committed, repeatable read and serializable.
      
### 4.1.5. Control Flow 
*	Data will transmit between client and PostgreSQL database. Client interacts with the PostgreSQL database using PHP Data Objects (PDO) API. It allows performing the common database operations in PHP such as creating new tables, inserting data, updating data, querying data, deleting data and so on. Once the connection is established successfully, client will directly send qury to database and database will respond corresponding answers to client. 


## 4.2 Project Deployment
* The deployment process will support starting the application on virtual server instances on Heroku. However it could run on a server using any OS that supports Python 3, as this is the runtime that Subby will use.
* Depending on the deployment configuration, the hosting server will also need to support a local Postgres database; alternatively, a separate server with a networked Postgres instance must be provided and reachable by the application server.

# 5. Project Testing

# 6. Project Architecture
## 6.1. Class Diagram
![DesignClassDiagram](https://i.imgur.com/ODITqTs.jpg)

## 6.2. Package Details
As discussed in the Analysis Phase, the system consists of five packages: User Package, Sublet Package, Rating Package, Favourite Package, and Report Package. Within each package diagram, we list the relevant entity objects and their corresponding methods. Additionally, each package diagram includes the control objects responsible for realizing the major use cases representing the interactions between external actors and the system. 


## 6.2.1 User Package
![UserPackage](https://i.imgur.com/zEhaUms.jpg)

### User Class
#### Methods
* Constructor (public)
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
    * reports() - Returns an array of Reports created by the User.

## 6.2.2 Sublet Package
![SubbySubletPackage](https://i.imgur.com/16Ab2Kx.jpg)
### Sublet Class
#### Methods
* Constructor (public) 
	* Sublet(sublet_title: string, duration: int, price_per_month: double, location: string, description: string) – Class Constructor. All non-null fields are enforced except for datetime fields, which are automatically recorded by the system. 


* Getters (public)
    * get\_sublet_id(): int
    * get\_is_sold(): boolean
    * get\_sublet_title: string
    * get\_duration():int
    * get\_price_per_month(): double
    * get\_location: string
    * get\_description(): string
    * get\_created_at(): datetime 
    * get\_updated_at():datetime
    * get\_owner_id(): int
* Setters (public)
    * set\_sublet_title(title: string
    * set\_is_sold(status: boolean) 
    * set\_duration(duration: int)
    * set\_price_per_month(price: double)
    * set\_location(location: string)
    * set\_description(desc: string)
    * set\_created_at(date: datetime)
    * set\_updated_at(date: datetime)
    * set\_owner_id(user_id: int)

* Relation Helpers (public) 
    * save() – Commits the Sublet to the database, assuming Sublet is correctly initiated 
    * reviews() - Returns an array of Reviews concerning the Sublet 

## 6.2.3 Rating Package

![SubbyRatingPackage](https://i.imgur.com/szf85fl.png)
### Rating Class

### Methods
  * Constructor (public)
    * Rating(rating: int, comment : string, user_id: int, reviewed_user_id:int) - Constructes a Rating
    
  * Getters (public)
    *  get_comment():string - Returns the text description tied to a rating
    *  get_reviewed_user_id():int - Returns the ID of the user being rated
    *  get_user_id():int - Returns the ID of the user who is rating another user
    *  get_created_at():datetime - Returns time data for time of class creation
    *  get_updated_at():datetime - Returns time data for time of last update to class
  
  * Setters (public)
    *  set_rating(rating: tinyint) - Updates the rating review number
    *  set_comment(comment: string) - Updates the comment for the review
    *  set_reviewed_user_id(reviewed_user_id: int) - Updates the reviewed user ID
    *  set_user_id(user_id: int) - Updates the reviewing user ID
    *  set_created_at(date: datetime) - Updates created_at
    *  set_updated_at(date: datetime) - Updates updated_at
    
  * Helpers (private)
    *  validate_rating(rating: tinyint) - Ensures that the rating is valid (i.e A value that is held in ALLOWED_REVIEW_VALS)
    
  * Relation Helpers (public):
    * save() - Saves and persistes the Rating
    * users() - Returns an array of User that have been rated.
    * sublet() - Returns an array of Sublets that is held by the rated user.
    
## 6.2.4 Favorite Package

![SubbyFavouriteDiagram](https://i.imgur.com/3X5iN2c.png)
### Favourite Class
  *  **FavouritesLister:** Gathers and returns all favourites for sublet listings display purposes
  *  **FavouritesManager:** Creates or destroys favourites from the database
### Methods
  * Constructor (public)
    *  Favourite(user_id: int, sublet_id: int) - Constructes Favourite
    
  * Getters (public)
    *  get_favourite_id():int - Returns favourite ID
    *  get_sublet_id():int - Returns the favourited sublet ID
    *  get_user_id():int - Returns user ID the favourite is tied to
    *  get_created_at():datetime - Returns time data for time of class creation
    *  get_updated_at():datetime - Returns time data for time of last update to class
  
  * Setters (public)
    *  set_created_at(date: datetime) - Updates created_at
    *  set_updated_at(date: datetime) - Updates updated_at
    
  * Relation Helpers (public):
    * save() - Saves and persistes Favourite
    
## 6.2.5 Report Package
![UserPackage](https://i.imgur.com/cqmxUjY.png)

### Report Class
#### Methods
* Constructor (public)
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
![DataDictionary](https://i.imgur.com/frsaeyW.png)


# 8. Revision History
## Version 1.0
* **Section 1**
  * Sarah Younes [1.0 - 1.1] [2018-07-01]
  * Sandra Sung [1.2 - 1.4] [2018-07-03]

* **Section 2**
  * Jingchi Chen [2.1 - 2.3] [2018-07-04]
  
* **Section 3**
  * Sandra Sung [3.1 - 3.5] [2018-07-03]
  
* **Section 4**
  *  Alex Kirsopp [4.1] [2018-06-20]
   * Sarah Younes [4.1.2 - 4.1.4] [2018-07-02]

* **Section 6**
  *  Alex Kirsopp [6.2.1] [2018-06-27]
  *  Xiaochao Luo [6.2.5] [2018-07-01]
  * Sarah Younes [6.1] [2018-07-02]

* **Other**
    * Alex Kirsopp - Layout, initial outline, markdown, etc

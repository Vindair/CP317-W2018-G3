# Subby

---
## Design Document

1. **[Introduction](#1introduction)**  
  1.1. [Purpose](#11purpose)  
  1.2. [Intended Audience](#12intendedaudience)  
  1.3. [Product Scope](#13productscope)  
  1.4. [Referencing Documents](#14referencingdocuments)  
2. **[Major Features](#2majorfeatures)**  
  2.1. [Browse/Search Sublet Listings](#21browsesearchsubletlistings)  
  2.2. [Create Sublet Listings](#22createsubletlistings)  
  2.3. [Contact Sublet Owner](#23contactsubletowner)  
  2.4. [Create/Edit User Account](#24createedituseraccount)  
  2.5. [Add/Remove Favourite Sublet Listings](#25addremovefavouritesubletlistings)  
  2.6. [Edit/Delete Posted Sublet Listings](#26editdeletepostedsubletlistings)  
  2.7. [Submit Reports](#27submitreports)  
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
  4.1.4. [Security and Privacy Considerations](#414securityandprivacyconsiderations)  
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
The Design Phase seeks to capture and document the specific data structures and workflows of the system in order to provide a detailed description of the project's design and automation. Once completed, the development team may proceed with a reliable forecast of the project's time line and design for the Implementation Phase.


## 1.2. Intended Audience
The intended audience for Subby includes students in the Waterloo region who are either looking to sublet a place or are looking to rent their place out for a specified amount of time.

## 1.3. Product Scope
The scope of Subby is driven by the need for a "one-stop shop" for Waterloo sublets. This will be done by creating, advertising and maintaining a sing website dedicated for finding and selling sublets. Achieving this will simplify an individual's search to find a place for the school year while also aiding in an individual's search for a renter. The finished product will be simple to use and easy to navigate through its various filters.

## 1.4. Referencing Documents
* [Requirements Documentation for Subby](https://rawgit.com/Kuresov/CP317-W2018-G3/master/documents/Subby-Requirements.md.html)
* [Analysis Documentation for Subby](https://rawgit.com/Kuresov/CP317-W2018-G3/master/documents/Subby-Analysis.md.html)

# 2. Major Features
## 2.1.  Browse/Search Sublet Listings
* Users can browse listings created by users.
  * Browsing is not limited to registered users and listings are accessible to public users.
  * Users can browse listings using a list, or by manipulating an interactive map.
* Search functions enable public and registered users to specify postings by location or address.
  * Filters can be applied by users to refine searches using criteria such as, price range, size, number of rooms available, and duration of stay.
  * Users can sort search results using price, date, and ratings.

## 2.2. Create Sublet Listings
* Registered users can create sublet listings.
  * Users can add details, such as the location and a description, of the listing and choose to upload photos as well.
  * Users can also add filters to their listing, enabling their listing to be included in more refined searches.

## 2.3. Contact Sublet Owners
* Users can contact sublet owners through the subby platform.
  * An e-mail will be sent to the sublet owner's registered e-mail address and will include the attached message and the e-mail address with which the user registered.
  * The sublet owner will then be able to contact the user directly.

## 2.4. Create/Edit User Account
* Users are able to create an account using a verified school e-mail address.
  * Users are able to edit their preferences and change their password.
  * Users will also have a profile containing basic information about them, such as their name and school.

## 2.5. Add/Remove Favourite Sublet Listings
* Users can organize and manage a list of their favourite sublet listings.
  * Users are able to add sublet listings to their favourites as they are browsing.
  * Users can later go to their favourite listings and remove any listings they no longer want to include.

## 2.6. Edit/Delete Posted Sublet Listings
* Users are able to modify any sublet listings that they post.
  * Users are able to change any details, filter options or photos they included in their listing.
  * Users are also able to delete their listings at any time they desire.

## 2.7. Submit Reports
* Users are able to issue reports concerning any violations of the terms and conditions policy and privacy policy. (Attach link to policies).
  * Reports will be reviewed by administrators and the appropriate punishment will be carried out.

# 3. Design Considerations
## 3.1. Assumptions and Dependencies
* Users will have basic knowledge of how to use a computer, more specifically webiste navigation
* Users will have a university or college email to register
* Google Maps API will be available for use

## 3.2. End-user Characteristics
* The ability for administrators to fix, update and maintain the website
* Users have the ability to filter their searches based on their needs
* Users are able to view available sublets on a map
* Users can post their rooms for rent in addition to posting "wanted" ads
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
* Frontend HTML and CSS must be in compliance with the established [W3C standards](https://www.w3.org/standards/).
* Browser Compatibility:
  * Bootstrap front-end framework will be used to ease cross-browser compatibility
  * A CSS reset stylesheet will be used to ensure behavior consistency between browsers 
  * Mac OS X, Linux and Windows users should be able to display the website with full functionality in the following browsers:
  	* internet Explorer 8.0 and 9.0 (Windows)
	* Safari (mac)
	* Firefox (Windows, Mac, Linux)
	* Chrome (Windows, Mac, Linux)


### 4.1.3. Data Storage
*	All objects will be organized into logical groups within one or more schemas in the database to maintain data organization and manageability.
*	Objects within one schema should be accessible within another schema, assuming access is permitted.
*	Permit flexible and robust implementation of user defined objects, such as functions, data types, indexes and operators



### 4.1.4. Security and Privacy Considerations
* Privacy Settings.
  * Dual-Mode privacy setting for User account data:
    * Private:
      * By default, User’s phone number, email address, and name will be exclusively accessible to the User
    * Public:
      * By default, a User’s username, published listings and pictures and profile description will be shared with all Users and
	Visitors.
* User Authentication.
  * Subby will use single sign-on to authenticate Users;
  * Usernames must be unique and can contain letters (A-Z), numbers (0-9), dashes (-), underscores (_), apostrophes ('), and periods (.);
  * Passwords can contain any combination of printable ASCII characters and must contain a minimum of 8 characters comprised of at least       one number and one special character  (e.g. !, @, #, $, etc.).
  
   * Passwords will be automatically salted to further safeguard passwords before they are stored in the database.
* User Access and Permissions.
   * Based on the functional requirements of Users and on security considerations, Subby will offer three permission levels:
      * Visitor – View-Only:
        * search and view listings
      * User – Design:
        * view, add, update and delete authored listings
        * search, view, report, flag and respond to the listings of others
     * Admin – Full-Access:
       * add, modify, and delete User listings
       * freeze and terminate User accounts
       * view and delete User profile information
       * review and respond to reports and flagged User listings and accounts
   * Below, Table A summarizes the aforementioned User Access Controls

     **Table A**
    ![permissionsSummary](https://i.imgur.com/OisjZIs.png)


   * For more details on User functionalities and permissions, refer to **[Major Features](#2majorfeatures)**
* Subby’s Privacy Policy (unofficial):
  * Subby will not share data with any third party entities, including marketing organizations
  * Subby will not send unsolicited marketing material and advertisements
  * Subby will collect and store all User provided information:
     * Account Information: Information requested during the In the Sign Up stage such as, user’s name, username, date of birth and  email
    address.
    * Profile Information: A User’s profile description, phone number, profile picture and other profile information.
    * Listing Information: A listing’s address, price, features, pictures, and reviews.
    * Communication Forms: Information sent by a sublet seeker to a leasee through a listing communication form.
  * Information that will be automatically collected and stored:
    * Log Data: Datetime of all data updates and creation,  including account creation and destruction, website access, and listing edits.
    * Cookies: Subby will use (persistent and session) cookies for User recognition and personalization purposes.
  * For more Subby privacy and secuirty policies and regulations, refer to Subby's [Terms and Conditions Policy](https://rawgit.com/Kuresov/CP317-W2018-G3/master/documents/Terms&Conditions.md)


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
	* Sublet(sublet\_title: string, duration: int, price\_per\_month: double, location: string, description: string) - Class Constructor. All non-null fields are enforced except for datetime fields, which are automatically recorded by the system.


* Getters (public)
    * get\_sublet\_id(): int
    * get\_is\_sold(): boolean
    * get\_sublet\_title: string
    * get\_duration():int
    * get\_price\_per\_month(): double
    * get\_location: string
    * get\_description(): string
    * get\_created\_at(): datetime 
    * get\_updated\_at():datetime
    * get\_owner\_id(): int
* Setters (public)
    * set\_sublet\_title(title: string
    * set\_is\_sold(status: boolean) 
    * set\_duration(duration: int)
    * set\_price\_per\_month(price: double)
    * set\_location(location: string)
    * set\_description(desc: string)
    * set\_created\_at(date: datetime)
    * set\_updated\_at(date: datetime)
    * set\_owner\_id(user\_id: int)

* Relation Helpers (public)
    * save() - Commits the Sublet to the database, assuming Sublet is correctly initiated
    * reviews() - Returns an array of Reviews concerning the Sublet

## 6.2.3 Rating Package

![SubbyRatingPackage](https://i.imgur.com/szf85fl.png)
### Rating Class

### Methods
  * Constructor (public)
    * Rating(rating: int, comment : string, user\_id: int, reviewed\_user\_id:int) - Constructes a Rating

  * Getters (public)
    *  get\_comment():string - Returns the text description tied to a rating
    *  get\_reviewed\_user\_id():int - Returns the ID of the user being rated
    *  get\_user\_id():int - Returns the ID of the user who is rating another user
    *  get\_created\_at():datetime - Returns time data for time of class creation
    *  get\_updated\_at():datetime - Returns time data for time of last update to class

  * Setters (public)
    *  set\_rating(rating: tinyint) - Updates the rating review number
    *  set\_comment(comment: string) - Updates the comment for the review
    *  set\_reviewed\_user\_id(reviewed\_user\_id: int) - Updates the reviewed user ID
    *  set\_user\_id(user\_id: int) - Updates the reviewing user ID
    *  set\_created\_at(date: datetime) - Updates created\_at
    *  set\_updated\_at(date: datetime) - Updates updated\_at

  * Helpers (private)
    *  validate\_rating(rating: tinyint) - Ensures that the rating is valid (i.e A value that is held in ALLOWED\_REVIEW\_VALS)

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
    *  Favourite(user\_id: int, sublet\_id: int) - Constructes Favourite

  * Getters (public)
    *  get\_favourite\_id():int - Returns favourite ID
    *  get\_sublet\_id():int - Returns the favourited sublet ID
    *  get\_user\_id():int - Returns user ID the favourite is tied to
    *  get\_created\_at():datetime - Returns time data for time of class creation
    *  get\_updated\_at():datetime - Returns time data for time of last update to class

  * Setters (public)
    *  set\_created\_at(date: datetime) - Updates created\_at
    *  set\_updated\_at(date: datetime) - Updates updated\_at

  * Relation Helpers (public):
    * save() - Saves and persistes Favourite

## 6.2.5 Report Package
![UserPackage](https://i.imgur.com/cqmxUjY.png)

### Report Class
#### Methods
* Constructor (public)
    * Report(user\_id: int, sublet\_id: int, issue: string, description: string) - Class Constructor. All non-null fields are enforced except datetime frields, which are recorded by system automatically.

* Getters (public): only available for admins
    * get\_report\_id():int
    * get\_created\_at():datetime
    * get\_updated\_at():datetime
    * get\_issue():string
    * get\_user\_id():int
    * get\_description():string

* Setters (public): only available for admins
    * set\_report\_id(report\_id: int)
    * set\_created\_at(date: datetime)
    * set\_updated\_at(date: dateime)
    * set\_issue(issue: string)
    * set\_description(description: string)
    * set\_user\_id(user\_id: int)


* Helpers (private):
    * test\_description(description: string) - Tests the descriptions user has entered. Reject the report if the description is not valid. For example: a series of punctuations, Non english letters, a series of random letters.


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

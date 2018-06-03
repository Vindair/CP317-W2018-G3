# Subby

---
## Requirements Document
Version 1.0 – 5/20/18
1. **[Introduction](#1introduction)**  
    1.1. [Purpose](#11purpose)  
2. **[Object Classification](#2systemoverview)**  
    2.1. [Entity Objects](#211entityobjects)  
    2.1.1. [User](#211user)  
    2.1.2. [Sublet](#212sublet)  
    2.1.3. [Rating](#213rating)  
    2.1.4. [Favorite](#214favorite)  
    2.2. [Control Objects](#22controlobjects)  
    2.3. [Boundary Objects](#23boundaryobjects)  
    2.4. [Class Diagram](#22classdiagram)
3. **[Model Analysis](#3modelanalysis)**  
    3.1. [UML Diagram](#31umldiagram)
4. **[Revision History](#40revisionhistory)**  


# 1. Introduction

## 1.1. Purpose

# 2. Object Classification

## 2.1. Entity Objects

### 2.1.1. User

The User package contains the following:
* **Entity:** User
* **Controls:**
    * User Creator: Create and persist Users to the database.
    * User Manager: Edit and Destroy Users.
    * User Retriever: Retrieve single records of a User for display.
    * User Lister: List the index of Users.

As displayed in the Class Diagram, visitors are the only actors who will be able to use the User Creator view and controller. Administrators and regular users will be able to display accounts, and possibly edit them depending on their role.

### 2.1.2. Sublet

The Sublet package contains the following:
* **Entity:** Sublet
* **Controls:**
    * Sublet Creator: Create and persist Sublets to the database.
    * Sublet Manager: Edit and Destroy Sublets.
    * Sublet Lister: List the index of Sublets.
    * Sublet Searcher: Searches for Sublet records, taking params such as search query and page number.
    * Sublet Retriever: Retrieve single records of a Sublet for display.

Note that controllers such as the Sublet Manager will determine, based on User role, whether an actor has permission to edit or destroy a Sublet record. The Sublet Searcher controller will have no such authorization, as it is open to both visitors and regular users.

### 2.1.3. Rating

The Rating package contains the following:
* **Entity:** Rating
* **Controls:**
    * Rating Creator: Create and persist Ratings to the database.
    * Rating Manager: Edit and Destroy Ratings.
    * Rating Retriever: Retrieve single records of a Rating for display.

Note that both the User Display UI, Sublet Search UI, and Sublet Display UI will also use the Rating Retriever Control to display Rating information on their respective pages.

### 2.1.4. Favorite

The Favorite package contains the following:
* **Entity:** Favorite
* **Controls:**
    * Favorite Lister: Retrieve all of a User's Favorites to display the related Sublet listings.
    * Favorite Manager: Create and destroy Favorite entities.

The Sublet Search UI will display whether a Sublet listing has been "Favorited", and will access the Favorites Manager. 


## 2.2. Control Objects

## 2.3. Boundary Objects

## 2.4. Class Diagram

This class diagram shows an overall picture of the various actor interactions as well as controller/entity packages the GUI's pertain to. Note that some views will potentially retrieve data from more than one source- these have been indicated with dashed lines.

![SubbyClassDiagram](https://i.imgur.com/DFIcLAT.jpg)

# 3.0. Model Analysis

## 3.1. UML Diagram

This UML diagrams displays the various models required to accomplish the above use-cases, as well as their attributes and relations.

![SubbyUML](https://i.imgur.com/0hShmiR.jpg)

# 4.0. Revision History

---
## Version 1.0
* **Section 2**
    *  Alex Kirsopp [2.1.1-2.1.4, 2.4] [2018-06-03]
* **Section 3**
    *  Alex Kirsopp [3.1] [2018-06-03]

* **Other**
    * Alex Kirsopp - Doc layout and formatting

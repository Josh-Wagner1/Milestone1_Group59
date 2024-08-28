# Software Design Document

## Project Name: Nutritional Food - Assignment.
## Group Number: 59

## Team members

| Student Number | Name          | 
|----------------|---------------|
| s5277614       | Gemma Manns   |
| s5384766       | Joshua Wagner | 
| s5280075       | Juan Martinez | 


<div style="page-break-after: always;"></div>



# Table of Contents

<!-- TOC -->
* [Software Design Document](#software-design-document)
  * [Project Name: Nutritional Food - Assignment.](#project-name-nutritional-food---assignment)
  * [Group Number: 59](#group-number-59)
  * [Team members](#team-members)
* [Table of Contents](#table-of-contents)
  * [1. System Vision](#1-system-vision)
    * [1.1 Problem Background](#11-problem-background)
    * [1.2 System capabilities/overview](#12-system-capabilitiesoverview)
    * [1.3	Benefit Analysis](#13benefit-analysis)
  * [2. Requirements](#2-requirements)
    * [2.1 User Requirements](#21-user-requirements)
    * [2.2	Software Requirements](#22software-requirements)
    * [2.3 Use Case Diagram](#23-use-case-diagram)
    * [2.4 Use Cases](#24-use-cases)
  * [3.	Software Design and System Components](#3-software-design-and-system-components-)
    * [3.1	Software Design](#31software-design)
    * [3.2	System Components](#32system-components)
      * [3.2.1 Functions](#321-functions)
      * [3.2.2 Data Structures / Data Sources](#322-data-structures--data-sources)
      * [3.2.3 Detailed Design](#323-detailed-design)
  * [4. User Interface Design](#4-user-interface-design)
    * [4.1 Structural Design](#41-structural-design)
    * [4.2	Visual Design](#42visual-design)
<!-- TOC -->


<div style="page-break-after: always;"></div>



## 1. System Vision (Gemma)

### 1.1 Problem Background

#### Problem Identification: What problem does this system solve?

The system addresses the challenge of accessing and understanding detailed nutritional information for a wide range of food items. Many individuals, healthcare professionals, and dietitians struggle to find reliable and comprehensive nutritional data in a user-friendly format. This tool solves the problem by providing a centralised platform where users can easily search for foods, analyse their nutritional content, and make informed dietary decisions. It facilitates personalised diet planning, supports health and medical research, and helps users manage specific dietary requirements or restrictions.

#### Dataset: What is the dataset used?

The dataset used is a CSV file named Nutritional_Food_Database.csv. This database contains detailed nutritional information for various food items commonly consumed around the world. It includes columns that describe food names and their nutritional content, such as caloric value, fat types, carbohydrates, proteins, vitamins, minerals, and more. The dataset is essential for supporting a wide range of dietary, health, and medical research applications.

#### Data Input/Output: What kind of data input and output is required?
**Data Input:**
- **Text Input:** Users will input text strings when searching for specific food items by name or when selecting nutrients to filter by range or level.
- **Numerical Input:** Users may enter numerical values to set minimum and maximum ranges for specific nutrients, such as calories, fat, or protein content.
- **Selection Input:** Users will use selection inputs, such as drop-down menus or checkboxes, to choose specific nutrients or categories of nutrients for analysis and filtering.

**Data Output:**
- **Textual Output:** The system will display lists of food items along with their corresponding nutritional information based on user searches and filters.
- **Graphical Output:** The tool will generate visual representations, such as pie charts and bar graphs, to illustrate the nutritional breakdown of selected food items. These visuals will help users easily interpret the data and make informed decisions.
- **Filtered Results:** The system will provide filtered lists of foods that meet the criteria set by the user, such as foods within a certain caloric range or with a specific nutrient level.

#### Target Users: Who will use the system, and why?

- **Sports Professionals**: Use the tool to optimise dietary plans for athletes by selecting foods that meet specific nutritional needs, such as high protein or low fat.
- **People with Dietary Requirements or Restrictions**: Individuals with allergies, medical conditions, or personal dietary preferences can use the system to find foods that align with their specific nutritional requirements.
Doctors: Utilise the tool to recommend and plan dietary interventions for patients with specific health conditions, such as diabetes, cardiovascular issues, or obesity.
- **Nutritionists**: Use the system to create balanced diet plans for clients, ensuring that all nutritional needs are met based on detailed food data.
- **Dietitians**: Provide expert advice and feedback on food choices, using the tool to support patient dietary management and to educate clients on healthy eating.
- **Health-Conscious Consumers**: Individuals looking to make informed decisions about their food choices can use the tool to understand the nutritional content of the foods they consume and to plan meals that support their health goals.

### 1.2 System capabilities/overview

The System will do the following:

- Display results from the following searches of the Database:
  - Food Search - Text search names for specific entries. 
  - Nutrition Range Filter - Filter entries by nutrition values
  - Nutrition Level Filter - Filter entries by nutritional content levels. 
- Display the nutritional breakdown of entries when selected by the end user, in both numerical and graphical form.  
- View Changelog


### 1.3	Benefit Analysis

The Nutritional Food Analysis System provides significant value across various user groups, contributing to better dietary decisions, improved health outcomes, and enhanced professional practice. The benefits of the system include:

**Enhanced Dietary Planning:**
  - Personalised Diets: The system enables users to tailor their diets based on specific nutritional needs, whether for weight management, athletic performance, or medical conditions. By providing detailed nutritional information and filtering options, users can easily find foods that align with their dietary goals.
  - Accurate Nutritional Calculations: The weight-based nutritional calculator allows users to scale the nutritional content of food items, ensuring precise portion control and more accurate dietary planning.

**Improved Health Outcomes:**
  - Informed Food Choices: By offering detailed and reliable nutritional data, the system empowers users to make informed food choices that support their health objectives. This is particularly beneficial for individuals managing conditions like diabetes, cardiovascular diseases, or obesity.
  - Support for Health Professionals: Nutritionists, dietitians, and doctors can use the system to develop and recommend scientifically-backed dietary plans, enhancing patient care and dietary interventions.

**Educational Value:**
  - Nutritional Awareness: The system’s visual representation tools, such as pie charts and bar graphs, make it easier for users to understand the nutritional content of foods. This helps in educating users about balanced diets and the impact of different nutrients on health.
  - Accessible Information: The user-friendly interface and comprehensive database make nutritional information accessible to a wide audience, from health-conscious consumers to professionals in the healthcare industry.

**Time Efficiency:**
  - Quick Food Searches: The advanced search and filtering capabilities allow users to quickly find and analyse food items, saving time compared to traditional methods of dietary research.
  - Streamlined Professional Use: For professionals like nutritionists and dietitians, the system streamlines the process of dietary analysis and planning, allowing them to focus more on client interaction and less on manual data processing.

**Comprehensive Data Access:**
  - Centralised Nutritional Information: The system acts as a central repository for detailed nutritional data, reducing the need to consult multiple sources and ensuring consistency in the information provided.

## 2. Requirements (Josh)

### 2.1 User Requirements
#### End users:
We have listed a fair few end users that could potentially use the product, however “Nutritionist” (or other health professional) and “Health-conscious consumers” are the users that are most likely to fully interact with the program.

**Nutritionist:**

A Nutritionist is an example of a user that may use the program to find a wide variety of foods/ food combinations on behalf of a that meets their dietary needs. To this this primarily do searches across the database primarily using nutrition range and nutrition level filters rather than specific searches with text. They may also use the food calculator so they can correctly portion these foods (and their nutritional levels) for their specified client.

**Nutritionist user needs:**
* An easily accessible search function built for bulk searches.
* Is correct and consistent with its data.
* Filters that are relevant to what they need (Calorific value, Protein, Fat, Carbs, Sodium) while also giving the option for more niche filters for specific searches (like vitamins and minerals).
* A calculation feature that can reliably and accurately scale the nutritional stats of an item based on its weight.

**Health-Conscious Consumers:**

While health-conscious consumers might be more concerned with the specific details of a single food. E.g. they want to know the nutritional benefits of pulled pork for a dinner the following night. They will do this by inputting text into the search bar to look for the stated food. Another such example is a consumer looking up a specific cheese only to find it has too much saturated fat or is lacking another type of nutritional value. So, they do a general search of for “cheese” with a limit of 5g of fat on fat to find some alternate options.

**Health-conscious consumer needs:**
* Search feature can help pinpoint a specific food.
* Search text and filters can help find a range of foods that can are useful for their diet.
* UI is simple and easy to navigate and complete a search within seconds.

#### Operational users:
Like the end users there are a fair few operational users but the main ones that directly interact with the end user are the “Database Administrator” and the “System” itself. Taking from the perspective of the end user both these user’s serve different roles:

**Database Administrator**
The Database Administrator plays a simple role of providing downloadable updates to the database/ program in case it goes out of date or needs maintenance. Their only direct interaction with the client is the popup and changelog of what has been modified. 

**Database administrator needs:**
* Easily accessible UI to update the data.
* A way to log changes through a change-log field.

**System:**
While the System is the sole user that interacts with the program to provide the main services. With every food search (along with applied filters) the system will return the appropriate result(s) for the search. When the user selects a food item, the system will also display a page with the relevant pie charts and bar graphs on its nutritional breakdown. The final task for the system to calculate the nutritional information on based on a food item and weight set by the user.

**System user needs:**
* Full access to the stored data instance for reading purposes.
* A compute module for the functionality of the Food Calculator function.
* To be regularly updated if there is a change to the stored information.


### 2.2	Software Requirements

#### Functional requirements:
* R1.1 The program shall only accept all standard English letters, symbols and numerical characters as an input.
* R1.2 The program shall use the stored “Nutritional_Food_Database.csv” as its sole source of information and provide search results based on it.
* R2.1 The Food Search shall provide a list of all applicable results that contain the text contents of the user’s input. 
* R3.1 The Nutrition Breakdown function shall show pie charts and bar graphs displaying the nutritional breakdown of the selected food. 
* R4.1 The Nutrition Range Filter shall accept a string value to determine the nutrition being range limited.
* R4.2 The Nutrition Range Filter shall accept floating point values to constrain the minimum and maximum value of a specific nutrition that show up in the results.
* R5.1 The Nutrition Level Filter shall provide a dropdown value to filter their search results based on nutritional density which includes “LOW”, “MEDIUM” and “HIGH” as selectable values or “NONE” as a placeholder if undecided.
* R6.1 The Weight calculator feature shall give the option for the user to input a food item in plaintext along with a numerical weight (in grams) in which they can scale the other nutritional values with.
* R6.2 The Weight calculator shall provide a list of scaled nutritional values based on the inputted food and weight. 

#### Non-Functional requirements: 
* R1.1 User Interface is clean and easy to navigate.
* R2.1 Widget layout is consistent both in size and position.
* R3.1 Widgets follow the same layout/sizing practices of other applications.
* R4.1 List of values is properly aligned with associated nutrition column names.
* R5.1 Buttons and navigational widgets transfer to the correct Frame/ function when interacted with.

### 2.3 Use Case Diagram

![Use Case Diagram](./UCD.png)

### 2.4 Use Cases

| Use Case ID    | UC-01                                                                                                                               |
|----------------|-------------------------------------------------------------------------------------------------------------------------------------|
| Use Case Name  | Search for food item                                                                                                                |
| Actors         | User                                                                                                                                |
| Description    | The user enters an item they want to search for in the textbox and presses search to retrieve all results that match the query.     |
| Flow of Events | 1. The user selects the search bar.                                                                                                 |
|                | 2. The user writes a text input the matches/closely relates to an item they want to search for.                                     |
|                | 3. The user presses search                                                                                                          |
|                | 4. The system retrieves all matching rows.                                                                                          |
|                | 5. The system displays the results (or lack thereof).                                                                               |
| Alternate Flow | 1. If there are no matching results the user is notified through a message after pressing search and sent back to the search screen |

| Use Case ID    | UC-02                                                                                                                                                                                         |
|----------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Use Case Name  | Search using range filter                                                                                                                                                                     |
| Actors         | User                                                                                                                                                                                          |
| Description    | The user designates one nutritional value to filter by along with defining a minimum and maximum threshold for its corresponding value and returns food items that match the specified values |
| Flow of Events | 1. User selects the nutritional filter feature.                                                                                                                                               |
|                | 2. The user selects “nutritional range” option.                                                                                                                                               |
|                | 3. The user inputs the nutrient they want to filter by.                                                                                                                                       |
|                | 4. The user specifies a floating-point minimum and maximum nutritional value for the nutrient.                                                                                                |
|                | 5. The user presses the “confirm” button.                                                                                                                                                     |
|                | 6. The system retrieves all matching rows.                                                                                                                                                    |
|                | 7. The system displays the results (or lack thereof).                                                                                                                                         |
| Alternate Flow | 1. If there are no matching results the user is notified through a message after pressing search and sent back to the nutritional range screen.                                               |
|                | 2. If the user presses “Filter again” it will return back to the filter screen to repeat the flow of events.                                                                                  |

| Use Case ID    | UC-03                                                                                                                                                                                                                   |
|----------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Use Case Name  | Search using level filter                                                                                                                                                                                               |
| Actors         | User                                                                                                                                                                                                                    |
| Description    | The user designates one nutritional value to filter by along with defining if its nutritional levels is “LOW”, “MEDIUM” or “HIGH” compared to the maximum value and returns food items that matches the specified range |
| Flow of Events | 1. User selects the nutritional filter feature.                                                                                                                                                                         |
|                | 2. The user selects “nutritional level” option.                                                                                                                                                                         |
|                | 3. The user inputs the nutrient they want to filter by.                                                                                                                                                                 |
|                | 4. The user specifies if they want the nutritional level to be “LOW”, “MEDIUM” or “HIGH”.                                                                                                                               |
|                | 5. The user presses the “confirm” button.                                                                                                                                                                               |
|                | 6. The system retrieves all matching rows.                                                                                                                                                                              |
|                | 7. The system displays the results (or lack thereof).                                                                                                                                                                   |
| Alternate Flow | 1. If the user presses “Filter again” it will return back to the filter screen to repeat the flow of events.                                                                                                            |

| Use Case ID    | UC-04                                                                                                                           |
|----------------|---------------------------------------------------------------------------------------------------------------------------------|
| Use Case Name  | View nutritional breakdown                                                                                                      |
| Actors         | User                                                                                                                            |
| Description    | The user selects 1 food and the system displays its nutritional breakdown of the food in the form of pie charts and bar graphs. |
| Flow of Events | 1. User selects a food item.                                                                                                    |
|                | 2. The system searches the for the full data of the selected food item.                                                         |
|                | 3. The systems displays pie charts and bar graphs based on the food items nutritional breakdown.                                |
|                | 4. The user specifies if they want the nutritional level to be “LOW”, “MEDIUM” or “HIGH”.                                       |
|                | 5. The user presses the “confirm” button.                                                                                       |
|                | 6. The system retrieves all matching rows.                                                                                      |
|                | 7. The system displays the results (or lack thereof).                                                                           |
| Alternate Flow | 1. The system gives the user an option to select another food item. If selected repeat the flow of events again.                |

| Use Case ID    | UC-05                                                                                                                                                                        |
|----------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Use Case Name  | Weight Calculator                                                                                                                                                            |
| Actors         | User                                                                                                                                                                         |
| Description    | The user inputs a food item and floating-point weight in grams that the system uses to calculate and display the appropriately scaled nutrient composition of the food item. |
| Flow of Events | 1. User selects weight calculator feature.                                                                                                                                   |
|                | 2. User inputs the food item’s name and weight they desire it to be scaled to.                                                                                               |
|                | 3. The system searches for the food item and calculates the results.                                                                                                         |
|                | 4. The system displays the scaled nutrient composition for the specified weight.                                                                                             |
| Alternate Flow | 1. If the food item doesn’t exist in the database the user is prompted to input the food item and weight again.                                                              |
|                | 2. The system gives the user an option to select another food item to calculate. If selected repeat the flow of events again.                                                |                                                                                                                                                                              |

## 3.	Software Design and System Components 

### 3.1	Software Design
 
![Software Design](./FlowChart.png)

### 3.2	System Components

#### 3.2.1 Functions
List all key functions within the software. For each function, provide:
- Description: Brief explanation of the function’s purpose.
- Input Parameters: List parameters, their data types, and their use.
- Return Value: Describe what the function returns.
- Side Effects: Note any side effects, such as changes to global variables or data passed by reference.

#### 3.2.2 Data Structures / Data Sources
List all data structures or sources used in the software. For each, provide:

- Type: Type of data structure (e.g., list, set, dictionary).
- Usage: Describe where and how it is used.
- Functions: List functions that utilize this structure.

#### 3.2.3 Detailed Design
Provide pseudocode or flowcharts for all functions listed in Section 3.2.1 that operate on data structures. For instance, include pseudocode or a flowchart for a custom searching function.


## 4. User Interface Design

### 4.1 Structural Design
Present a structural design, a hierarchy chart, showing the overall interface’s structure. Address:

- Structure: How will the software be structured?
- Information Grouping: How will information be organized?
- Navigation: How will users navigate through the software?
- Design Choices: Explain why these design choices were made.

Example:  
![Structural Design](./Structural_Design.png)

### 4.2	Visual Design
Include all wireframes or mock-ups of the interface. Provide a discussion, explanation, and justification for your design choices. Hand-drawn wireframes are acceptable.

- Interface Components: Clearly label all components.
- Screens/Menus: Provide wireframes for different screens, menus, and options.
- Design Details: Focus on the layout and size of components; color and graphics are not required. 

Example:  
![Visual Design](./visual_design.png)




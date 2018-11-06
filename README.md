# Table of Contents
1. [Problem](README.md#problem)
2. [Approach](README.md#approach)
3. [Output](README.md#output)
4. [Run Instructions](README.md#run-instructions)

# Problem

According to the challenge, a newspaper editor was researching immigration data trends on H1B(H-1B, H-1B1, E-3) visa application processing over the past years, trying to identify the occupations and states with the most number of approved H1B visas. The code calculates the **Top 10 Occupations** and **Top 10 States** for **certified** visa applications given each year of data, formatted with the name of "h1b_input.csv" under the 'input' directory.


# Approach

After reading in the data, I identified the indexes of relevant entries by analyzing the title labels. I traversed rows of data entries and collected relevant information using the indexes identified in the previous step. I then conducted calculation on each category and format the data into the desired output. Finally, I called a dedicated output function to write results into the target directory. 


# Output 

* `top_10_occupations.txt`: Top 10 occupations for certified visa applications
* `top_10_states.txt`: Top 10 states for certified visa applications

Each line holds one record and each field on each line is separated by a semicolon (;).

Each line of the `top_10_occupations.txt` file contains:
1. __`TOP_OCCUPATIONS`__: Use the occupation name associated with an application's Standard Occupational Classification (SOC) code
2. __`NUMBER_CERTIFIED_APPLICATIONS`__: Number of applications that have been certified for that occupation. An application is considered certified if it has a case status of `Certified`
3. __`PERCENTAGE`__: % of applications that have been certified for that occupation compared to total number of certified applications regardless of occupation. 

The records in the file are sorted by __`NUMBER_CERTIFIED_APPLICATIONS`__, and in case of a tie, alphabetically by __`TOP_OCCUPATIONS`__.

Each line of the `top_10_states.txt` file should contains:
1. __`TOP_STATES`__: State where the work will take place
2. __`NUMBER_CERTIFIED_APPLICATIONS`__: Number of applications that have been certified for work in that state. An application is considered certified if it has a case status of `Certified`
3. __`PERCENTAGE`__: % of applications that have been certified in that state compared to total number of certified applications regardless of state.

The records in this file must are sorted by __`NUMBER_CERTIFIED_APPLICATIONS`__ field, and in case of a tie, alphabetically by __`TOP_STATES`__. 


# Run Instructions

Please put input data into 'h1b_input.csv' under the 'input' directory and use the run.sh file to execute the code.

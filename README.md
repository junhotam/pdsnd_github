# Bike Share Data Analysis

## Overview

Bicycle-sharing systems have become increasingly popular in cities worldwide. These systems allow users to rent bicycles for short periods, either for one-way trips or round trips. With the integration of modern technology, data on bike usage has become readily available, enabling analysis of patterns and trends.
g
This project leverages bike share data from three major U.S. cities—Chicago, New York City, and Washington, DC—to explore usage patterns and uncover key insights.

## Datasets

The analysis uses data provided by Motivate, a bike share system provider. The dataset includes randomly selected records from the first six months of 2017 for each city. Each dataset contains six core columns:

- **Start Time** (e.g., `2017-01-01 00:07:57`)
- **End Time** (e.g., `2017-01-01 00:20:53`)
- **Trip Duration** (in seconds, e.g., `776`)
- **Start Station** (e.g., `Broadway & Barry Ave`)
- **End Station** (e.g., `Sedgwick St & North Ave`)
- **User Type** (Subscriber or Customer)

Additionally, the Chicago and New York City datasets contain:

- **Gender**
- **Birth Year**

## Analysis Performed

This project computes various descriptive statistics to analyze bike-sharing trends, including:

### 1. Popular Times of Travel

- Most common month
- Most common day of the week
- Most common hour of the day

### 2. Popular Stations and Trips

- Most common start station
- Most common end station
- Most common trip (start to end combination)

### 3. Trip Duration

- Total travel time
- Average travel time

### 4. User Information

- Counts of each user type
- Counts of each gender (for NYC and Chicago only)
- Earliest, most recent, and most common year of birth (for NYC and Chicago only)

## Files Included

The project consists of the following files:

- ``: The main Python script for analyzing the data

## Getting Started

### Prerequisites

To run this project, you need:

- Python 3
- Pandas library

### Running the Script

1. Clone the repository or download the project files.
2. Navigate to the project directory.
3. Run the script using:
   ```sh
   python bikeshare.py
   ```
4. Follow the on-screen prompts to select a city and view insights.




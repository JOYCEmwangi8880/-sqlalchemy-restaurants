## Introduction

Welcome to the Restaurants Application! This application provides a  platform for managing restaurant information, customer records, customer reviews, and even an anagram checker. Whether you're a restaurant owner, a customer, or just an anagram enthusiast, this application has something for you.

## Features

The Restaurants Application offers a range of features, including:

- **Restaurant Management**: Easily add, update, or delete restaurant information, including names and price ranges.

- **Customer Management**: Keep track of customer records, including first names and last names.

- **Review System**: Allow customers to leave detailed reviews for restaurants, complete with star ratings and feedback.

## Usage of the project

- **Restaurant Information**: Easily access and manage restaurant details.

- **Customer Records**: Keep customer records up to date.

- **Review System**: Enable customers to leave detailed reviews for restaurants.

- **Anagram Checker**: Use the built-in anagram checker to find anagrams within a list of words.

## Database Schema

The Restaurants Application uses a simple and effective database schema consisting of three tables:

- **restaurants**: Stores essential restaurant information, including names and price ranges.

- **customers**: Maintains customer records, including first names and last names.

- **reviews**: Records customer reviews for restaurants, including star ratings and feedback.

Here's a simplified schema diagram:
```
+---------------+        +--------------+        +-------------+
|  restaurants  |   1    |   reviews    |   N    |   customers |
|---------------| ------ |--------------| ------ |-------------|
| id            |        | id           |        | id          |
| name          |   <----| restaurant_id| ---->  | first_name  |
| price         |        | customer_id  |        | last_name   |
+---------------+        | star_rating
                            comments  |        +-------------+
                        | |
                        +--------------+


 ## Contributing

Contributions to the Restaurants Application are encouraged and welcome! If you have any suggestions, bug reports, or feature requests. If you'd like to contribute to the project, please fork the repository, make your changes, and submit a pull request.

### License

This project is licensed under the `MIT` License. 

## Author
It is written by Joyce Mwangi

## Github: https://github.com/JOYCEmwangi8880

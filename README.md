# Financial Control System

This is a simple financial control system built with Python. The goal of this project is to practice backend fundamentals such as data persistence, project organization, and input validation.

## What the project does

The system allows the user to deposit money, withdraw money, view the current balance, store all transactions in a database, and search transactions using different filters such as type (deposit or withdraw), value, date, and period (date range).

## Technologies used

Python, SQLite (relational database), and basic SQL queries.

## Project Structure

main.py (controls program flow and user interaction)  
service.py (handles business logic and validations)  
database.py (manages database operations and queries)  
account.py (represents account behavior and rules)

## How to run

Clone the repository, go to the project folder, and run the application with Python. The database will be created automatically when the program runs.

## How it works (high level)

The project is organized into simple layers: the main file controls the application flow and user interaction, the service layer handles business logic and validations, the database layer is responsible for storing and retrieving data, and the account model manages balance operations.

## What I learned

I learned how to structure a backend project, how to separate responsibilities between layers (main, service, database, model), how to use basic SQL with SQLite, how to persist data in a relational database, and how to handle user input and validation.

## Improvements

Replaced JSON storage with SQLite database, improved project organization, and added a service layer to separate business logic.

## Future improvements

Use a more robust database like PostgreSQL or MySQL, turn the system into an API (using Flask or FastAPI), and add user accounts and authentication.

## Author

Project developed for backend learning and practice.
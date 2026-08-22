# Bank System

A banking system simulator developed in Python as a portfolio project, focused on object-oriented programming, database integration, layered architecture, validation, authentication, and transaction management.

The project simulates basic banking operations through a terminal-based user interface and uses PostgreSQL as its database.

> **Project status:** MVP (Minimum Viable Product)

[🇧🇷 Portuguese version](README-pt.md)

---

## Overview

Bank System is a Python application that simulates a simple banking environment.

The system allows users to create an account, authenticate using their CPF and password, view their account information, perform deposits and withdrawals, and access their transaction statements.

The system also includes an administrator interface that allows administrators to search for users, accounts, and transactions.

The project was designed with a layered architecture to separate responsibilities between the user interface, services, repositories, entities, validation, security, and database layers.

---

## Features

### User

The current MVP allows users to:

* Register a new user
* Create a bank account during registration
* Authenticate using CPF and password
* View personal information
* View account information
* View account balance
* Deposit money
* Withdraw money
* View transaction statements
* View transactions from the last 30 days
* View transactions from the last 90 days
* View deposit transactions
* View withdrawal transactions
* View all transactions
* Return to previous menus
* Log out

---

### Administrator

The administrator interface currently provides several search and management features.

#### User search

Administrators can search for a specific user by:

* ID
* CPF
* Email
* Phone number

After finding a user, the administrator can access a more detailed view containing information about the user and their associated account.

The detailed view currently allows the administrator to:

* View personal information
* View account information
* View account status
* Activate an account
* Block an account
* View the user's transaction statements

---

#### Account search

Administrators can search for accounts by:

* Account ID
* Account number
* Active status
* Blocked status

The system can also perform global searches, returning multiple accounts based on their current status.

---

#### Transaction search

Administrators can search transaction records using:

* Transactions from the last 30 days
* Transactions from the last 90 days
* Deposit transactions
* Withdrawal transactions
* Complete transaction history

---

## Architecture

The project follows a layered architecture to keep responsibilities separated.

```text
Bank-System/
│
├── database/
│   ├── connection.py
│   └── initializer.py
│
├── entities/
│
├── exceptions/
│
├── repositories/
│
├── security/
│
├── services/
│
├── ui/
│
├── validators/
│
├── .env.example
├── .gitignore
├── main.py
├── requirements.txt
└── README.md
```

### Main layers

#### UI

Responsible for interaction with the user through the terminal.

The UI handles:

* Menus
* User input
* Displaying information
* Calling the appropriate services
* Presenting validation and business errors to the user

The UI does not directly access the database.

---

#### Services

Contains the application's business logic.

Examples include:

* User services
* Account services
* Authentication services
* Banking services
* Transaction services
* Administrator services

Services coordinate repositories, validators, security components, and database operations.

---

#### Repositories

Responsible for database access.

Repositories contain operations such as:

* Creating records
* Searching records
* Updating records
* Retrieving transactions
* Searching users and accounts

This layer isolates SQL operations from the rest of the application.

---

#### Entities

Represent the main objects of the banking system.

Examples include:

* User
* Account
* Transaction

---

#### Validators

Responsible for validating user input before it reaches the business logic.

Examples include:

* CPF validation
* Email validation
* Phone validation
* Date validation
* Password validation
* Amount validation
* ID validation
* Account number validation

---

#### Security

Contains security-related functionality.

The current project uses password hashing to avoid storing user passwords directly in the database.

---

#### Database

The project uses PostgreSQL as its relational database.

The database connection is configured through environment variables rather than storing credentials directly in the source code.

---

## Database

The MVP uses three main entities:

```text
User
  │
  │ 1:1
  ▼
Account
  │
  │ 1:N
  ▼
Transaction
```

### Users

Stores personal and authentication information.

Examples:

* ID
* First name
* Last name
* CPF
* Birth date
* Email
* Phone
* Password hash

---

### Accounts

Stores banking account information.

Examples:

* Account ID
* User ID
* Account number
* Balance
* Status
* Creation date

Account statuses currently include:

* `ACTIVE`
* `BLOCKED`

---

### Transactions

Stores financial operations performed on accounts.

Examples:

* Transaction ID
* Account ID
* Transaction type
* Amount
* Description
* Creation date

---

## Technologies

The project was developed using:

* Python
* PostgreSQL
* Psycopg
* Object-Oriented Programming
* SQL
* Git
* GitHub

External Python libraries include:

* `psycopg`
* `bcrypt`
* `python-dotenv`
* `email-validator`
* `validate-docbr`
* `phonenumbers`

Python standard-library modules are also used throughout the project, including modules such as:

* `datetime`
* `decimal`
* `re`
* `os`

---

## Requirements

Before running the project, make sure you have installed:

* Python 3
* PostgreSQL
* Git

The project dependencies are listed in:

```text
requirements.txt
```

Install them with:

```bash
pip install -r requirements.txt
```

---

## Environment Variables

Database credentials are not stored directly in the source code.

The project uses a `.env` file to store local configuration.

Create a `.env` file based on the provided example:

```text
.env.example
```

The environment file should contain the database configuration required by the application.

Example:

```env
DB_HOST=localhost
DB_PORT=5432
DB_NAME=bank_system
DB_USER=postgres
DB_PASSWORD=your_password
```

The `.env` file is ignored by Git and should not be committed to the repository.

---

## Running the Project

After installing the dependencies and configuring PostgreSQL:

### 1. Clone the repository

```bash
git clone <repository-url>
```

### 2. Enter the project directory

```bash
cd Bank-System
```

### 3. Create and activate a virtual environment

Windows:

```bash
python -m venv venv
venv\Scripts\activate
```

Linux/macOS:

```bash
python3 -m venv venv
source venv/bin/activate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

### 5. Configure the environment variables

Create your `.env` file based on `.env.example`.

### 6. Configure PostgreSQL

Create a PostgreSQL database with the name configured in your `.env` file.

The application is responsible for initializing the required database tables.

### 7. Run the application

```bash
python main.py
```

---

## Application Flow

The application starts with the main menu.

```text
Main Menu
│
├── User
│   ├── Register
│   ├── Login
│   │   ├── Account Information
│   │   ├── Deposit
│   │   ├── Withdrawal
│   │   ├── Transactions
│   │   │   ├── Last 30 Days
│   │   │   ├── Last 90 Days
│   │   │   ├── Deposits
│   │   │   ├── Withdrawals
│   │   │   └── All Transactions
│   │   └── Logout
│   └── Back
│
├── Administrator
│   ├── Users
│   │   ├── Search by ID
│   │   ├── Search by CPF
│   │   ├── Search by Email
│   │   └── Search by Phone
│   │
│   ├── Accounts
│   │   ├── Search by ID
│   │   ├── Search by Account Number
│   │   ├── Search Active Accounts
│   │   └── Search Blocked Accounts
│   │
│   ├── Transactions
│   │   ├── Last 30 Days
│   │   ├── Last 90 Days
│   │   ├── Deposits
│   │   ├── Withdrawals
│   │   └── All Transactions
│   │
│   └── Back
│
└── Exit
```

---

## Data Validation

The application validates user input before processing operations.

Examples include:

* Invalid CPF
* Invalid email
* Invalid phone number
* Invalid date
* Invalid ID
* Invalid account number
* Invalid transaction amount
* Invalid password

The password validation rules currently require:

* At least 8 characters
* At least one uppercase letter
* At least one number
* At least one special character

---

## Authentication and Password Security

User passwords are not stored as plain text.

The project uses `bcrypt` to generate password hashes before storing authentication data in the database.

During login, the provided password is compared against the stored hash.

---

## Error Handling

The application uses custom exceptions to separate different types of errors.

Examples include:

* Invalid input
* Invalid CPF
* Invalid email
* Invalid phone number
* Invalid password
* Resource not found
* Account-related errors

These exceptions allow the service layer to communicate errors to the UI without placing business logic directly inside the interface.

---

## Current MVP Limitations

This project is currently an MVP.

The core banking flow is functional, but not every service method implemented in the project has been exposed through the user interface yet.

Some administrator features are also still being expanded.

For example, account status changes are currently implemented, but the blocked status does not yet restrict all banking operations performed by the user.

The administrator authentication flow is also intentionally simplified in the current MVP and will be improved in a future version.

---

## Future Improvements

Planned improvements include:

* Implement administrator authentication
* Fully enforce blocked account restrictions
* Expand administrator account management
* Improve administrator transaction search
* Improve account selection after global searches
* Add more transaction filtering options
* Improve UI navigation
* Add automated tests
* Improve error handling and user feedback
* Improve application security
* Expand database functionality
* Add more comprehensive documentation
* Improve project architecture as the system grows

---

## Project Goals

The main goal of this project is to practice and demonstrate software development concepts using a realistic banking-system scenario.

The project focuses on:

* Python
* Object-oriented programming
* Clean separation of responsibilities
* Layered architecture
* Database integration
* SQL
* PostgreSQL
* Authentication
* Password hashing
* Input validation
* Exception handling
* Repository pattern
* Service layer
* Dependency injection
* Git and GitHub

---

## Disclaimer

This project is an educational and portfolio application.

It is a simulation of a banking system and is **not intended for real financial transactions or production banking environments**.

---

## Author

Developed as a personal portfolio project to practice Python backend development, databases, software architecture, and application design.

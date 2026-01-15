# SOFTWARE DEVELOPMENT LIFE CYCLE (SDLC) OF SRMS

The development of the School Result Management System (SRMS) followed the standard Software Development Life Cycle (SDLC) phases as explained below.

# Planning Phase

In this phase, the problem to be solved was identified.

Problem Identified

Many schools manage results manually, which leads to:
	•	Calculation errors
	•	Loss of student records
	•	Time-consuming processes


# Requirements Analysis Phase

At this stage, the requirements of SRMS were identified and documented in the Software Requirements Specification (SRS).

Functional Requirements
	•	The system shall allow the admin to add students.
	•	The system shall allow the admin to add subjects.
	•	The system shall allow the admin to record scores.
	•	The system shall calculate total, average, and grade.
	•	The system shall display a student’s result.

Non-Functional Requirements
	•	The system shall be easy to use (console-based).
	•	The system shall store data persistently using SQLite.
	•	The system shall be reliable and accurate.

Outcome
	•	SRS document created (SRS.md)

# System Design Phase

In this phase, the structure and components of SRMS were designed.

System Architecture

The system was divided into two main modules:
	1.	Database Module – `srms_db.py`
	•	Implemented using the SRMSDB class
	•	Handles database creation and data operations
	2.	Console Module – `srms_console.py`
	•	Implemented using the SRMSApp class
	•	Handles user interaction and menu display

# Database Design

Three tables were designed:
	•	students
	•	subjects
	•	scores

# Implementation Phase

In this phase, the system was coded according to the design.

Programming Language
	•	Python

Implementation Details
	•	The SRMSDB class in `srms_db.py` handles:
	•	Adding students
	•	Adding subjects
	•	Recording scores
	•	Fetching results
	•	The SRMSApp class in `srms_console.py`:
	•	Displays menu options
	•	Accepts user input
	•	Calls database functions


# Testing Phase

The system was tested to ensure it works correctly.

Types of Testing
	•	Unit Testing: Testing individual functions like adding students.
	•	Integration Testing: Ensuring `srms_console.py` interacts correctly with `srms_db.py`.
	•	Input Validation Testing: Ensuring scores are between 0 and 100.

# Deployment Phase

After successful testing, the system was deployed.

Deployment Method
	•	The project files were uploaded to a GitHub repository.
	•	The system can be run using:
python `srms_console.py`

# Maintenance Phase

This phase involves future improvements and updates.

Possible Enhancements
	•	User authentication
	•	Web-based version
	•	Printable result sheets



# CodeAlpha Data Redundancy Removal System

## Project Overview

A cloud-based web application that detects and prevents duplicate data.

## Architecture

User
↓
AWS EC2
↓
Flask Application
↓
Duplicate Detection
↓
PostgreSQL on AWS RDS

## Technologies

- Python
- Flask
- PostgreSQL
- AWS EC2
- AWS RDS
- GitHub
- Linux

## Duplicate Detection Rule

The system uses email as a unique identifier.

If an email already exists in the database, the system rejects the new record.

## Security

- RDS is not publicly accessible.
- PostgreSQL uses port 5432.
- Database access is restricted to the EC2 Security Group.
- Database credentials are stored in environment variables.

## Result

The system successfully detects duplicate records and stores unique records in PostgreSQL.

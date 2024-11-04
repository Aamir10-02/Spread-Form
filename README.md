# Flask Application with Google Sheets Integration

This repository contains a Flask web application that integrates with Google Sheets to store user information. It utilizes Google Sheets API for data storage and provides a simple user interface for inputting and displaying data.

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Architecture](#architecture)
- [Setup and Installation](#setup-and-installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Environment Variables](#environment-variables)
- [Acknowledgements](#acknowledgements)


## Introduction

This project demonstrates a Flask application that allows users to submit their information via a web form. The data is stored in a Google Sheet, which is updated using the Google Sheets API. The application provides a user-friendly interface for data entry and displays the entered information on a separate page.

## Features

- **Form Submission**: Users can submit their name, email, role, recommendation, programming languages, and comments.
- **Data Storage**: Information is saved in a Google Sheet for easy access and management.
- **Session Management**: Displays a welcome message on a separate page after form submission.
- **Responsive Design**: The user interface is designed to be intuitive and easy to use.

## Architecture

1. **Frontend**: HTML templates for user input and display (located in the `templates` directory).
2. **Backend**: Flask web framework for handling HTTP requests and interacting with Google Sheets.
3. **Google Sheets API**: Used for data storage and retrieval.
4. **Session Management**: Flask sessions are used to manage user data between requests.

## Setup and Installation

### Prerequisites

- Python 3.6+
- Virtualenv (recommended)
- Google Cloud Platform account with Google Sheets API enabled

### Installation Steps

1. **Clone the repository**
    ```bash
    git clone https://github.com/Aamir10-02/Spread-Form.git
    cd flask-google-sheets
    ```

2. **Create a virtual environment**
    ```bash
    python -m venv venv
    source venv\Scripts\activate`
    ```

3. **Install dependencies**
    ```bash
    pip install -r requirements.txt
    ```

4. **Set up Google Sheets API**
    - Create a Google Cloud project and enable the Google Sheets API.
    - Create a service account and download the JSON credentials file.
    - Encode the credentials file in base64 and set it as an environment variable named `GOOGLE_CREDENTIALS`.

5. **Set environment variables**
    ```bash
    export GOOGLE_CREDENTIALS=<your-base64-encoded-credentials>
    ```

### Running the Application

1. **Start the Flask application**
    ```bash
    python application.py
    ```

2. **Access the application**
    Open your web browser and navigate to `http://127.0.0.1:5000`.

## Project Structure

```plaintext
flask-google-sheets/
├── application.py          # Main Flask application
├── requirements.txt        # List of dependencies
├── templates/              # HTML templates
│   ├── first.html
│   └── display_info.html
└── static/                 # Static files (CSS, JS, images)
    └── styles.css
```

## Environment Variables
- 'GOOGLE_CREDENTIALS': Base64 encoded Google service account credentials JSON. Used for authenticating with Google Sheets API.


## Acknowledgements
- Flask: Web framework used for creating the web interface.
- gspread: Python library for interacting with Google Sheets.
- oauth2client: Provides OAuth2 authentication for Google APIs.
- Google Sheets API: Used for data storage and retrieval.

## This project combines web development with cloud-based data management, providing a seamless way to handle user information. We hope you find it both useful and impressive!

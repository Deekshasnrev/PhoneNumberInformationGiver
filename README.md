# Phone Info Application

This is a Django-based application that allows users to enter a phone number (including country code) and retrieve detailed information about the phone number such as:
- **Time Zones**: The time zone where the number is registered.
- **Carrier**: The service provider or carrier of the phone number.
- **Region**: The geographic region where the phone number is registered.

## Features

- Input a phone number with a country code (e.g., `+1234567890`).
- Get real-time details such as:
  - The **time zone** of the phone number.
  - The **carrier** providing service for the phone number.
  - The **region** where the number is registered.

## Demo

![image](https://github.com/user-attachments/assets/f1f668cf-196b-4316-a858-932ffc9e6ffb)


## Technologies Used

- **Django**: The web framework used for building the backend.
- **HTML/CSS/Bootstrap**: For the frontend design and responsiveness.
- **Phonenumbers**: A Python library used to parse, format, and validate phone numbers and obtain relevant metadata.

## Getting Started

These instructions will help you set up the project on your local machine for development and testing purposes.

### Prerequisites

- **Python 3.x**: Ensure Python is installed on your machine.
- **Django**: The project uses Django as the backend framework.
- **Phonenumbers Library**: Required for phone number parsing.

### Installation

1. **Clone the repository** to your local machine using Git:
   ```bash
   git clone https://github.com/username/repository-name.git
   cd repository-name

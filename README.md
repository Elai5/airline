# Kenya Airways Website

The **Kenya Airways Website** is a dynamic, fully responsive platform built using Django, HTML, CSS, and JavaScript. It provides users with the ability to check flights, browse an online shopping catalog across various categories such as perfumes, electronics, and travel essentials. Additionally, users can explore famous destinations for Kenya Airways flights, complete with brief descriptions of each destination. The website also features a duty-free shopping section and a dedicated contact page for user feedback.

## Features:

- **Flight Booking**: Check flights and explore popular destinations with brief descriptions (e.g., Nairobi, Paris, Johannesburg, London).
- **Online Shopping**: Shop duty-free items categorized into perfumes, electronics, and travel essentials.
- **Fully Responsive Design**: Optimized for seamless experience across all devices.
- **Bootstrap Integration**: For a clean and modern UI design on the About page.
- **Contact Page**: For user feedback and support.

## Future Enhancements:

- **Real-Time APIs**: Integrate real-time data for flight status, seat availability, and pricing.
- **Booking and Payment Integration**: Allow users to book flights directly with in-app payment options for a simulation experience.
- **2FA Login/Account Creation**: Enhance security with two-factor authentication and streamlined account creation for enhanced user experience.
- **React Integration**: Rebuild the project in React alongside Django for improved user interface and performance.

## Technologies Used:

- **Frontend**: HTML, CSS, JavaScript  
- **Backend**: Django  
- **Bootstrap**: UI enhancements on About page  
- **APIs**: For future real-time data

## How to Run Locally:

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd kenya-airways-website
Set up a virtual environment
```bash
python -m venv venv
source venv/bin/activate  # For Mac/Linux
.\venv\Scripts\activate  # For Windows
```
Install dependencies:
```bash
pip install -r requirements.txt
```
Run migrations
```bash
python manage.py migrate
```
Start server
```bash
python manage.py runserver
```
## Acknowledgements:
Special thanks to Caleb Mwema and Chris for their outstanding support and guidance throughout the development process.

## Usage:
This project serves as a simulation of a flight booking and e-commerce platform for educational purposes, allowing users to explore Django, Bootstrap, and React for enhanced web development.



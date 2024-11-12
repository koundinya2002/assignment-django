<!-- setup instructions -->
1) Setup Instructions
Follow these steps to get the project up and running locally.

(i) Clone the Repository
First, clone the repository to your local machine:
git clone https://github.com/koundinya2002/assignment-backend-django.git
cd invoice-api

(ii) Create a Virtual Environment
It’s recommended to use a virtual environment to manage dependencies:
python3 -m venv env

(iii) Activate the virtual environment:
.\env\Scripts\activate

(iv) Install Dependencies
Install the required dependencies from requirements.txt:
pip install -r requirements.txt

(v) Set Up the Database
Ensure that you have a database set up for the project. By default, the project uses SQLite, which does not require any additional configuration.
Run the migrations to set up the database:
python manage.py makemigrations
python manage.py migrate

(vi) Create a Superuser (Optional)
If you need to access the Django admin interface, create a superuser:
python manage.py createsuperuser

(vii) Run the Development Server
Run the Django development server:
python manage.py runserver
The API should now be available at http://127.0.0.1:8000/.

(viii)Test the API Endpoints
Create or Update Invoice: POST and PUT requests to /api/invoices/
View Invoice: GET request to /api/invoices/{invoice_id}/
For example, you can test the POST endpoint by using tools like Postman or cURL.



<!-- assumptions made during the implementation -->
2) Assumptions Made During Implementation

A view (invoice_detail) is created to view the json files as desired

Single Invoice Creation and Update: When creating or updating an invoice, the entire invoice data (including the nested details) is passed in the request. The invoice details are either created (in case of a new invoice) or replaced (in case of an update).
Invoice Details Overwrite:

For the PUT (update) operation, the existing invoice details are deleted and replaced with the new details provided in the request. There is no support for updating individual invoice details (e.g., modifying only one line item), unless explicitly re-sent in the payload.
Line Total Calculation:

The line_total field in InvoiceDetail is either provided directly by the user in the payload or will be calculated as quantity * price if it is not included. This is done in the serializer to ensure accuracy.
No Authentication or Permissions:

This implementation assumes that no authentication or permission systems are required. Anyone who can access the API is able to create, update, or view invoices. For a production system, proper authentication and permission classes should be added (e.g., using token-based authentication or OAuth).
Database:

By default, the project uses SQLite as the database. For production environments, you may need to configure a more robust database system (e.g., PostgreSQL, MySQL).
Invoice Numbers:

The invoice_number field is required to be unique. This assumption allows for using the invoice number as an identifier for invoices.
Simplified Validation:

Validation for the fields (such as quantity, price, and line_total) is basic. More advanced checks (e.g., validating that line_total matches the calculated value) can be added to improve data integrity.
Development Environment:

This project is intended to be run in a local development environment. For deployment in production, additional configuration (such as settings for static files, allowed hosts, and database settings) will be required.
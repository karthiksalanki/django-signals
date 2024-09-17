# django-signals

*   Question 1: Synchronous or Asynchronous Execution

    *   By default, Django signals are executed synchronously. This means that the signal handlers run in the same request/response cycle as the signal sender. 
    *   Here's a code snippet to illustrate this:
    *   ![Screenshot (18)](https://github.com/user-attachments/assets/4fcb023c-481b-4960-b3dc-33f513afef17)

*   Question 2: Thread Execution:
    *   Yes, Django signals run in the same thread as the caller.
    *   Here’s a snippet to demonstrate that:
    *   ![Screenshot (18)](https://github.com/user-attachments/assets/4fcb023c-481b-4960-b3dc-33f513afef17)
    *   ![Screenshot (19)](https://github.com/user-attachments/assets/e6b8ad89-7e12-45d7-be4c-032c9c15deb1)

*   Question 3: Database Transactions:
    *   By default, Django signals run in the same database transaction as the caller. This means that if the transaction is rolled back, the signal handlers are also rolled back( by using transaction atomic()).



*   Prerequisites:

    *   Python 3.x
    *   Django 3.x or higher
    *   Required packages listed in requirements.txt

*   Installation:

    *   Clone the repository:
        *    git clone https://github.com/karthiksalanki/django-signals

    *   Navigate to the project directory:
        *    cd project-repository

    *   Set up a virtual environment:
        *    python -m venv venv
        *    venv\Scripts\activate   # on Linux venv/bin/activate

    *   Run the development server:
        *    python manage.py runserver


    *   Test the requirements by using the APIs:
        *   Create a User:
            curl -X POST http://localhost:8000/users/ \
            -H "Content-Type: application/json" \
            -d '{
                "username":"testing_name",
                "password":"testing_name@123",
                "email":"testing_name@gmail.com"
            }'


        *   List users:
                curl http://localhost:8000/users/


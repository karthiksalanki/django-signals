# django-signals

*   Question 1: Synchronous or Asynchronous Execution

    *   By default, Django signals are executed synchronously. This means that the signal handlers run in the same request/response cycle as the signal sender. 
    *   Here's a code snippet to illustrate this:

        @receiver(post_save, sender=User)
        def send_welcome_email(sender, instance, created, **kwargs):
            try:
                with transaction.atomic():
                    print(f"Signal handler called in thread: {threading.current_thread().name}")
                    if created:
                        send_mail(
                            'Welcome to Our Platform',
                            'Thank you for signing up!',
                            settings.EMAIL_HOST_USER,
                            [instance.email],
                            fail_silently=False,
                        )
                return Response(status=status.HTTP_200_OK)
            except Exception as e:
                return Response({'Error':str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


*   Question 2: Thread Execution:
    *   Yes, Django signals run in the same thread as the caller.
    *   Here’s a snippet to demonstrate that:
        (View code snippet)
        try:
            with transaction.atomic():
                serializer = UserSerializer(data=request.data)
                if serializer.is_valid():
                    serializer.save()
                    print(f"View running in thread: {threading.current_thread().name}")
                    return Response(serializer.data, status=status.HTTP_201_CREATED)
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({'error':str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        (signal code snippet)
        try:
            with transaction.atomic():
                print(f"Signal handler called in thread: {threading.current_thread().name}")
                if created:
                    send_mail(
                        'Welcome to Our Platform',
                        'Thank you for signing up!',
                        settings.EMAIL_HOST_USER,
                        [instance.email],
                        fail_silently=False,
                    )
            return Response(status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'Error':str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


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


# SendMail
START
1. Install postgresql
2. Install rabbitmq
3. Edit settings in file SendMail\.env
4. run command: python manage.py migrate 
5. Create folder logs in project root dir
6. to start server run command: python manage.py runserver
7. in other terminal run: celery -A SendMail worker -l info -f logs/celery.log 


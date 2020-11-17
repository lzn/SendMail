# SendMail
START
1. Install postgresql
2. Install rabbitmq
3. Edit settings in .env
4. run command: python manage.py migrate 
5. to start server run command: python manage.py runserver
6. in other terminal run: celery -A SendMail worker -l info 

    
TODO
- [x] postgresl
- [x] django-environ
- [X] model + api email
- [x] email model field types to change
- [x] rabbitmq
- [x] cellery
- [x] smtp integration
- [x] cellery retry
- [ ] logger logs/email
- [x] filter 
- [ ] instruction
- [x] mailbox.sent
- [x] last_update
- [x] create date
- [x] active mailbox
- [x] reply tos
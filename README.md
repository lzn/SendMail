# SendMail
START
1. Install postgresql
2. Install rabbitmq
1. Settings in .env
1. python manage.py migrate 
2. python manage.py runserver
3. celery -A SendMail worker -l info 

    
TODO
- [x] postgresl
- [x] django-environ
- [X] model + api email
- [ ] email model field types to change
- [x] rabbitmq
- [x] cellery
- [ ] smtp integration
- [ ] cellery retry
- [ ] logger logs/email
- [ ] filter 
- [ ] instruction
- [ ] mailbox.sent
- [ ] last_update
- [ ] create date
- [x] active mailbox
# SimpleRoBo

## Installation

```
virtualenv .venv
# in linux :
source .venv/bin/activate
# in windows:
.venv\Script\activate
# after create virtualenv , install packages
pip install -r requirements.txt
```

### Run Django Project 
go to `adminrobo` folder and then run below command:

if you need admin user : 
```
python manage.py createsuperuser
```
and then :
```
python manage.py runserver 0.0.0.0:8000
```
### Rrun Script Project
go to `scripts` folder and then run below command

**Signal BUY Script**: run this command : `python run_buy.py`

**Seller Script**: run this command : `python run_seller.py`



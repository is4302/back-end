# Healthcare back-end
Backend database built using the help of Django and SQL
Group project built by IS4302 AY22/23 Sem 2 Group 16

### Introduction

A blockchain-based technique for patients and doctors to manage their medical records

### Setting up
1. Ensure that you have installed Python >= 3.9 on your local machine.
2. Install all required packages through `pip install -r requirements.txt`
3. Enter the backend folder to start the server using `cd backend` if you are not in the `/backend` folder.
4. If you are setting up for the first time, run `python manage.py makemigrations` then `python manage.py migrate`
5. To manage the accounts that are added to the database, run `python manage.py createsuperuser` and follow the instructions there.
6. To start up the server, run `python manage.py runserver`. The server will be deployed on your local host at either: `http://127.0.0.1:8000/` or `http://localhost:8000`

### Pages
Append the URL behind `http://127.0.0.1:8000/` or `http://localhost:8000`:

| Purpose                     | URL                     | Method    |Notes |
| --------------------------- |:---------------------- :| :--------:|---------------:|
| Database Administration     | `admin`                 | NA        | NA             |
| Patient Signup              | `api/signup/patient`    | POST      | NA             |
| Doctor signup               | `api/signup/doctor`     | POST      | NA             |
| Login Page                  | `api/login`             | POST      | NA             |
| Profile Page                | `api/profile`           | GET       | Requires Login |
| Appointments page           | `api/appointment`       | POST, GET | Requires Login |
| Prescription Page           | `api/prescription`      | POST, GET | Requires Login |
| List Doctors on platform    | `api/appointment/doctor`| GET       | Requires Login |
| List available Appointments | `api/list/doctor`       | GET       | Requires Login |


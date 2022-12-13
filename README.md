### Django yogacls
**In This tow apps are created **

####- admissionapi app

(admissionapi) app is mainly create api's ;
	- userloginapi
- It Checks Login and Currasponding Response return
- it takes {email,password} in POST


		- userregisterapi
- It Register or Add new user
- it takes {name,age,email,mobile,password} in POST


	- admissionapi/<int>
- It addmission in yoga class or book batch
- it takes api with < user_id> , {date,batch} in POST


	- completepaymentapi<int>/<str>
- It payment api
- it takes api with < user_id>/< date> in POST

 
Database :
![]([https://github.com/swapnilkanaki/apiyogaclass/blob/main/login.jpeg](https://github.com/swapnilkanaki/apiyogaclass/blob/master/database.jpeg))


####- yogaplatform app

(yogaplatform) use of API

#####/yogaplatform/views.py is main domain on localhost

```html
domain="http://127.0.0.1:8000/"+(api's)
```
Image:
Login:-
![](https://github.com/swapnilkanaki/apiyogaclass/blob/main/login.jpeg)

Register:-
![](https://github.com/swapnilkanaki/apiyogaclass/blob/main/register.jpeg)

addmission:-
![](https://github.com/swapnilkanaki/apiyogaclass/blob/main/addmission.jpeg)

For Createing API use Complite Django Framework
In this one App called (admissionapi) is Create All api like
    - userloginapi                        # for login Check and currasponding Response return
    - userregisterapi                     # for Register New user
    - admissionapi<int>                   # for addmission in yoga class or book batch
    - completepaymentapi<int>/<str>       # for Payment api in prograse



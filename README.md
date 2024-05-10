The prototype developed for Finvest Holdings consists of three main components that are an enrollment interface, login interface, and an access control system. First, the access control model that is used is role-based access control (RBAC) because each employee has a different role in the system. Based on their role, they have different permissions, so RBAC was the best choice. Furthermore, an access control list was used for the access control policy model instead of an access control matrix since it allows for addition of more resources and roles in the future if needed. Also, it is easier to maintain and more readable since there are already many resources in the company. Second, the hash function that I chose to employ in the password file mechanism was bcrypt due to its excellent security and moderate performance, achieving a great balance between security and performance. Finally, I ensured that each user in the system must have a unique username and a strong password that adheres to the password policy that was mentioned. 
The enrollment interface allows new users to enroll by entering their username, password, and role. The login interface ensures the users that are already enrolled into the system can log in using their username and password. As a security measure, a rate-limiting mechanism is implemented to mitigate brute-force attacks. This means the user must wait two minutes after they incorrectly input their credentials in the login interface more than five times. The access control system defines and enforces user permissions based on their role. Also, it displays the user ID, role, and access rights of the user upon successful authorization. After the user is successfully logged in, they can also enter a resource they would like to access along with an action that they want to execute on that resource (e.g., read or write), and the system shall notify them whether permission is granted or denied. 
This prototype was implemented in Python. To compile and run this program, follow these steps in the virtual machine:
1.	Extract the ZIP archive of source code to a folder of your own choice.
2.	Open the terminal (command-line interface) on your computer.
3.	Check which version of Python is installed by typing “python --version” or “python3 --version” and pressing Enter. On the virtual machine, a version of python3 was installed, so I used that command.
4.	Go to the folder (where you extracted the source code to in step 1) that contains the Python program, using the “cd enter/specified/path” command. Once you get to that folder, then cd into the “SYSC4810Assignment” folder by typing “cd SYSC4810Assignment”. Now, you shall be able to view all the source code files as well as the test files that I wrote for my program.
5.	To see which files there are in the folder, type the “ls” command, assuming you are on Linux.
6.	Run the MainMenu.py file to run the prototype by typing “python3 MainMenu.py” or “python MainMenu.py” depending on what version of python is installed on your computer. 
7.	There are also several tests written for this program. If you want to ensure all the tests pass for each test file, you can do so by running each test file individually with the command: “python -m unittest test_file_name.py” or “python3 -m unittest test_file_name.py”. Each test file in the program has “Test” used as a prefix, so you can easily tell which files are test files.


Next, I shall give a demonstration of my prototype. I shall show the enrollment of a new user and the enrolled user logging in afterwards:
1.	Run the prototype following the instructions above.
2.	Select the “Register (Enroll)” option by inputting 1.

![image](https://github.com/YashKapoor1102/Access-Control-System-for-Users/assets/78821595/142e6f20-5439-4890-988c-3d7370b1651f)
Figure 46: Operation Use Case Register 1

3.	Enter the username (The username I chose was yashk123).
4.	Enter the password (The password I chose was Awesome567#).
5.	Confirm the password (Enter the same password, so in my case, I entered Awesome567#)

![image](https://github.com/YashKapoor1102/Access-Control-System-for-Users/assets/78821595/8f0fe624-ee28-441f-8179-36f1d1635403)
Figure 47: Operation Use Case Register 2  

6.	Enter the number that corresponds to your role in the company (I chose 2, which corresponds to premium client). 

![image](https://github.com/YashKapoor1102/Access-Control-System-for-Users/assets/78821595/4de5a469-daee-4051-abf2-53f7ca09efdb)
Figure 48: Operation Use Case Register 3  

7.	Upon successful registration, a confirmation message is displayed to the user saying, “Enrolled Successfully” and the user is added to the passwd.txt file as you can see below.

![image](https://github.com/YashKapoor1102/Access-Control-System-for-Users/assets/78821595/b1b2a755-e9d5-4427-bb46-baca58d0d8d1)  
Figure 49: Operation Use Case Register Passwd.txt File

The user is then redirected to the login interface.
1.	Enter the username (I entered yashk123 because that is the username that I registered with)
2.	Enter the password (I entered Awesome567# because that is the password that I registered with). Assuming you have entered the correct credentials, access should be granted as shown below and user information shall be displayed.

![image](https://github.com/YashKapoor1102/Access-Control-System-for-Users/assets/78821595/ea5537ec-dbd9-4fcd-b1e5-d7d0bae6df9f)
Figure 50: Operation Use Case Login 1

![image](https://github.com/YashKapoor1102/Access-Control-System-for-Users/assets/78821595/20fe25db-5dbf-4341-833e-f376151bf166)
Figure 51: Operation Use Case Login 2

3.	The user is also allowed to enter the resource they would like to access and what they want to do with the resource. Then, depending on their permissions, they shall be denied or granted permission to access that resource. As you can see below, the role, premium client, has permission read on client account balance, so they are granted permission. On the other hand, even though the role, premium client, has “read” access to financial planner account details, they do not have “write” access to financial planner account details, so permission is denied. 

![image](https://github.com/YashKapoor1102/Access-Control-System-for-Users/assets/78821595/e6267b16-7a8d-4656-ab4e-43e10ab793e7)
Figure 52: Operation Use Case Login 3  

Indeed, it was exciting to work on this prototype for Finvest Holdings and provide the required functionality along with the tests. 

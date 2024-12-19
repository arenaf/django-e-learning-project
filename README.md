# Django e-learning project

This Project has been developed with ***Django***, it handles two types of users: teacher and student. The teacher can perform actions that the student cannot access, such as creating other users, adding or deleting subjects and uploading or removing files.


![home](https://github.com/user-attachments/assets/7fb24997-fa68-4421-b4d8-f30335bfef89)



## User management
A teacher can register more users.

![register-new-student](https://github.com/user-attachments/assets/cb61c597-bf55-433e-869a-329e2dfbb356)


All users can modify their profile, however the student only the password and the avatar can be changed. 

![profile](https://github.com/user-attachments/assets/6d34d95f-f8df-41e6-931a-2a16d0e1eee3)

In addition, the teacher can see their students and the subjects in which they are enrolled.
The teacher can also add or remove subjects from each of his students.

![my-students](https://github.com/user-attachments/assets/0e96e02e-f6b1-430a-aa05-33f8dfec31d4)


Django's own password management has been used, however the forms have been adapted to the application's style. 

![reset-password](https://github.com/user-attachments/assets/1e781598-9a62-4cc6-86c5-b16bdb2bb1fd)


## Subject management

Users can see the subjects in which they are enrolled.

![my-subjects](https://github.com/user-attachments/assets/54fb31fc-986c-493d-a126-4c8c6ca71157)


If the logged in user is a teacher, you can add a subject and, within each of them, the files you want.

![new-subject](https://github.com/user-attachments/assets/4dd03326-04ff-46b5-89e4-28c81959dbd7)


## File management

The teacher can create files and delete them, while the student can only download them.

If students try to access a teacher-only page, they will be redirected to the login page.


![login](https://github.com/user-attachments/assets/bcce5052-70d4-49a1-91b9-aa98ca83ed49)



## Requirements
**Pillow** for image management



# 🎓 Student Management System (Django)

A web-based Student Management System built using Django.  
This application allows users to manage student records with CRUD operations and search functionality.


## 🚀 Features

- Add Student
- View Student List
- Update Student Marks
- Delete Student
- Search Student by Name
- View Top Performer



## 🛠️ Technologies Used

- Python
- Django
- MySQL
- HTML
- CSS



## 📂 Project Structure


studentwebsite/
- │
- ├── manage.py
- ├── studentwebsite/
- ├── students/
- │ ├── models.py
- │ ├── views.py
- │ ├── urls.py
- │ ├── templates/
- │ └── static/



## ⚙️ Installation & Setup



### 1. Clone the repository


git clone https://github.com/your-username/Student-Management-System-Django.git


### 2. Navigate to project folder


cd studentwebsite


### 3. Install dependencies


pip install -r requirements.txt


### 4. Set environment variables


DB_PASSWORD=your_password
SECRET_KEY=your_secret_key


### 5. Run migrations


python manage.py makemigrations
python manage.py migrate


### 6. Start server


python manage.py runserver


### 7. Open in browser


http://127.0.0.1:8000/




## 🔍 How It Works

- Users can add and manage student records through web forms
- Data is stored in MySQL database
- Search feature filters students by name
- Topper page shows highest scoring student



## 📸 Screenshots (Optional but Recommended)

### 🏠 Home Page
![Home Page](images/Home.png)

### ➕ Add Student
![Add Student](images/Add.png)

### ✏️ Update Student
![Update](images/update.png)

### 🏆 Topper Page
![Topper](images/View_Toppers.png)

## 📸 Final Output
![Final Output](images/Final.png)



## 📌 Future Improvements

- User Authentication (Login/Register)
- Advanced Search Filte
- Dashboard with Charts
- Responsive UI Design



## 👨‍💻 Author

- C Parveen
- GitHub: https://github.com/Cparveen27

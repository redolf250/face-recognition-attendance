from utils.sql import *
from packages.pyqt import *
from packages.system import *
from packages.processing import *
from packages.ui_files import Ui_Registration

class Registration(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        self.ui_registration = Ui_Registration()
        self.ui_registration.setupUi(self)
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.ui_registration.btn_close.clicked.connect(self.close)
        self.ui_registration.btn_minimize.clicked.connect(self.showMinimized)
        self.ui_registration.frame.mouseMoveEvent = self.MoveWindow

        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(20)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(230, 230, 230, 50))
        self.ui_registration.frame.setGraphicsEffect(self.shadow)

        self.ui_registration.btn_reg_browse.clicked.connect(self.browse_files)
        self.ui_registration.btn_reg_register.clicked.connect(self.register_student)
        self.ui_registration.btn_reg_search.clicked.connect(self.search_student)
        self.ui_registration.btn_reg_delete.clicked.connect(self.delete_student)

    def load_programs(self,file_path):
        completer = QCompleter(self.read_text_file(file_path))
        completer.setCaseSensitivity(Qt.CaseInsensitive)
        self.ui_registration.reg_program.setCompleter(completer)
        
    def resource_path(self,relative_path):
        path= os.path.abspath(os.path.join(os.path.dirname(__file__),relative_path)) 
        return path

    def dump_face_encoding(self):
        encodings=list(self.get_face_encoding(self.ui_registration.reg_filename.text()))
        return self.formater(encodings)
        
    def formater(self,encoding):
        value="\'{}\'".format(encoding)
        return value

    def save_picture(self):
        path=f'C:\\ProgramData\\iFaces\\images\\{self.ui_registration.reg_reference.text()}.png'
        with open(self.ui_registration.reg_filename.text(),'rb') as file:
            img_data=file.read()
            with open(path,'wb') as out_put:
                out_put.write(img_data)
            out_put.close()
        file.close()

    def register_student(self):
        _,empty = self.validate_fields()
        db=sqlite3.connect(self.get_path())
        cursor = db.cursor()
        if len(empty)==0:
            details=self.get_field_text()
            db_results=self.query_database(f"SELECT student_reference FROM tb_students WHERE student_reference={details[0]}")
            if not db_results:
                encodings = self.dump_face_encoding()
                cursor.execute(
                    "INSERT INTO tb_students(student_reference,student_index,student_firstname,student_lastname,student_program) VALUES(?,?,?,?,?)",
                    (details[0],details[1],details[2],details[3],details[4]))
                cursor.execute(f"INSERT INTO tb_face_values(student_reference,student_face_encoding) VALUES({details[0]},{encodings})")
                db.commit()
                db.close()
                self.save_picture()
                self.ui_registration.label_notification.setText(f"Data captured successfully, for student\n with Reference: {details[0]}")
            else:
                self.ui_registration.label_notification.setText(f"Oops! data already captured for student\n with Reference: {details[0]}")
        else:
            self.ui_registration.label_notification.setText(f"Oops! some data fields are empty, provide all\ndetails to continue registration")

    def delete_student(self):
        db=sqlite3.connect(self.get_path())
        cursor = db.cursor()
        reference=self.ui_registration.reg_reference.text()
        if reference !='':
            cursor.execute(f"DELETE FROM tb_students WHERE student_reference={reference}")
            cursor.execute(f"DELETE FROM tb_face_values WHERE student_reference={reference}")
            db.commit()
            db.close()
            self.clear_ui()
            self.ui_registration.label_notification.setText(f"Record associated with student\nReference: {reference} removed!") 
        else:
            self.clear_ui()
            self.ui_registration.label_notification.setText(f"Oops! reference field can't be empty...") 
             
    def search_student(self):
        reference=self.ui_registration.reg_reference.text()
        if reference !='':
            details=self.query_database(f"SELECT * FROM tb_students WHERE student_reference={reference}")
            if details:
                self.clear_ui()
                self.update_interfaces_with_details(details)
                self.ui_registration.image.setPixmap(QPixmap.fromImage(f"C:\\ProgramData\\iFaces\\images\\{reference}.png"))
                self.ui_registration.image.setScaledContents(True)
            else:
                self.clear_ui()
                self.ui_registration.label_notification.setText(f"Oops! no record found for student\n with Reference: {reference}")
        else:
            self.ui_registration.label_notification.setText(f"Oops! reference field can't be empty...") 

    def query_database(self, query: str):
        db=sqlite3.connect(self.get_path())
        cursor = db.cursor()
        detail =cursor.execute(query)
        detail= cursor.fetchone()
        db.commit()
        cursor.close()
        db_data = []
        if detail:
            for data in detail:
                db_data.append(data)
            return db_data

    def get_face_encoding(self,image_path: str):
        image = face_recognition.load_image_file(image_path)
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        face_encoding = face_recognition.face_encodings(image)[0]
        return face_encoding

    def validate_fields(self):
        properties_list =  self.get_field_text()
        data_list = []
        empty_list = []
        for field in properties_list:
            if field:
                data_list.append(field)
            else:
               empty_list.append(field)
        return data_list,empty_list

    def get_field_text(self):
        firstname = self.ui_registration.reg_firstname.text()
        othername = self.ui_registration.reg_othername.text()
        lastname = self.ui_registration.reg_lastname.text()
        reference = self.ui_registration.reg_reference.text()
        index = self.ui_registration.reg_index.text()
        program = self.ui_registration.reg_program.text()
        image = self.ui_registration.reg_filename.text()
        return reference, index, firstname+' '+othername, lastname, program, image

    def update_interfaces_with_details(self, details):
        name = str(details[3]).split(' ')
        self.ui_registration.reg_firstname.setText(name[0])
        self.ui_registration.reg_othername.setText(name[1])
        self.ui_registration.reg_lastname.setText(details[4])
        self.ui_registration.reg_reference.setText(details[1])
        self.ui_registration.reg_index.setText(details[2])
        self.ui_registration.reg_program.setText(details[5])

    def clear_ui(self):
        self.ui_registration.reg_firstname.setText('')
        self.ui_registration.reg_othername.setText('')
        self.ui_registration.reg_lastname.setText('')
        self.ui_registration.reg_reference.setText('')
        self.ui_registration.reg_index.setText('')
        self.ui_registration.reg_program.setText('')
        self.ui_registration.reg_filename.setText('')
        self.ui_registration.image.setPixmap(u":/icons/asset/image.svg")
        self.ui_registration.image.setScaledContents(False)
        self.ui_registration.label_notification.setText("Notification")

    def browse_files(self): 
        file_type = "PNG Files(*.png);;JPG Files(*.jpg);;JPEG Files(*.jpeg)"   
        path= QFileDialog.getOpenFileName(self, "Select File","C:\\Pictures",file_type)
        if path:
            self.ui_registration.reg_filename.setText(path[0])
            self.ui_registration.image.setPixmap(QPixmap.fromImage(path[0]))
            self.ui_registration.image.setScaledContents(True)

    def read_text_file(self,path):
        with open(path,'r') as file:
            data_list = []
            programs = file.readlines()
            for program in programs:
                data_list.append(program)
            file.close()
            return data_list

    def get_path(self):
        return 'C:\\ProgramData\\iFaces\\database\\attendance_system.db'

    def MoveWindow(self, event):
        if self.isMaximized() == False:
            self.move(self.pos() + event.globalPos() - self.clickPosition)
            self.clickPosition = event.globalPos()
            event.accept()

    def mousePressEvent(self, event):
        self.clickPosition = event.globalPos()

   

    

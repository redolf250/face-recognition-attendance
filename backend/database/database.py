
from packages.pyqt import *
from packages.system import *
from packages.ui_files import *

class Database(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        self.ui = Ui_Database()
        self.ui.setupUi(self)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.ui.btn_close.clicked.connect(self.close)
        self.ui.btn_minimize.clicked.connect(self.showMinimized)
        self.ui.frame.mouseMoveEvent = self.MoveWindow 

        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(20)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(230, 230, 230, 50))
        self.ui.frame.setGraphicsEffect(self.shadow)

        self.ui.btn_add_program.clicked.connect(self.create_table)
        self.ui.btn_remove_program.clicked.connect(self.drop_table)
        self.ui.btn_refresh.clicked.connect(self.refresh)

    def MoveWindow(self, event):
        if self.isMaximized() == False:
            self.move(self.pos() + event.globalPos() - self.clickPosition)
            self.clickPosition = event.globalPos()
            event.accept()

    def mousePressEvent(self, event):
        self.clickPosition = event.globalPos()
    
    def get_path(self):
        return 'C:\\ProgramData\\iFaces\\database\\attendance_system.db'

    def create_table(self):
        data = self.ui.add_program.text()
        db = sqlite3.connect(self.get_path())
        cursor = db.cursor()
        try:
            if self.ui.add_program.text():
                year=str(dt.now().date().strftime("%Y"))
                table_name = "tb_"+data+"_"+year
                cursor.execute("CREATE TABLE IF NOT EXISTS "+table_name+"(generated_id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,student_name TEXT, student_index TEXT, student_reference TEXT, student_program TEXT,date_stamp TEXT, time_stamp TEXT)")
                db.commit()
                self.ui.label_notification.setText("Table created successfully...")
                self.refresh()
            else:
                self.ui.label_notification.setText("Oops! no table name provided...")
        except Exception as e:
            self.ui.label_notification.setText(str(e))

    def drop_table(self):
        db = sqlite3.connect(self.get_path())
        cursor = db.cursor()
        try:
            table=self.ui.database_tables.currentText()
            cursor.execute("DROP TABLE IF EXISTS "+table)
            db.commit()
            self.refresh()
            self.ui.label_notification.setText("Table removed successfully...")
        except Exception as e:
            self.ui.label_notification.setText(str(e))
        
    def combo_box(self,items:list):
      self.ui.database_tables.addItems(items)
        
    def refresh(self):
        self.ui.database_tables.clear()
        con = sqlite3.connect(self.get_path())
        cursor = con.cursor()
        sql = """SELECT name FROM sqlite_master WHERE type = 'table';"""
        my_cursor = cursor.execute(sql)
        my_cursor=my_cursor.fetchall()
        details = [v[0] for v in my_cursor if v[0] !='sqlite_sequence' and v[0] !='tb_students' and v[0] !='tb_face_values']
        self.ui.database_tables.addItems(details)
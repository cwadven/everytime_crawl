import requests
from bs4 import BeautifulSoup
import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
import re
import time
from PyQt5.QtGui import QCursor, QPixmap, QIcon
import urllib.request
from PyQt5.QtCore import Qt, QByteArray

image_base64 = b"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AABMPSgyTD0oMgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA/////////z////gP///wA///4APwAAAB4AAAAeAAAAHgAAAB4AAAAeAAAAHgAAAD4AAAA+AAAA/gAAAH4AAAB+AAAAfgAAAH4AAAB+AAAAfgAAAH4AAAB+AAAAfgAAAH4AAAB/AAAA//nnn//555//////////////////////8="

def iconFromBase64(base64):
    pixmap = QPixmap()
    pixmap.loadFromData(QByteArray.fromBase64(base64))
    icon = QIcon(pixmap)
    return icon

#UI파일 연결
#단, UI파일은 Python 코드 파일과 같은 디렉토리에 위치해야한다.
form_class = uic.loadUiType("start_gui.ui")[0]

#화면을 띄우는데 사용되는 Class 선언
def doit(_id, pw, _board_num, _board, _search):
    #로그인을 해야될 것 같음...
    login_url = 'https://everytime.kr/user/login'

    #만약 GUI 아이디 비밀번호
    user = _id
    password = pw

    session = requests.session()

    params = dict()
    params['userid'] = user
    params['password'] = password

    res = session.post(login_url, data = params) 

    soup2 = BeautifulSoup(res.text, 'html.parser') #html로 되어있는 소스코드를 박아 버린다
    script = soup2.findAll("script") #메시지창 떳을 경우 예외처리하기
    # find all alert text
    #alert = re.findall(r'(?<=alert\(\").+(?=\")', script.text) #메시지창 떳을 경우 예외처리하기

    login_test = str(script[3].text)

    gettitle=[] #질문들의 제목은 이 리스트에 집어 넣고
    getstory=[] #질문들의 내용은 이 리스트에 집어 넣을 것이다.

    if(login_test):
        return "에러 : 아이디 혹은 비밀번호가 잘못 입력하셨습니다"
    #################

    #!!!!!!!!!!!!! 중요!!!!!!!!!!쿠키가 계속 있지 않을 것 같아 그래서 나중에 cookie를 또 따로 가져와야 될것 같아. (추가:request를 할경우 쿠키 값으로 가져오지만 이유에있는 소스와 session을 이용할 경우 그럴 필요가 사라짐)

    url = 'https://api.everytime.kr/find/board/article/list'

    a=0 #초기 값 a는 0을 줘서 for 문을 돌려서 20 씩 증가 시키게 해서 질문들을 다 가져올 것이다.

    

    ##############

    id_list=[] #리스트 안에 넣어서 확인

    ############## GUI
    limit_board = _board_num

    board_category = _board

    if board_category == "자유":
        board_category = "384383"
    elif board_category == "비밀":
        board_category = "259001"
    elif board_category == "새내기":
        board_category = "385909"
    else:
        return "에러 : ???"

    word = _search

    if len(word) >= 2 and len(word) <= 5:
        pass
    else:
        return "에러 : 검색 단어는 2글자~5글자 여야 합니다"

    global count_check #전역으로 설정 GUI로 설정
    count_check = 0

    for j in range(0, limit_board, 20): #반복문을 돌려서 0에서 부터 20씩 증가 그래서 start_num은 20증가, limit_num은 20씩 증가되는거에서 20더 증가
        payload = { #id값이 맞아야되고 limit  num이랑 start num은 게시글의 처음(start) 마지막(limit) 인것 같음 moiminfo는 모르겠음 
            #f12해서 network 그리고 새로고침 그리고 xhr클릭해서 header안에 맨밑에 id를 가져옴
            'id': board_category, #이 id는 게시판을 가르키는 것같음 지금은 자유 게시판    
            'limit_num':20, #페이지의 마지막 게시글 번호 (20이 최대)
            'start_num':j, #페이지의 처음 게시글 번호
            'moiminfo':'true'
        }

        r = session.post(url, data=payload) #원래 request.post(url, data=payload, headers=headers)였는데 session을 이용해서 해더에 있는 쿠키값이 아닌 위에 로그인을 계속 유지하는 식으로 했음.

        soup = BeautifulSoup(r.text, 'html.parser') #html로 되어있는 소스코드를 박아 버린다

        
        he_coin = soup.findAll('article') #거기에 있는 article이라는 것만 리스트화 해서 he_coin안에 집어 넣는다

        for link in he_coin: #반복문을 돌려서 리스트안에 title이라는 것의 값을 가져온다.
            #print(link.get('title')) #질문 제목 [[비밀게시판에는 제목이 없음]]
            #gettitle.append(link.get('title')) #질문 제목을 리스트에 추가

            ######################## 정규화  ############## 문제 --> 남친아 남친이 이런식으로 되었을 경우 못 찾음 해결방법 : N-gram 출력 --> 해결
            if(board_category == "259001" or board_category == "385909"):
                non_split_title = link.get('text')
                title_words = link.get('text').split() # 비밀, 새내기 게시판은 text 에 있다 ㅠ
            else:
                non_split_title = link.get('title')
                title_words = link.get('title').split()
            count = 0
            for title_word in title_words: #정규화 완료
                title_words[count] = title_word.strip("?.~!;")
                count+=1

            processing = True #반복문을 돌리기!!
            
            ######## 여기서 부터는 txt에 저장하는 구간 ####

            for title_word in title_words:
                
                if(word):
                    for i in range(len(title_word) - (len(word)-1)): # ==> title_word는 찾고 싶은 글자 수 - 1 을 빼야된다 즉 2글자면 -1, 4글자면 -3 !
                        if title_word[i:len(word)+i] == word: #다른 단어도 같이 이용할 경우 or 하면 된다
                            id_list.append(link.get('id') + " : " + non_split_title)
                                    #gettitle.append(link.get('title'))
                            processing = False #남친 한번 나오면 바로 False로 만들어서 if문 안되게 만듦
                            break

                    if processing == False: #즉 한번이라도 해당 단어가 나오면 그 제목을 가진 녀석 조건 끝!!
                        break

    ############## ▼▼▼▼▼▼ 만약 3글자 단어 등 다른 단어 밑에 있는 것을 이용할 경우 이것을 전부 맨 밑으로 붙여넣기 ▼▼▼▼▼▼ ######################
            
            ###################
            count_check = count_check + 1 # %를 보여주기 위해서 count_check += 1 하면 안되더라구...
            myWindow.progressBar.setValue((count_check/limit_board)*100)
            ###################

    global how_many
    how_many = 0
    for line in id_list:
        how_many = how_many + 1
    #print(how_many, "개의 글을 발견")
    myWindow.count_label.setText(str(how_many))

    return id_list

    ############## ▲▲▲▲▲ 만약 3글자 단어 등 다른 단어 밑에 있는 것을 이용할 경우 이것을 전부 맨 밑으로 붙여넣기 ▲▲▲▲▲ ######################


            #print(link.get('text')) #질문 내용
            #getstory.append(link.get('text')) #질문 내용을 리스트에 추가
            #print("--")
        
    #print(gettitle)
    #print(getstory)

def do_comment(_id, pw, _board_id, _comment):
    #로그인을 해야될 것 같음...
    login_url = 'https://everytime.kr/user/login'

    #만약 GUI 아이디 비밀번호
    user = _id
    password = pw

    session = requests.session()

    params = dict()
    params['userid'] = user
    params['password'] = password

    res = session.post(login_url, data = params) 

    #################

    #!!!!!!!!!!!!! 중요!!!!!!!!!!쿠키가 계속 있지 않을 것 같아 그래서 나중에 cookie를 또 따로 가져와야 될것 같아. (추가:request를 할경우 쿠키 값으로 가져오지만 이유에있는 소스와 session을 이용할 경우 그럴 필요가 사라짐)

    url = 'https://api.everytime.kr/find/board/article/list'

    global count_check #전역으로 설정 GUI로 설정
    count_check = 0

    ##############
    for i in _board_id:
        data = {    #댓글 자동으로 쓰기, 즉 댓글 무한정 쓰기!!!
            'id' : i,
            'text' : _comment,
            'is_anonym' : 1,
            'success' : True
        }
        
        post_url = "https://api.everytime.kr/save/board/comment" # 댓글 쓰는 url

        r = session.post(post_url, data=data)
        r.raise_for_status()

        time.sleep(3) # 댓글 달 때 빨리 못 달음...

    ############## ▼▼▼▼▼▼ 만약 3글자 단어 등 다른 단어 밑에 있는 것을 이용할 경우 이것을 전부 맨 밑으로 붙여넣기 ▼▼▼▼▼▼ ######################
            
        ###################
        count_check = count_check + 1 # %를 보여주기 위해서 count_check += 1 하면 안되더라구...
        myWindow.progressBar.setValue((count_check/int(myWindow.count_label.text()))*100)
        
        ###################

############## ▲▲▲▲▲ 만약 3글자 단어 등 다른 단어 밑에 있는 것을 이용할 경우 이것을 전부 맨 밑으로 붙여넣기 ▲▲▲▲▲ ######################

def delete(_id, pw):
    #로그인을 해야될 것 같음...
    login_url = 'https://everytime.kr/user/login'

    #만약 GUI 아이디 비밀번호
    user = _id
    password = pw

    session = requests.session()

    params = dict()
    params['userid'] = user
    params['password'] = password

    res = session.post(login_url, data = params) 

    soup2 = BeautifulSoup(res.text, 'html.parser') #html로 되어있는 소스코드를 박아 버린다
    script = soup2.findAll("script") #메시지창 떳을 경우 예외처리하기
    # find all alert text
    #alert = re.findall(r'(?<=alert\(\").+(?=\")', script.text) #메시지창 떳을 경우 예외처리하기

    login_test = str(script[3].text)

    if(login_test):
        return "에러 : 아이디 혹은 비밀번호가 잘못 입력하셨습니다"

    #################

    #!!!!!!!!!!!!! 중요!!!!!!!!!!쿠키가 계속 있지 않을 것 같아 그래서 나중에 cookie를 또 따로 가져와야 될것 같아. (추가:request를 할경우 쿠키 값으로 가져오지만 이유에있는 소스와 session을 이용할 경우 그럴 필요가 사라짐)

    url = 'https://api.everytime.kr/find/board/article/list'

    ##############

    #만약 GUI range(0,300<-- 이거,20)
    for j in range(0, 300, 20): #반복문을 돌려서 0에서 부터 20씩 증가 그래서 start_num은 20증가, limit_num은 20씩 증가되는거에서 20더 증가
        payload = { #id값이 맞아야되고 limit  num이랑 start num은 게시글의 처음(start) 마지막(limit) 인것 같음 moiminfo는 모르겠음 
            #f12해서 network 그리고 새로고침 그리고 xhr클릭해서 header안에 맨밑에 id를 가져옴
            'id':'myarticle', #이 id는 게시판을 가르키는 것같음 지금은 자유 게시판    [[384383이 자유 게시판]]  [[259001이 비밀 게시판]]
            'limit_num':20, #페이지의 마지막 게시글 번호 (20이 최대)
            'start_num':j, #페이지의 처음 게시글 번호
            'moiminfo':'true'
        }

        r = session.post(url, data=payload) #원래 request.post(url, data=payload, headers=headers)였는데 session을 이용해서 해더에 있는 쿠키값이 아닌 위에 로그인을 계속 유지하는 식으로 했음.

        try:
            r.raise_for_status()
        except:
            return "에러 : 아이디 혹은 비밀번호가 잘못 입력하셨습니다"

        soup = BeautifulSoup(r.text, 'html.parser') #html로 되어있는 소스코드를 박아 버린다

        
        he_coin = soup.findAll('article') #거기에 있는 article이라는 것만 리스트화 해서 he_coin안에 집어 넣는다

        for link in he_coin: #반복문을 돌려서 리스트안에 title이라는 것의 값을 가져온다.
            #print(link.get('title')) #질문 제목 [[비밀게시판에는 제목이 없음]]
            #gettitle.append(link.get('title')) #질문 제목을 리스트에 추가  

            board_remove_url = "https://api.everytime.kr/remove/board/article"
            
            payload2={
                'id' : link.get('id'),
                'success' : 'true'
            }

            r = session.post(board_remove_url, data=payload2)
            r.raise_for_status()

    
    return "모든 글을 삭제 했습니다!"

def message_delete(_id, pw):
    #로그인을 해야될 것 같음...
    login_url = 'https://everytime.kr/user/login'

    #만약 GUI 아이디 비밀번호
    user = _id
    password = pw

    session = requests.session()

    params = dict()
    params['userid'] = user
    params['password'] = password

    res = session.post(login_url, data = params) 

    soup2 = BeautifulSoup(res.text, 'html.parser') #html로 되어있는 소스코드를 박아 버린다
    script = soup2.findAll("script") #메시지창 떳을 경우 예외처리하기
    # find all alert text
    #alert = re.findall(r'(?<=alert\(\").+(?=\")', script.text) #메시지창 떳을 경우 예외처리하기

    login_test = str(script[3].text)

    if(login_test):
        return "에러 : 아이디 혹은 비밀번호가 잘못 입력하셨습니다"
    #################

    #!!!!!!!!!!!!! 중요!!!!!!!!!!쿠키가 계속 있지 않을 것 같아 그래서 나중에 cookie를 또 따로 가져와야 될것 같아. (추가:request를 할경우 쿠키 값으로 가져오지만 이유에있는 소스와 session을 이용할 경우 그럴 필요가 사라짐)

    url = 'https://api.everytime.kr/find/messageBox/list'

    ##############

    data = {
        "limitNum":50,
        "isRead":"1"
    }

    r = session.post(url, data=data)

    try:
        r.raise_for_status()
    except:
        return "에러 : 아이디 혹은 비밀번호가 잘못 입력하셨습니다"

    soup = BeautifulSoup(r.text, 'html.parser') #html로 되어있는 소스코드를 박아 버린다

    messages = soup.findAll('box') #거기에 있는 article이라는 것만 리스트화 해서 he_coin안에 집어 넣는다

    message_remove_url = "https://api.everytime.kr/remove/messageBox/message/list"

    for message in messages: #반복문을 돌려서 리스트안에 title이라는 것의 값을 가져온다.

        payload2={
            'box_id' : message.get('id'),
            'success' : 'true'
        }

        r = session.post(message_remove_url, data=payload2)
        r.raise_for_status()
    
    return "모든 쪽지 삭제 완료!"

class WindowClass(QMainWindow, form_class) :
    def __init__(self) :
        super().__init__()
        self.setFixedSize(400, 333)
        self.ids = []
        self.setupUi(self)
        self.setWindowTitle("에브리타임 검색")
        self.progressBar.setValue(0)
        self.pushButton_2.setDisabled(True)

        urlString = "https://png.pngtree.com/png-vector/20190226/ourlarge/pngtree-hourglass-vector-icon-png-image_705952.jpg"
        imageFromWeb = urllib.request.urlopen(urlString).read()

        #웹에서 Load한 Image를 이용하여 QPixmap에 사진데이터를 Load하고, Label을 이용하여 화면에 표시
        self.qPixmapWebVar = QPixmap()
        self.qPixmapWebVar.loadFromData(imageFromWeb)
        self.qPixmapWebVar = self.qPixmapWebVar.scaled(100,100)
        self.lbl_picture.setPixmap(self.qPixmapWebVar)

        self.pushButton.clicked.connect(self.button1Function)
        self.pushButton_2.clicked.connect(self.button2Function)
        self.delete_all.clicked.connect(self.button3Function)
        self.delete_message.clicked.connect(self.button4Function)
        

    def button1Function(self):
        self.progressBar.setValue(0)
        self.lbl_picture.setGeometry(150, 90, 100, 100) #눈속임 주기 모래시계
        self.pushButton.setDisabled(True) #버튼 2번 이상 못 누르게

        id_list = []
        id_list = doit(self.id_edit.text(), self.pw_edit.text(), self.board_spinbox.value(), self.category_combo.currentText(), self.search_edit.text())
        self.listWidget.clear()

        if id_list[:2] == "에러":
            self.addItemText = id_list
            self.listWidget.addItem(self.addItemText)
        else:
            if id_list:
                for i in id_list:
                    self.addItemText = i
                    self.listWidget.addItem(self.addItemText)
                self.pushButton_2.setEnabled(True) #버튼 활성화 댓글이 보이면
            else:
                self.pushButton_2.setDisabled(True)
        
        self.pushButton.setEnabled(True) #버튼 2번 이상 못 누르게
        self.lbl_picture.setGeometry(150, 90, 0, 0) #눈속임 주기 모래시계
        

    def button2Function(self):
        self.setCursor(Qt.WaitCursor)
        self.pushButton_2.setCursor(QCursor(Qt.WaitCursor))

        self.lbl_picture.setGeometry(150, 90, 100, 100)
        self.ids = [] #함수로 id 값을 넣기 위해서 (리스트 넣기 위해서)
        self.progressBar.setValue(0)
        self.pushButton_2.setDisabled(True) #버튼 2번 이상 못 누르게
        self.pushButton.setDisabled(True) #버튼 2번 이상 못 누르게

        for i in range(int(self.count_label.text())):
            id_boundary = self.listWidget.item(i).text().find(" : ") #경계를 찾는다
            if id_boundary > 0:
                self.ids.append(self.listWidget.item(i).text()[:id_boundary])
            else:
                self.ids.append(self.listWidget.item(i).text())

        do_comment(self.id_edit.text(), self.pw_edit.text(), self.ids, self.comment_edit.text())

        self.lbl_picture.setGeometry(150, 90, 0, 0)

        self.setCursor(QCursor(Qt.ArrowCursor)) #커서 돌아오기
        self.pushButton_2.setCursor(QCursor(Qt.ArrowCursor))
        self.pushButton_2.setEnabled(True) #버튼 2번 이상 못 누르게
        self.pushButton.setEnabled(True) #버튼 2번 이상 못 누르게

    def button3Function(self):
        self.listWidget.clear()
        self.lbl_picture.setGeometry(150, 90, 100, 100) #눈속임 주기 모래시계

        reply = QMessageBox.question(self, '삭제 확인', '정말로 모든 글을 삭제하겠습니까?', QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

        if reply == QMessageBox.Yes:
            id_list = delete(self.id_edit.text(), self.pw_edit.text())
            self.addItemText = id_list
            self.listWidget.addItem(self.addItemText) 
        else:
            pass

        self.lbl_picture.setGeometry(150, 90, 0, 0)

    def button4Function(self):
        self.listWidget.clear()
        self.lbl_picture.setGeometry(150, 90, 100, 100) #눈속임 주기 모래시계

        reply = QMessageBox.question(self, '삭제 확인', '정말로 모든 쪽지를 삭제하겠습니까?', QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

        if reply == QMessageBox.Yes:
            id_list = message_delete(self.id_edit.text(), self.pw_edit.text())
            self.addItemText = id_list
            self.listWidget.addItem(self.addItemText) 
        else:
            pass

        self.lbl_picture.setGeometry(150, 90, 0, 0)
        


if __name__ == "__main__" :
    app = QApplication(sys.argv) 
    myWindow = WindowClass()
    icon = iconFromBase64(image_base64)
    myWindow.setWindowIcon(icon)
    myWindow.show()
    app.exec_()


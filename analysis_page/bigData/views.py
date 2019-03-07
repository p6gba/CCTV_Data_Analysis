from django.shortcuts import render
from . import models
from .apriori import main
from django.contrib import messages
from django.http import HttpResponse
from django.views import View
import pprint
import json
import datetime
dat = {'a': 'c'}

# Create your views here.
def index(request):
    return render(request, 'bigData/index.html', {})

def Category_1(request):
    if request.method == 'POST':
        receieved_from_date = request.POST['from_date']
        receieved_to_date = request.POST['to_date']
        selectRadio = request.POST['options']
        # 날짜 입력 안되면 되돌아가기
        messages = []
        messages = "구하고 싶은 구역 날짜를 입력하세요"
        if str(receieved_from_date) == ""  or str(receieved_to_date) == "":
            return render(request, 'bigData/menu1.html', {'messages' : messages})
        else:
            tempFromDate.SetFromDate = receieved_from_date
            tempToDate.SetToDate = receieved_to_date
            tempRadioValue.SetRadioValue = selectRadio
            print(selectRadio)
            DateList = []
            DateList.append(receieved_from_date)
            DateList.append(receieved_to_date)
            return render(request,'bigData/menu1-all.html', {'DateList' : DateList, 'selectRadio' : selectRadio})

    return render(request, 'bigData/menu1.html', {})


def Category_2(request):
    if request.method == 'POST':
        receieved_from_date = request.POST['from_date']
        receieved_to_date = request.POST['to_date']
        selectRadio = request.POST['options']
        # 날짜 입력 안되면 되돌아가기
        messages = []
        messages = "동선 날짜를 입력하세요"
        if str(receieved_from_date) == ""  or str(receieved_to_date) == "":
            return render(request, 'bigData/menu2.html', {'messages' : messages})
        else:
            tempFromDate2.SetFromDate2 = receieved_from_date
            tempToDate2.SetToDate2 = receieved_to_date
            tempRadioValue2.SetRadioValue2 = selectRadio
            print(selectRadio)
            DateList = []
            DateList.append(receieved_from_date)
            DateList.append(receieved_to_date)
            return render(request,'bigData/menu2-all.html', {'DateList' : DateList, 'selectRadio' : selectRadio})

    return render(request, 'bigData/menu2.html', {})

def Category_3(request):
    if request.method == 'POST':
        receieved_from_date = request.POST['from_date']
        receieved_to_date = request.POST['to_date']
        selectRadio = request.POST['options']
        # 날짜 입력 안되면 되돌아가기
        messages = []
        messages = "성별 or 날짜를 입력하세요"
        if str(receieved_from_date) == "" or str(receieved_to_date) == "":
            return render(request, 'bigData/menu3.html', {'messages': messages})
        else:
            tempFromDate3.SetFromDate3 = receieved_from_date
            tempToDate3.SetToDate3 = receieved_to_date
            tempRadioValue3.SetRadioValue3 = selectRadio
            DateList = []
            DateList.append(receieved_from_date)
            DateList.append(receieved_to_date)
            return render(request, 'bigData/menu3-all.html', {'DateList': DateList, 'selectRadio': selectRadio})

    return render(request, 'bigData/menu3.html', {})



def menu3_date(request):
    return render(request , 'bigData/menu3_date.html',{})

def menu3_gender(request):
    return render(request , 'bigData/menu3_gender.html',{})



def Category_4(request):
    return render(request, 'bigData/menu4.html', {})


def heatmap_menu1(request):
    return render(request, 'bigData/heatmap_menu1.html', {})




# 회원가입
class signUp(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'bigData/signUp.html', {})

    def post(self, request, *args, **kwargs):
        user_id = request.POST['id']
        user_pw = request.POST['pw']
        user_name = request.POST['name']
        user_email = request.POST['email']

        # MongoDB연결해서 GetMongo의 key값과 비교하여 로그인에 이용할거임


        if user_id is None or user_pw is None or user_name is None or user_email is None:
            return render(request, 'bigData/signUp.html', {})
        else:
            connection = models.Mongo()
            val = connection.Find_id_Mongo(user_id)
            if val == 1:
                return render(request, 'bigData/signUp.html', {})
            else:
                connection.Insert_info_Mongo(user_id, user_pw, user_name, user_email)
                # 이 사이에 회원가입 성공 popup message 띄우기
                return render(request, 'bigData/login.html', {})


# 로그인
class logIn(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'bigData/login.html', {})

    def post(self, request, *args, **kwargs):
        user_id = request.POST['login_id']
        user_pw = request.POST['login_pw']
        # 중요 ~! 이렇게 하면 안되고 return 넣어서 해보자
        # 아니면 HttpResponse() 데이터 자체를 하나의 변수에 넣어서 다시 비교하자
        # MongoDB연결해서 GetMongo의 key값과 비교하여 로그인에 이용할거임

        if(user_id is None or user_pw is None):
            return render(request, 'bigData/login.html', {})

        else:
            connection = models.Mongo()
            val1 = connection.Verify_id_Mongo(user_id)
            val2 = connection.Verify_id_pw_Mongo(user_id, user_pw)
        # 아이디가 존재한다면
            if val1 == 1:
            # 아이디와 비밀번호 모두 일치한다면
                if val2 == 1:
                # 성공 출력 후 로그인
                # return HttpResponse("로그인성공")
                    return render(request, 'bigData/base.html',{})
                else:

                    return render(request, 'bigData/login.html', {})
        # 입력한 아이디가 존재하지 않는다면
            else:
            # 실패 출력 후 되돌아가기

                return render(request, 'bigData/login.html', {})


class GetFromToDate:
    def __init__(self, FromDate, ToDate, RadioValue, FromDate2, ToDate2, RadioValue2, FromDate3, ToDate3, RadioValue3):
        self.__FromDate = FromDate
        self.__ToDate = ToDate
        self.__RadioValue = RadioValue
        self.__FromDate2 = FromDate2
        self.__ToDate2 = ToDate2
        self.__RadioValue2 = RadioValue2
        self.__FromDate3 = FromDate3
        self.__ToDate3 = ToDate3
        self.__RadioValue3 = RadioValue3

    # menu1
    def GetFromDate(self):
        return self.__FromDate

    def GetToDate(self):
        return self.__ToDate

    def GetRadioValue(self):
        return self.__RadioValue

    def SetFromDate(self, FromDate):
        self.__FromDate = FromDate

    def SetToDate(self, ToDate):
        self.__ToDate = ToDate

    def SetRadioValue(self, RadioValue):
        self.__RadioValue = RadioValue

    # menu2
    def GetFromDate2(self):
        return self.__FromDate2

    def GetToDate2(self):
        return self.__ToDate2

    def GetRadioValue2(self):
        return self.__RadioValue2

    def SetFromDate2(self, FromDate2):
        self.__FromDate2 = FromDate2

    def SetToDate2(self, ToDate2):
        self.__ToDate2 = ToDate2

    def SetRadioValue2(self, RadioValue2):
        self.__RadioValue2 = RadioValue2

    # menu3
    def GetFromDate3(self):
        return self.__FromDate3

    def GetToDate3(self):
        return self.__ToDate3

    def GetRadioValue3(self):
        return self.__RadioValue3

    def SetFromDate3(self, FromDate3):
        self.__FromDate3 = FromDate3

    def SetToDate3(self, ToDate3):
        self.__ToDate3 = ToDate3

    def SetRadioValue3(self, RadioValue3):
        self.__RadioValue3 = RadioValue3


class GetJson:
    def __init__(self, DataJason):
        self.__DataJson = DataJason

    @property
    def DataJson(self):
        return self.__DataJson

    @DataJson.setter
    def DataJson(self, DATAJSON):
        self.__DataJson = DATAJSON

# menu1
tempFromDate = GetFromToDate
tempToDate= GetFromToDate
tempRadioValue= GetFromToDate

# menu2
tempFromDate2 = GetFromToDate
tempToDate2= GetFromToDate
tempRadioValue2= GetFromToDate

# menu3
tempFromDate3 = GetFromToDate
tempToDate3= GetFromToDate
tempRadioValue3= GetFromToDate

tempJson = GetJson({})

# menu1
def HeatMapJSON(request):
    GetJsonHeatMap = models.Mongo()
    JsonHeatMap = list(GetJsonHeatMap.Find_HeatMap_Mongo())
    return HttpResponse(json.dumps(JsonHeatMap), content_type="application/json")

def Get_menu1_Total(request):
    receieved_from_date = tempFromDate.SetFromDate
    receieved_to_date = tempToDate.SetToDate
    RadioValue_get = tempRadioValue.SetRadioValue
    from_date = datetime.datetime.strptime(receieved_from_date,'%m/%d/%Y %H:%M %p').strftime('%Y-%m-%d-%H-%M')
    to_date = datetime.datetime.strptime(receieved_to_date,'%m/%d/%Y %H:%M %p').strftime('%Y-%m-%d-%H-%M')
    GetJsonHeatMap_Time = models.Mongo()
    JsonHeatMap_time = list(GetJsonHeatMap_Time.Find_HeatMap_Time_Mongo(from_date,to_date,RadioValue_get))
    return HttpResponse(json.dumps(JsonHeatMap_time), content_type="application/json")


# menu2
def RuleResult(request):
    dataFlow = []
    GetFlow = models.Mongo()
    dataFlow = GetFlow.Find_Flow_Mongo()
    result = []
    result = main(dataFlow)
    return HttpResponse(result, content_type="application/json")

def Get_menu2_Total(request):
    receieved_from_date = tempFromDate2.SetFromDate2
    receieved_to_date = tempToDate2.SetToDate2
    RadioValue_get = tempRadioValue2.SetRadioValue2
    print(receieved_from_date)
    print(RadioValue_get)
    from_date = datetime.datetime.strptime(receieved_from_date,'%m/%d/%Y %H:%M %p').strftime('%Y-%m-%d-%H-%M')
    to_date = datetime.datetime.strptime(receieved_to_date,'%m/%d/%Y %H:%M %p').strftime('%Y-%m-%d-%H-%M')
    GetFlow = models.Mongo()
    dataFlow = GetFlow.Find_Flow_Time_Mongo(from_date,to_date,RadioValue_get)
    result = []
    result = main(dataFlow)
    return HttpResponse(result, content_type="application/json")


# menu3
def Product(request):
    # GetProduct = models.Mongo()
    # dataProduct = GetProduct.Find_Product_Mongo()
    # result = main(dataProduct)
    # return HttpResponse(result, content_type="application/json")
    GetProduct = models.MongoProduct()
    dataProduct = list(GetProduct.Find_Product_Mongo())
    return HttpResponse(json.dumps(dataProduct), content_type="application/json")



def Get_menu3_Total(request):
    receieved_from_date = tempFromDate.SetFromDate3
    receieved_to_date = tempToDate.SetToDate3
    RadioValue_get = tempRadioValue.SetRadioValue3
    from_date = datetime.datetime.strptime(receieved_from_date,'%m/%d/%Y %H:%M %p').strftime('%Y-%m-%d-%H-%M')
    to_date = datetime.datetime.strptime(receieved_to_date,'%m/%d/%Y %H:%M %p').strftime('%Y-%m-%d-%H-%M')
    GetProduct = models.MongoProduct()
    dataProduct = list(GetProduct.Find_Product_Time_Mongo(from_date, to_date, RadioValue_get))
    return HttpResponse(json.dumps(dataProduct), content_type="application/json")

def base(request):
    # 모델의 Mongo 객체 생성
    connection = models.Mongo()
    # MongoDB Insert
    # connection.InsertMongo()
    connection.GetMongo()
    return render(request, 'bigData/base.html', {'MongoGet': connection.GetMongo()})


# 처음에 모든 데이터 보여줄때
def find_all(request):
    connection = models.MongoAll()
    val = list(connection.find_all())
    return HttpResponse(json.dumps(val), content_type="application/json")


def default_GetTotal(request):
    received_from_date = request.POST['from_date']
    received_to_date = request.POST['to_date']

    if (received_to_date is None) or (received_from_date is None):
        return render(request, 'bigData/menu3_date.html', {})
    else:
        connection = models.MongoAll()
        val = list(connection.find_date2(received_from_date, received_to_date))
        return HttpResponse(json.dumps(val), content_type="application/json")


def default_GetTotal2(request):
    received_btn_type = request.POST['btn_type']

    if received_btn_type is None:
        return render(request, 'bigData/menu3_gender.html', {})
    else:
        connection = models.MongoAll()
        val = list(connection.find_gender(received_btn_type))
        return HttpResponse(json.dumps(val), content_type="application/json")


def base(request):
    # 모델의 Mongo 객체 생성
    connection = models.Mongo()
    # MongoDB Insert
    # connection.InsertMongo()

    connection.GetMongo()
    return render(request, 'bigData/base.html', {'MongoGet': connection.GetMongo()})

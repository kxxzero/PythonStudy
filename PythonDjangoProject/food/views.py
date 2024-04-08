from django.shortcuts import render

# @Controller 역할

# Create your views here.
from django.shortcuts import render, redirect # render(forward 기법) redirect(send redirect 기법)
from select import select
from food import models
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

"""
    urls.py => Router(화면 이동)
    models.py => DAO
    views.py => Controller
        => 사용자의 요청 => 화면 이동
"""

def food_list(request):
    try:
        page=request.GET['page']
    except Exception as e:
        page="1"
    curpage=int(page)
    food_data=models.foodListData(curpage)
    totalpage=models.foodTotalPage()

    BLOCK=10
    startPage=((curpage-1)/BLOCK*BLOCK)+1
    endPage=((curpage-1)/BLOCK*BLOCK)+BLOCK

    if(endPage > totalpage):
        endPage=totalpage

    food_list=[]
    for food in food_data:
        r={"fno":food[0], "name":food[1],  "poater":food[2]}
        food_list.append(r)

    # 쿠키 읽기
    """
        request.session['id']=id
        => request.session.clear() => logout
    """
    cook_data = []
    food_cook=request.COOKIES
    if food_cook:
        for key in food_cook:
            if key.startswith('food'):
                data=request.COOKIES.get(key)
                # DB
                db_data=models.foodInfoData(int(data))
                cd={"fno":db_data[0], "name":db_data[1], "poster":db_data[2]}
                cook_data.append(cd)

    # 한 번에 모아서 한 번에 출력
    send_data={
        "curpage":curpage,
        "totalpage":totalpage,
        "startPage":startPage,
        "endPage":endPage,
        "range":range(int(startPage), int(endPage)),
        "food_list":food_list,
        "cook_data":cook_data
    }
    return render(request, 'food/list.html', send_data)

def food_before(request):
    fno=request.GET['fno']
    response=redirect(f"/food/detail/?fno={fno}")
    response.set.cookie(f"food{fno}", str(fno))
    return response

def food_detail(request):
    fno=request.GET['fno']
    #request.getParameter("fno")
    fd=models.foodDetailData(int(fno))
    detail_data={
        "fno":int(fd[0]),
        "name":fd[1],
        "poster":fd[2],
        "address":fd[3],
        "phone":fd[4],
        "type":fd[5],
        "time":fd[6],
        "theme":fd[7],
        "seat":fd[8],
        "score":float(fd[9])
    }
    return render(request, "food/detail.html", {"msg":"맛집 상세보기"})


def emp_list(request):
    emp=pd.read_csv("EMP.csv")
    colors_type=["#CCCCFF","#CCFFCC"]
    colors=sns.color_palette(colors_type)
    sns.set_palette(colors)
    sns.barplot(x='DEPTNO', y='SAL', data=emp)
    plt.savefig("C:\Users\user\PycharmProjects\PythonDjangoProject\food\static\images\emp.png")
    plt.close()

    return render(request, "emp/list.html")
from django.shortcuts import render, redirect
from django.http import JsonResponse
from web import models # models => DAO

"""
    render(request, "url", {키:값,...}) = forward
    redirect("url") = sendRedirect
    JsonResponse({}) => JSON만 전송 => Vue/React => Rest
    => CrossOrigin
"""

# Create your views here.
def main_page(request):
    try:
        # 'main/home.html'에서 출력할 데이터 전송
        recipe_data=models.mainRecipeData();
        """
            [
                (1, "title", "http")
                (1, "title", "http")
                (1, "title", "http")
                (1, "title", "http")
            ]
        """

        food_data=models.mainFoodData();
        rd=[] # recipe_data List 구조
        for r in recipe_data:
            rdata={"no":r[0], "title":r[1], "poster":r[2], "chef":r[3]}
            rd.append(rdata) # rd List에 데이터 값 저장하기

        fd=[]
        for f in food_data:
            fdata={"fno":f[0], "name":f[1], "poster":f[2]}
            fd.append(fdata)

        cdata=models.MainChefData()
        cd={
            "chef":cdata[0],
            "poster":cdata[1],
            "mc1":cdata[2],
            "mc2":cdata[3],
            "mc3":cdata[4],
            "mc7":cdata[5]
        }








            p
        }

        tdata=models.todayFoodData()
        td={}

        # 데이터를 배열로 묶어서 전송
        main_data={
            "rd":rd,
            "fd":fd
        }
    except Exception as e:
        print(e)

    return render(request, "main/home.html", main_data)
    # return JsonResponse(main_data)

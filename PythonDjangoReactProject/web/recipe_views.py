from django.http import JsonResponse
from django.shortcuts import render, redirect
from web import recipe_models

# render = forward => "경로명 / jsp명" => request로 HTML에 값을 전송

def recipe_list_view(request):
    return render(request, "recipe/list.html")

def recipe_list(request):
    try:
        page=request.GET['page']
    except Exception as e:
        page=1

    curpage=int(page)
    recipeList=recipe_models.recipeListData(curpage)
    totalpage=recipe_models.recipeTotalPage()

    BLOCK=10
    startPage=((curpage-1)/BLOCK*BLOCK)+1
    endPage=((curpage-1)/BLOCK*BLOCK)+BLOCK
    # [1] ... [10]
    if endPage > totalpage:
        endPage=totalpage

    # no, title, poster, chef
    rd=[]

    for recipe in recipeList:
        rdata={"no":recipe[0], "title":recipe[1], "poster":recipe[2], "chef":recipe[3]}
        rd.append(rdata)

        recipe_data={
            "recipe_list":rd,
            "curpage":int(curpage),
            "totalpage":int(totalpage),
            "startPage":int(startPage),
            "endPage":int(endPage)
        }

        return JsonResponse(recipe_data)


def recipe_find_view (request):
    return render(request, "recipe/find.html")

def recipe_find(request):
    try:
        page=request.GET['page']
    except Exception as e:
        page=1

    try:
        fd=request.GET['fd']
    except Exception as e:
        fd="감자"

    curpage=int(page)
    recipeList=recipe_models.recipeFindData(curpage, fd)
    totalpage=recipe_models.recipeFindTotalPage(fd)

    BLOCK=10
    startPage=((curpage-1)/BLOCK*BLOCK)+1
    endPage=((curpage-1)/BLOCK*BLOCK)+BLOCK
    # [1] ... [10]
    if endPage > totalpage:
        endPage=totalpage

    # no, title, poster, chef
    rd=[]

    for recipe in recipeList:
        rdata={"no":recipe[0], "title":recipe[1], "poster":recipe[2], "chef":recipe[3]}
        rd.append(rdata)

        recipe_data={
            "recipe_list":rd,
            "curpage":int(curpage),
            "totalpage":int(totalpage),
            "startPage":int(startPage),
            "endPage":int(endPage),
            "fd":fd
        }

        return JsonResponse(recipe_data)


def recipe_chef_view(request):
    return render(request, "recipe/chef.html")

def recipe_chef(request):
    try:
        page=request.GET['page']
    except Exception as e:
        page="1"

    curpage = int(page)
    chefList = recipe_models.recipeChefList(curpage)
    totalpage = recipe_models.recipeChefTotalPage()

    # BLOCK = 10
    # startPage = ((curpage - 1) / BLOCK * BLOCK) + 1
    # endPage = ((curpage - 1) / BLOCK * BLOCK) + BLOCK
    # # [1] ... [10]
    # if endPage > totalpage:
    #     endPage = totalpage

    # no, title, poster, chef
    cd = []

    for chef in chefList:
        cdata = {"no": chef[0], "chef": chef[1], "poster": chef[2], "mem_con1": chef[3], "mem_con2": chef[4], "mem_con3": chef[5], "mem_con7": chef[6]}
        cd.append(cdata)

        chef_data = {
            "chef_list": cd,
            "curpage": int(curpage),
            "totalpage": int(totalpage),
            # "startPage": int(startPage),
            # "endPage": int(endPage),
        }

    return JsonResponse(chef_data)


def recipeDetailView(request):
    no=request.GET['no']
    return render(request, "recipe/detail.html", no)


def recipeDetail(request):
    no=request.GET['no']
    rd=recipe_models.recipe_detail(int(no))
    re_detail={
        "no":int(rd[0]),
        "poster":rd[1],
        "chef":rd[2],
        "chef_poster":rd[3],
        "chef_profile":rd[4],
        "info1":rd[5],
        "info2":rd[6],
        "info3":rd[7],
        "content":rd[8]
    }
    stuff=rd[10].split(",")
    r_data=rd[9].split("\n")
    posters=[]
    make=[]

    for data in r_data:
        temp=data.split("^")
        make.append(temp[0])
        posters.append(temp[1])

    detail={
        "detail":re_detail
    }

    return JsonResponse(detail)

    return render()

from django.shortcuts import render, render_to_response
from django.views.decorators import csrf
import json
import datetime
with open("record.csv", "w") as f:
    f.write(",".join(["时间", "摘要", "方向", "金额", "操作人"])+"\n")


def home(request):
    return render_to_response("home.html")


def account(request):
    ctx = {}
    if request.POST:
        with open("record.csv", "a") as f:
            rst = dict(request.POST)
            print(rst)
            rst["time"] = datetime.datetime.now().strftime("%Y-%m-%d")
            f.write(",".join([rst["time"], rst["content"][0], rst["direction"][0],
                              rst["money"][0], rst["name"][0]])+"\n")
        ctx["operator"] = request.POST["name"]
    return render(request, "home.html", ctx)

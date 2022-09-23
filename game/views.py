from django.http import HttpResponse

def index(request):
    line1 = '<h1 style ="text-align: center">我爱解老师，此网站为她而做，祝她一切顺利</h1>'
    line2 = '<img src = "https://gimg2.baidu.com/image_search/src=http%3A%2F%2Fwww.comicyu.com%2FUploadFiles%2FYC%2F2009%2F9%2F200993151453.jpg&refer=http%3A%2F%2Fwww.comicyu.com&app=2002&size=f9999,10000&q=a80&n=0&g=0n&fmt=auto?sec=1666506807&t=72da36774f96e8a6f264351ebde97360", width=1000>'
    line4 = '<hr>'
    line3 = '<a href ="/play/">进入游戏界面</a>'
    return HttpResponse(line1 + line3 + line4 + line2)

def play(request):
    line1 = '<h1 style ="text-align: center">游戏界面</h1>'
    line2 = '<img src = "https://gimg2.baidu.com/image_search/src=http%3A%2F%2Fwww.comicyu.com%2FUploadFiles%2FYC%2F2009%2F9%2F200993151453.jpg&refer=http%3A%2F%2Fwww.comicyu.com&app=2002&size=f9999,10000&q=a80&n=0&g=0n&fmt=auto?sec=1666506807&t=72da36774f96e8a6f264351ebde97360", width=1000>'
    line3 = '<a href ="/">返回主界面</a>'
    return HttpResponse(line1 + line3 + line2)

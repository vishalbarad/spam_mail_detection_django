from django.shortcuts import render
import joblib

def home(request):
    return render(request,'index.html')

def spam(request):
    msg1 = request.POST['msg']
    model = joblib.load('Email_Spam_detector.pkl')
    message = model.predict([msg1])[0]
    if message==0:
        ans = "Mail sent successfully"
        return render(request,'index.html',{'ans':ans})
    else:
        ans = "Looking like, you sent a spam email!!!"
        return render(request, 'index.html', {'ans': ans})

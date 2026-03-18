from django.shortcuts import redirect, render


def register_view(request):
    return render(request, "register/register.html")


def success_view(request):
    if request.method != "POST":
        return redirect("register")

    username = request.POST.get("username", "").strip()
    password = request.POST.get("password", "")
    email = request.POST.get("email", "").strip()
    contact = request.POST.get("contact", "").strip()

    if not username:
        context = {
            "error": "Username is required.",
            "username": username,
            "password": password,
            "email": email,
            "contact": contact,
        }
        return render(request, "register/register.html", context)

    context = {
        "username": username,
        "email": email,
        "contact": contact,
    }
    return render(request, "register/success.html", context)

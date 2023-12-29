from django.urls import path

from . import views

urlpatterns = [path("index.html", views.index, name="index"),
	       path("Login.html", views.Login, name="Login"),
	       path("index.html", views.Logout, name="Logout"),
	       path("Signup.html", views.Signup, name="Signup"),
	       path("LoginAction", views.LoginAction, name="LoginAction"),
	       path("SignupAction", views.SignupAction, name="SignupAction"),	
	       path("Deposit.html", views.Deposit, name="Deposit"),
	       path("DepositAction", views.DepositAction, name="DepositAction"),
	       path("ViewBalance", views.ViewBalance, name="ViewBalance"),
	       path("SendAmount.html", views.SendAmount, name="SendAmount"),
	       path("SendAmountAction", views.SendAmountAction, name="SendAmountAction"),
]
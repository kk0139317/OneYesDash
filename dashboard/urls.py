from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views
from .views import UploadJsonView, UploadFJsonView
from .views import verify_otp  # make sure to import the view




urlpatterns = [
    path("", views.index, name="main page"),
    path('upload/', UploadJsonView.as_view(), name='upload_json'),
    path('upload_data', views.main, name='upload'),
    path('uploadf/', UploadFJsonView.as_view(), name='upload_json'),
    path('uploadvalue', views.valuation, name='upload'),
    path('charts', views.charts, name="CHarts"),
    path('finance', views.finance, name="Finance"),
    path('logoutuser', views.CustomLogout, name='logout'),
    path('logout', views.CustomLogout, name='logout'),
    path('CreateUser', views.CreateUser, name="CreateUser" ),
    path('login', views.loginuser, name="loginuser"),
    path('finance_matrics', views.Finance_Matrics, name="Finance Matrrics" ),
    path('oprational', views.Oprational, name="Oprational"),
    path('marketing', views.Marketing, name='marketing'),
    path('chatpage/<pid>', views.ChatRoom, name="CHat Room"), 
    path('chatpage', views.ChatRoomapp, name="CHat Room"), 
    path('finance_admin', views.finance_admin, name="finance_admin"), 
    path('finance_matric_admin', views.finance_matric_admin, name="finance_matric_admin"), 
    path('oprational_admin', views.Oprational_admin, name="Oprational_admin"), 
    path('marketing_admin', views.marketing_admin, name="marketing_admin"),
    path('verify-otp/', verify_otp, name='verify_otp'), 
    
    # path('profile', views.profile, name='Profile'),

]
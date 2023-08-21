from django.urls import re_path
from .views import *




urlpatterns = [
    # re_path('^validate_phone/', ValidatePhoneSendOTP.as_view()),
    # re_path('^validate_otp/', ValidateOTP.as_view()),
    re_path('^register/', Register.as_view()),
    re_path('^login/', LoginAPI.as_view()),

]
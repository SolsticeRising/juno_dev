from django.urls import path
from form_api import views

urlpatterns = [
    path('test_api', views.testview, name='Test'),
    path('save_form', views.save_form, name='Save Form'),
    path('form_list', views.form_list, name='Form List'),
    path('save_filled_form', views.save_filled_form, name='Save Filled Form'),
    path('save_field', views.save_field, name="Save Field"),
    path('field_list', views.field_list, name='Field List'),
]

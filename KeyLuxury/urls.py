from django.urls import path

from KeyLuxury.views import ( 
Welcome, Categories, Products, Form_user, LogIn , See_Products, Edit_Product, Delete_Product, Create_Products, About, BlogReview) #Search_Products) 



urlpatterns = [

    # URL HOME PAGE, (basadas den views funcionales)
    path('Welcome/', Welcome, name = "Welcome"),
    # URL PRODUCTS CATEGORIES
    path('Categories/', Categories, name = "Categories"),
    # URLS PRODUCT MANAGEMENT
    path('Products/', Products, name = "Products"),
    path('Products/<int:id>/', See_Products, name="See_Products"),
    path('Edit-Product/<int:id>/', Edit_Product, name="Edit_Products"),
    path('Delete-Product/<int:id>/', Delete_Product, name="Delete_Product"),
    path('Create-Products/', Create_Products, name="Create_Products"),
    #path('Search-Products/', Search_Products, name="Search_Products"),
    # URLS FORMS USER MANAGEMENT "SingUp" "LogIn"
    path('Form-user/', Form_user, name = "Form-user"),
    path('Log-In/', LogIn, name = "LogIn"),
    #URL FOOTER
    path('About/', About, name= "About"), 
   # URL BLOG
    path('Blog-Review/', BlogReview, name= "BlogReview"),
    ]
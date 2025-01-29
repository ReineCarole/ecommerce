from django.contrib import admin
from django.urls import path, include  
from cart.urls import urlpatterns as cart_urls  
from reviews.urls import urlpatterns as review_urls  


urlpatterns = [  
    path('api/cart/', include(cart_urls)),  
    path('api/reviews/', include(review_urls)),  

    path('admin/', admin.site.urls),
    path('api/', include('products.urls')),  # Include product URLs
    path('users/', include('users.urls')),    # Include user URLs
]

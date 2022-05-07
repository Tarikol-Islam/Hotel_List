from django.urls import path
from .views import TaskDetailView, TaskList, TaskCreate, TaskUpdate, DeleteView, CustomLoginView, TaskReorder, UserBookingsCreate, UserBookingsListView, signup
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('signup/', signup, name='signup'),

    path('', TaskList.as_view(), name='tasks'),
    path('task/<int:pk>/', TaskDetailView.as_view(), name='task'),
    path('task-create/', TaskCreate.as_view(), name='task-create'),
    path('task-update/<int:pk>/', TaskUpdate.as_view(), name='task-update'),
    path('task-delete/<int:pk>/', DeleteView.as_view(), name='task-delete'),
    #path('task-detail/<int:pk>/',TaskDetailView.as_view(),'task-detail'),
    path('task-reorder/', TaskReorder.as_view(), name='task-reorder'),
    #USer  BOOKINGS
    path('bookings/', UserBookingsListView.as_view(), name='bookings'),
    path('booking-place/<int:id>/', UserBookingsCreate ,name="book"),
]

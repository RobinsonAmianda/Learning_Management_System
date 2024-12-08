from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    # Course URLs
    path('course/list/', views.course_list, name='course_list'),
    path('course/add/', views.course_create, name='course_add'),
    path('course/edit/<int:pk>/', views.course_update, name='course_edit'),
    path('course/delete/<int:pk>/', views.course_delete, name='course_delete'),

    # path('course/details/<int:pk>/', views.CourseDetail, name='course_details'),

    # Question URLs
    path('question/list/', views.question_list, name='question_list'),
    path('question/add/', views.question_create, name='question_add'),
    path('question/edit/<int:pk>/', views.question_update, name='question_edit'),
    path('question/delete/<int:pk>/', views.question_delete, name='question_delete'),

    # Student URLs
    path('student/list/', views.student_list, name='student_list'),
    path('student/add/', views.student_create, name='student_add'),
    path('student/edit/<int:pk>/', views.student_update, name='student_edit'),
    path('student/delete/<int:pk>/', views.student_delete, name='student_delete'),
    # Tutorial URLs
    path('tutorial/list/', views.tutorial_list, name='tutorial_list'),
    path('tutorial/add/', views.tutorial_create, name='tutorial_add'),
    path('tutorial/edit/<int:pk>/', views.tutorial_update, name='tutorial_edit'),
    path('tutorial/delete/<int:pk>/', views.tutorial_delete, name='tutorial_delete'),
    # Instructor URLs
    path('instructor/list/', views.instructor_list, name='instructor_list'),
    path('instructor/add/', views.instructor_create, name='instructor_add'),
    path('instructor/edit/<int:pk>/', views.instructor_update, name='instructor_edit'),
    path('instructor/delete/<int:pk>/', views.instructor_delete, name='instructor_delete'),
    # Topic URLs
    path('topic/list/', views.topic_list, name='topic_list'),
    path('topic/add/', views.topic_create, name='topic_add'),
    path('topic/edit/<int:pk>/', views.topic_update, name='topic_edit'),
    path('topic/delete/<int:pk>/', views.topic_delete, name='topic_delete'),
    # Result URLs
    path('result/list/', views.result_list, name='result_list'),
    path('result/add/', views.result_create, name='result_add'),
    path('result/edit/<int:pk>/', views.result_update, name='result_edit'),
    path('result/delete/<int:pk>/', views.result_delete, name='result_delete'),
    path('logout/', views.logout_view, name='logout'),
    path('instructor_dashboard/', views.instructor_dashboard, name='instructor_dashboard'),
    path('student_dashboard/', views.student_dashboard, name='student_dashboard'),
    path('instructor/', views.instructor, name='instructor'),
    path('single/', views.single, name='single'),
    path('course/', views.course, name='course'),
    path('contact/', views.contact, name='contact'),
    path('blog/', views.blog, name='blog'),
    path('about/', views.about, name='about'),
    path('home/', views.home, name='home'),
    path('student_course', views.student_course, name='student_course'),
    path('student_instructor', views.student_instructor, name='student_instructor'),
    path('student_topics', views.student_topic, name='student_topics'),
    path('student_tutorial', views.student_tutorial, name='student_tutorial'),
    path('student_question', views.student_question, name='student_question'),
    path('submit_answers', views.submit_answers, name='submit_answers'),
    path('student_result', views.student_result, name='student_result'),
    path('password-reset/', auth_views.PasswordResetView.as_view(template_name='password_reset.html'),
         name='password_reset'),
    path('password-reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='password_reset_done.html'),
         name='password_reset_done'),
    path('reset/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html'),
         name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'),
         name='password_reset_complete'),
    path('user/list/', views.user_list, name='user_list'),
    path('profile_view', views.profile_view, name='profile_view'),

]

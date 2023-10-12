from django.urls import path, include
from . import views
from aplications.persona.views import EmpleadoCreateView

app_name="persona_app"

urlpatterns = [
    
    path(
        '',
        views.InicioView.as_view(),
        name='inicio'
    ),    
    path('listar-todo-empleados/',
        views.ListAllEmpleados.as_view(),
        name='empleados_all'
        ),
        
    path('listar-by-area/<shorname>/', 
        views.ListByArea.as_view(),
        name='empleados_area'
        ),
    path('buscar-empleado/', views.ListEmpleadosByKword.as_view()),
    path('listar-habilidades-empleado/', views.ListHabilidadesEmpleado.as_view()),
    path(
            'ver-empleado/<pk>/',
            views.EmpleadoDetailView.as_view(),
            name='empleado_detail'
        ),
    path('add-empleado',
        views.EmpleadoCreateView.as_view(),
        #views.EmpleadoCreateView,
        name='empleado_add'
        ),
    #xxxxx   
    

     

    #xxxxx  
    path(
        'succes',
        views.SuccesView.as_view(),
        name='correcto'
    ),
    path(
        'update-empleado/<pk>/',
        views.EmpleadoUpdateView.as_view(),
        name='modificar_empleado'
    ),
    path(
        'delete-empleado/<pk>/',
        views.EmpleadoDeleteView.as_view(),
        name='eliminar_empleado'
    ),

    path('lista-empleados-admin/', 
        views.ListaEmpleadosAdmin.as_view(),
        name='empleados_admin'
        ),
    #path('lista-empleados-admin/', 
     #   views.ListaEmpleadosAdmin,
      #  name='empleados_admin'
       # ),    
    
    
   
]
  
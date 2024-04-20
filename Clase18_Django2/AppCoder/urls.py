from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    #path("alta_curso/<nombre>", views.alta_curso),
    path("",views.inicio, name="home"),

    path("ver_cursos",views.ver_cursos, name="cursos"),
    path("ver_alumnos",views.ver_alumnos, name="alumnos"),
    path("ver_profesores",views.ver_profesores, name="profesores"),

    path("alta_curso", views.curso_formulario, name="alta_curso"),
    path("alta_alumno", views.alumno_formulario, name="alta_alumno"),
    path("alta_profesor", views.profesor_formulario, name="alta_profesor"),

    path("buscar_curso", views.buscar_curso,name="buscar_curso"),
    path("buscar_alumno", views.buscar_alumno,name="buscar_alumno"),
    path("buscar_profesor", views.buscar_profesor,name="buscar_profesor"),

    path("buscar_resultado_curso",views.buscar_resultado_curso),
    path("buscar_resultado_alumno",views.buscar_resultado_alumno),
    path("buscar_resultado_profesor",views.buscar_resultado_profesor),

    path("eliminar_curso/<int:id>",views.eliminar_curso,name="eliminar_curso"),
    path("eliminar_alumno/<int:id>",views.eliminar_alumno,name="eliminar_alumno"),
    path("eliminar_profesor/<int:id>",views.eliminar_profesor,name="eliminar_profesor"),

    path("editar_curso/<int:id>",views.editar_curso,name="editar_curso"),
    path("editar_alumno/<int:id>",views.editar_alumno,name="editar_alumno"),
    path("editar_profesor/<int:id>",views.editar_profesor,name="editar_profesor"),

    path("login", views.login_request , name="Login"),
    path("register", views.register, name="Register"),
    path("logout", LogoutView.as_view(template_name="logout.html"), name="Logout"),
    path("editarPerfil" , views.editarPerfil , name="EditarPerfil")



]
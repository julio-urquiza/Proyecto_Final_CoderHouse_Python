from django.shortcuts import render
from AppCoder.models import Curso,Alumno,Profesor,Avatar
from django.http import HttpResponse
from django.template import loader
from AppCoder.forms import Curso_formulario,Alumno_formulario,Profesor_formulario,UserEditForm,Avatar_formulario
from django.contrib.auth.forms import AuthenticationForm , UserCreationForm
from django.contrib.auth import login , authenticate
from django.contrib.auth.decorators import login_required
from django.templatetags.static import static

# Create your views here.

# def alta_curso(request,nombre):
#     curso = Curso(nombre=nombre, camada=232)
#     curso.save()
#     texto = f"se guardo en la bd el curso: {curso.nombre}{curso.camada}"
#     return HttpResponse(texto)

def inicio(request):
    if request.user.is_active:
        return render(request,"inicio.html",{"url":url_imagen(id=request.user.id)})
    
    return render(request, "home.html")


# @login_required
def ver_cursos(request):
    cursos = Curso.objects.all()

    if request.user.is_active:
        return render(request,"ver_cursos.html",{"cursos":cursos,"url":url_imagen(id=request.user.id)})
    
    return render(request,"ver_cursos.html",{"cursos":cursos})
    

def ver_alumnos(request):
    alumnos = Alumno.objects.all()

    if request.user.is_active:
        return render(request,"ver_alumnos.html",{"alumnos":alumnos,"url":url_imagen(id=request.user.id)})
    
    return render(request,"ver_alumnos.html",{"alumnos":alumnos})

def ver_profesores(request):
    profesores = Profesor.objects.all()

    if request.user.is_active:
        return render(request,"ver_profesores.html",{"profesores":profesores,"url":url_imagen(id=request.user.id)})
    
    return render(request,"ver_profesores.html",{"profesores":profesores})



def curso_formulario(request):
    if request.method == "POST":
        mi_formulario = Curso_formulario(request.POST)
    
        if mi_formulario.is_valid():
            datos = mi_formulario.cleaned_data
            curso = Curso( nombre=request.POST["nombre"] , camada=request.POST["camada"])
            curso.save()

            cursos = Curso.objects.all()
            return render(request,"ver_cursos.html",{"cursos":cursos,"url":url_imagen(id=request.user.id)})
    
    return render(request , "formulario_curso.html",{"url":url_imagen(id=request.user.id)})

def alumno_formulario(request):
    if request.method == "POST":
        mi_formulario = Alumno_formulario(request.POST)
    
        if mi_formulario.is_valid():
            datos = mi_formulario.cleaned_data
            alumno = Alumno( nombre=request.POST["nombre"] , legajo=request.POST["legajo"])
            alumno.save()

            alumnos = Alumno.objects.all()
            return render(request , "ver_alumnos.html",{"alumnos":alumnos,"url":url_imagen(id=request.user.id)})
    
    return render(request , "formulario_alumno.html",{"url":url_imagen(id=request.user.id)})

def profesor_formulario(request):
    if request.method == "POST":
        mi_formulario = Profesor_formulario(request.POST)
    
        if mi_formulario.is_valid():
            datos = mi_formulario.cleaned_data
            profesor = Profesor( nombre=request.POST["nombre"] , legajo=request.POST["legajo"])
            profesor.save()

            profesores = Profesor.objects.all()
            return render(request , "ver_profesores.html",{"profesores":profesores,"url":url_imagen(id=request.user.id)})
        
    return render(request , "formulario_profesor.html",{"url":url_imagen(id=request.user.id)})

def subir_imagen(request):
    if request.method == 'POST':
        mi_formulario = Avatar_formulario(request.POST, request.FILES)

        if mi_formulario.is_valid():
            imagen = mi_formulario.cleaned_data['imagen']
            avatar = Avatar(user=request.user,imagen=imagen)
            avatar.save()   

            return inicio(request)
        
    else:
        mi_formulario = Avatar_formulario()
    
    return render(request, 'subir_imagen.html',{'form': mi_formulario,"url":url_imagen(id=request.user.id)})



def buscar_curso(request):
    return render(request,"buscar_curso.html",{"url":url_imagen(id=request.user.id)})

def buscar_alumno(request):
    return render(request,"buscar_alumno.html",{"url":url_imagen(id=request.user.id)})

def buscar_profesor(request):
    return render(request,"buscar_profesor.html",{"url":url_imagen(id=request.user.id)})



def buscar_resultado_curso(request):
    if request.GET["nombre"]:
        nombre = request.GET["nombre"]
        cursos = Curso.objects.filter(nombre__icontains=nombre)
        return render( request, "resultado_busqueda_curso.html",{"cursos":cursos,"url":url_imagen(id=request.user.id)})
    else:
        return HttpResponse("ingrese el nombre del curso")

def buscar_resultado_alumno(request):
    if request.GET["nombre"]:
        nombre = request.GET["nombre"]
        alumnos = Alumno.objects.filter(nombre__icontains=nombre)
        return render( request, "resultado_busqueda_alumno.html",{"alumnos":alumnos,"url":url_imagen(id=request.user.id)})
    else:
        return HttpResponse("ingrese el nombre del alumno")
    
def buscar_resultado_profesor(request):
    if request.GET["nombre"]:
        nombre = request.GET["nombre"]
        profesores = Profesor.objects.filter(nombre__icontains=nombre)
        return render( request, "resultado_busqueda_profesor.html",{"profesores":profesores,"url":url_imagen(id=request.user.id)})
    else:
        return HttpResponse("ingrese el nombre del profesor")




def eliminar_curso(request,id):
    curso = Curso.objects.get(id=id)
    curso.delete()

    curso = Curso.objects.all()
    return render(request,"ver_cursos.html",{"cursos":curso,"url":url_imagen(id=request.user.id)})

def eliminar_alumno(request,id):
    alumno = Alumno.objects.get(id=id)
    alumno.delete()

    alumno = Alumno.objects.all()
    return render(request,"ver_alumnos.html",{"alumnos":alumno,"url":url_imagen(id=request.user.id)})

def eliminar_profesor(request,id):
    profesor = Profesor.objects.get(id=id)
    profesor.delete()

    profesor = Profesor.objects.all()
    return render(request,"ver_profesores.html",{"profesores":profesor,"url":url_imagen(id=request.user.id)})



def editar_curso(request,id):
    curso = Curso.objects.get(id=id)
    
    if request.method == "POST":
        mi_formulario = Curso_formulario(request.POST)

        if mi_formulario.is_valid():
            datos = mi_formulario.cleaned_data
            curso.nombre = datos["nombre"]
            curso.camada = datos["camada"]
            curso.save()

            curso = Curso.objects.all()

            return render(request,"ver_cursos.html",{"cursos":curso,"url":url_imagen(id=request.user.id)})
        
    else:
        mi_formulario = Curso_formulario(initial={"nombre":curso.nombre,"camada":curso.camada})

    return render(request,"editar_curso.html",{"mi_formulario":mi_formulario,"curso":curso,"url":url_imagen(id=request.user.id)})

def editar_alumno(request,id):
    alumno = Alumno.objects.get(id=id)
    
    if request.method == "POST":
        mi_formulario = Alumno_formulario(request.POST)

        if mi_formulario.is_valid():
            datos = mi_formulario.cleaned_data
            alumno.nombre = datos["nombre"]
            alumno.legajo = datos["legajo"]
            alumno.save()

            alumno = Alumno.objects.all()
            
            return render(request,"ver_alumnos.html",{"alumnos":alumno,"url":url_imagen(id=request.user.id)})
        
    else:
        mi_formulario = Alumno_formulario(initial={"nombre":alumno.nombre,"legajo":alumno.legajo})

    return render(request,"editar_alumno.html",{"mi_formulario":mi_formulario,"alumno":alumno,"url":url_imagen(id=request.user.id)})

def editar_profesor(request,id):
    profesor = Profesor.objects.get(id=id)
    
    if request.method == "POST":
        mi_formulario = Profesor_formulario(request.POST)

        if mi_formulario.is_valid():
            datos = mi_formulario.cleaned_data
            profesor.nombre = datos["nombre"]
            profesor.legajo = datos["legajo"]
            profesor.save()

            profesor = Profesor.objects.all()
            
            return render(request,"ver_profesores.html",{"profesores":profesor,"url":url_imagen(id=request.user.id)})
        
    else:
        mi_formulario = Profesor_formulario(initial={"nombre":profesor.nombre,"legajo":profesor.legajo})

    return render(request,"editar_profesor.html",{"mi_formulario":mi_formulario,"profesor":profesor,"url":url_imagen(id=request.user.id)})


def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request,data=request.POST)

        if form.is_valid():
            usuario = form.cleaned_data.get("username")
            contra = form.cleaned_data.get("password")

            user = authenticate(username = usuario, password = contra)

            if user is not None:
                login(request,user) 
                return inicio(request)
            
            else:
                return HttpResponse(f"Usuario no encontrado")
        else:
            return HttpResponse(f"FORM INCORRECTO {form}")

    form = AuthenticationForm()
    return render(request,"login.html",{"form":form})


def register(request):

    if request.method =="POST":
        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            return render(request, "salida.html", {"mensaje":"Usuario Creado","url":url_imagen(id=request.user.id)})

    else:
        form = UserCreationForm()

    return render(request, "registro.html", {"form":form,"url":url_imagen(id=request.user.id)})

@login_required
def editarPerfil(request):
    usuario = request.user

    if request.method == "POST":
        mi_formulario = UserEditForm(request.POST)

        if mi_formulario.is_valid():

            informacion = mi_formulario.cleaned_data
            usuario.email = informacion["email"]
            password = informacion["password1"]
            usuario.set_password(password)
            usuario.save()
            return render(request, "salida.html", {"mensaje":"Usuario Actualizado","url":url_imagen(id=request.user.id)})
            

    else:
        mi_formulario = UserEditForm(initial={'email':usuario.email})

    return render( request , "editar_perfil.html", {"miFormulario":mi_formulario,"url":url_imagen(id=request.user.id)})


def url_imagen(id):
    avatares = Avatar.objects.filter(user=id)

    if avatares.exists():
        imagen_url = avatares[0].imagen.url

    else:
        imagen_url = static('AppCoder/assets/img/usuario.png')
    
    return imagen_url


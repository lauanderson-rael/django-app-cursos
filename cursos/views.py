# aqui redireciono para templates html
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Curso
from datetime import datetime

# Create your views here.
def index(request):
   return render(request, 'index.html')

def listar_cursos(request):
   nome_filtrar = request.GET.get('nome_filtrar')
   carga_horaria = request.GET.get('carga_horaria')

   cursos = Curso.objects.all()
   if (nome_filtrar):
      cursos = cursos.filter(nome__contains=nome_filtrar)

   if (carga_horaria):
      cursos = cursos.filter(carga_horaria__gte=carga_horaria)

   return render(request, 'listar_cursos.html', {'cursos': cursos})


def criar_curso(request):
   if (request.method == 'GET'):
      status = request.GET.get('status')
      return render(request, 'criarcurso.html', {'status': status})

   elif (request.method == 'POST'):
      nomeX = request.POST.get('nome')
      carga_horariaX = request.POST.get('carga_horaria')

      curso = Curso(
         nome=nomeX,
         carga_horaria=carga_horariaX,
         data_criacao=datetime.now(),
         )
      curso.save()
      return redirect('/curso/criar_curso/?status=1')


def ver_curso(request, id):
   curso = Curso.objects.get(id=id)
   print(curso)
   return render(request, 'ver_curso.html', {'curso': curso})


def deletar_curso(request, id):
   curso = Curso.objects.get(id=id)
   # curso.delete()
   curso.ativo = False
   curso.save()
   return redirect('/curso/listar_cursos/')

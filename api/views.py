from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.shortcuts import render
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from .models import Cliente
from .models import Ticket
import json
# Create your views here.
 
class ClienteView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args , **kwargs):
        return super().dispatch(request, *args, **kwargs)
 
    def get(self, request, id=0):
        if (id>0):
            clientes=list(Cliente.objects.filter(id=id).values())
            if len(clientes)>0:
                cliente=clientes[0]
                datos = {'message': "Success", 'cliente': cliente}
            else:
                datos = {'message': "Cliente no existe..."}
            return JsonResponse(datos)
        else:
            clientes=list(Cliente.objects.values())
            if len(clientes)>0:
                datos={'message':"Success",'clientes':clientes}
            else:
                datos={'message':"cliente no existe..."}
            return JsonResponse(datos)
 
    def post(self, request):
        jd = json.loads(request.body)
        Cliente.objects.create(nombre=jd['nombre'], paterno=jd['paterno'], materno=jd['materno'], fechanac=jd['fechanac'])
        datos ={'message':"Success"}
        return JsonResponse(datos)
 
    def put(self, request, id):
        jd = json.loads(request.body)
        clientes=list(Cliente.objects.filter(id=id).values())
        if len(clientes)>0:
            cliente=Cliente.objects.get(id=id)
            cliente.nombre=jd['nombre']
            cliente.paterno=jd['paterno']
            cliente.materno=jd['materno']
            cliente.fechanac=jd['fechanac']
            cliente.save()
            datos ={'message':"Success"}
        else:
            datos = {'message': "Cliente no existe..."}
        return JsonResponse(datos)
 
    def delete(self, request, id):
        clientes=list(Cliente.objects.filter(id=id).values())
        if len(clientes) > 0:
            Cliente.objects.filter(id=id).delete()
            datos ={'message':"Success"}
        else:
            datos = {'message': "Cliente no existe..."}
        return JsonResponse(datos)
    
#--------------------------------------------------------------------------

class TicketView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args , **kwargs):
        return super().dispatch(request, *args, **kwargs)
 
    def get(self, request, id=0):
        if (id>0):
            tickets=list(Ticket.objects.filter(id=id).values())
            if len(tickets)>0:
                ticket=tickets[0]
                datos = {'message': "Success", 'ticket': ticket}
            else:
                datos = {'message': "Ticket no existe..."}
            return JsonResponse(datos)
        else:
            tickets=list(Ticket.objects.values())
            if len(tickets)>0:
                datos={'message':"Success",'tickets':tickets}
            else:
                datos={'message':"ticket no existe..."}
            return JsonResponse(datos)
 
    def post(self, request):
        jd = json.loads(request.body)
        Ticket.objects.create(numticket=jd['numticket'], servicio=jd['servicio'], fecha=jd['fecha'], idcliente=jd['idcliente'])
        datos ={'message':"Success"}
        return JsonResponse(datos)
 
    def put(self, request, id):
        jd = json.loads(request.body)
        tickets=list(Ticket.objects.filter(id=id).values())
        if len(tickets)>0:
            ticket=Ticket.objects.get(id=id)
            ticket.numticket=jd['numticket']
            ticket.servicio=jd['servicio']
            ticket.fecha=jd['fecha']
            ticket.idcliente=jd['idcliente']
            ticket.save()
            datos ={'message':"Success"}
        else:
            datos = {'message': "Ticket no existe..."}
        return JsonResponse(datos)
 
    def delete(self, request, id):
        tickets=list(Ticket.objects.filter(id=id).values())
        if len(tickets) > 0:
            Ticket.objects.filter(id=id).delete()
            datos ={'message':"Success"}
        else:
            datos = {'message': "Ticket no existe..."}
        return JsonResponse(datos)

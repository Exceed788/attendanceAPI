from django.shortcuts import render
from rest_framework import generics, mixins
# from rest_framework.authentication import (BasicAuthentication,
#                                            SessionAuthentication)
# from rest_framework.permissions import IsAuthenticated

from .models import Event, Student
from .serializers import EventSerializer, StudentSerializer


class StudentList(generics.GenericAPIView, 
                    mixins.ListModelMixin, 
                    mixins.CreateModelMixin,
                    mixins.UpdateModelMixin, 
                    mixins.RetrieveModelMixin, 
                    mixins.DestroyModelMixin):

                    
    serializer_class = StudentSerializer
    queryset = Student.objects.all()     
    lookup_field = 'id'
    # authentication_classes = [SessionAuthentication, BasicAuthentication]
    # permission_classes = [IsAuthenticated]

    
    def get(self, request, id = None):
        if id: 
            return self.retrieve(request)
        else:
            return self.list(request)

    def post (self, request): 
        return self.create(request)

class StudentDetail(mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.DestroyModelMixin,
                    generics.GenericAPIView):
                    
    serializer_class = StudentSerializer
    queryset = Student.objects.all()     
    lookup_field = 'id'
    # authentication_classes = [SessionAuthentication, BasicAuthentication]
    # permission_classes = [IsAuthenticated]


    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


class EventList(generics.GenericAPIView, 
                mixins.ListModelMixin, 
                mixins.CreateModelMixin,
                mixins.UpdateModelMixin, 
                mixins.RetrieveModelMixin, 
                mixins.DestroyModelMixin):

                    
    serializer_class = EventSerializer
    queryset = Event.objects.all()     
    lookup_field = 'id'
    # authentication_classes = [SessionAuthentication, BasicAuthentication]
    # permission_classes = [IsAuthenticated]

    
    def get(self, request, id = None):
        if id: 
            return self.retrieve(request)
        else:
            return self.list(request)

    def post (self, request): 
        return self.create(request)

class EventDetail(mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.DestroyModelMixin,
                    generics.GenericAPIView):
                    
    serializer_class = EventSerializer
    queryset = Event.objects.all()     
    lookup_field = 'id'
    # authentication_classes = [SessionAuthentication, BasicAuthentication]
    # permission_classes = [IsAuthenticated]


    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)




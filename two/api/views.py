from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Person
from .serializers import PersonSerializer


@api_view(["GET", "POST"])
def persons(request):
    if request.method == "GET":
        persons = Person.objects.all()
        serializer = PersonSerializer(persons, many=True)
        return Response(serializer.data, status.HTTP_200_OK)

    elif request.method == "POST":
        serializer = PersonSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET", "PUT", "PATCH", "DELETE"])
def person_detail(request, param):
    if param.isdigit():
        person = get_object_or_404(Person, id=param)
    else:
        person = get_object_or_404(Person, name__iexact=param)

    if request.method == "GET":
        serializer = PersonSerializer(person)
        return Response(serializer.data, status.HTTP_200_OK)

    elif request.method in ["PUT" or "PATCH"]:
        serializer = PersonSerializer(person, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == "DELETE":
        person.delete()
        return Response(
            {"message": f"Person deleted"}, status=status.HTTP_204_NO_CONTENT
        )

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
    try:
        if param.isnumeric():
            person = Person.objects.get(id=param)
        else:
            person = Person.objects.get(name__iexact=param)
    except Person.DoesNotExist:
        return Response(
            {"message": f"Person is not found"},
            status=status.HTTP_404_NOT_FOUND,
        )

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
        return Response(status=status.HTTP_204_NO_CONTENT)

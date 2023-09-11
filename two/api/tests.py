from rest_framework import status
from rest_framework.test import APITestCase


from .models import Person
from .serializers import PersonSerializer


class TestPerson(APITestCase):
    """Test Person model class"""

    def setUp(self) -> None:
        Person.objects.create(name="Mark Essien")

    def test_list_persons(self):
        """Test list all data is successful"""
        persons = Person.objects.all()
        response = self.client.get("/api")
        serializer = PersonSerializer(persons, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIsInstance(response.json(), list)

    def test_create_person(self):
        test_person2 = Person.objects.create(name="Santi Isaac")
        test_person3 = self.client.post("/api", data={"name": "Benson Isaac"})
        url = self.client.get("/api")

        self.assertEqual(str(test_person2), test_person2.name)
        self.assertEqual(len(url.data), 3)
        self.assertEqual(test_person3.status_code, status.HTTP_201_CREATED)

    def test_retrieve_person(self):
        person = Person.objects.create(name="John Doe")

        get_id = self.client.get(f"/api/{person.id}")
        self.assertEqual(get_id.status_code, status.HTTP_200_OK)
        self.assertEqual(get_id.data["name"], "John Doe")

    def test_update_person(self):
        person = Person.objects.create(name="Alice Smith")

        data = {"name": "Alice Johnson"}
        response = self.client.put(f"/api/{person.id}", data, format="json")
        self.assertEqual(response.status_code, 200)
        updated_person = Person.objects.get(id=person.id)
        self.assertEqual(updated_person.name, "Alice Johnson")

    def test_delete_person(self):
        person = Person.objects.create(name="Bob Johnson")
        
        response = self.client.delete(f"/api/{person.id}")
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        response = self.client.get(f"/api/{person.id}")
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

from ast import keyword
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from board_manager.models import Task
from django.utils import timezone

class TasksListCreateAPIViewTest(APITestCase): #nombre de la vista +test
    print("running TasksListCreateAPIViewTest")
    def setUp(self): #crea las cosas necesarias para testear la vista
        self.url = reverse('tasks') #llama al endpoint : nombre como se llame el name (url de la api)

        self.task_1 = Task.objects.create(
            task_name ='task1',
            description ='task list create APIView ',
            state ='BL',
            priority ='H',
            date_of_delivery = timezone.now(),
            comment = ''
        ) #cerrar parentesis al mismo nivel que se abre la variable

        self.task_2 = Task.objects.create(
            task_name ='prueba2',
            description ='asdfasdf',
            state ='TD',
            priority ='M',
            date_of_delivery = timezone.now(),
            comment = ''
        )

    def test_get_all_taks(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        count_db_objects = Task.objects.all().count()
        self.assertEqual(count_db_objects, 2)

    # def test_count_all_tks(self):
    #     count_db_objects = Task.objects.all().count()
    #     self.assertEqual(count_db_objects, 2)

    def test_create_task(self):
        data = {
            "task_name": "create1",
            "description": "asdfas",
            "state": "BL",
            "priority": "L",
            "date_of_delivery": "2022-02-02",
            "comment":"vacio"
        }
        response = self.client.post(self.url, data=data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        count_db_objects = Task.objects.all().count()
        self.assertEqual(count_db_objects, 3)

    def test_filter(self):
        # url_retrieve = reverse('task', args=[1])
        # print(url_retrieve)
        data = {'taskname':'',
                'state':'BL',
                'priority':'H'
        }
        response = self.client.get('/board_manager/tasks/',data=data)
        # print(response.content)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        # print(len(response.data))



class TasksRetrieveUpdateDestroyAPIViewTest(APITestCase):
    print('running TasksRetrieveUpdateDestroyAPIViewTest')
    def setUp(self):
        self.task_3 = Task.objects.create(
            task_name ='prueba2',
            description ='asdfasdf',
            state ='BL',
            priority ='L',
            date_of_delivery = timezone.now(),
            comment = ''
    ) #cerrar parentesis al mismo nivel que se abre la variable
        self.url_retrieve = reverse('task', kwargs={"pk": self.task_3.pk})

    def test_retrive(self):
        response = self.client.get(self.url_retrieve)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data.get("task_name"), "prueba2")

    def test_update(self):
        data = { "task_name": "cambio1"}
        response = self.client.patch(self.url_retrieve, data=data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(list(Task.objects.filter(pk=1).values("task_name")), [data])

    def test_delete(self):
        response = self.client.delete(self.url_retrieve)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(list(Task.objects.all()), [])

        data = { "task_name": "cambio2"}
        response = self.client.patch(self.url_retrieve, data=data)
        # print(response.status_code)


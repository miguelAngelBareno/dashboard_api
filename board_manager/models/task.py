from django.db import models

class Task(models.Model):
    
    HIGH = 'H'
    MEDIUM = 'M'
    LOW = 'L'

    BACKLOG = 'BL'
    TO_DO = 'TD'
    DOING = 'DI'
    TEST = 'TS'
    DONE = 'DN'

    Priority=[
        (HIGH, "High"),
        (MEDIUM, "Medium"),
        (LOW, "Low"),
    ]

    Status=[
        (BACKLOG, "Backlog"),
        (TO_DO, "To_Do"),
        (DOING, "Doing"),
        (TEST,"Test"),
        (DONE, "Done"),
    ]

    task_name = models.CharField(max_length=50)
    description = models.TextField(max_length=255)
    state = models.CharField(max_length=2, choices=Status, default="BACKLOG")
    priority = models.CharField(max_length=1, choices=Priority, default="LOW")
    date_of_delivery = models.DateField()
    comment = models.TextField(max_length=255, blank=True, null=True) #no obligatorio

    def __str__(self):
        return self.task_name
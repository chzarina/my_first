


from django.db import models

class Yangilik(models.Model):
    sarlavha = models.CharField(max_length=200)  # Yangilik sarlavhasi
    matn = models.TextField()                    # Yangilik matni
    sana = models.DateTimeField(auto_now_add=True)  # Avtomatik sana (yaratilgan vaqt)
    muallif = models.CharField(max_length=100, default="Admin")  # Muallif ismi

    def __str__(self):
        return self.sarlavha

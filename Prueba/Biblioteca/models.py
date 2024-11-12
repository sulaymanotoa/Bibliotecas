from django.db import models

# Create your models here.
class Libros (models.Model)
    id_libros=models.charField(max_length=10, blank=False, primary_key=True)
    nombre=models.charField(max_length=50, blank=False)
    autor=models.charField(max_length=50, blank=False)
    Fecha_creacio=models.DateField()

    def _str_(self):
        return self.nombre
    class Categorias (models.Model):
        id_categorias=models.CharField(max_length=10, blank=False, primary_key=True)
        nombre=models.charField(max_length=50, blank=False)
        descripcion=models.TextField()

     def _str_(self):
        return self.nombre
    class Ordenes(models.models)
       id_Ordenes=models.CharField(max_length=10, blank=False, primary_key=True)
       id_libros=models.ForengKey (Libros , on_delete=models.RESTRICT)
       id_categorias=models.CharField(Categorias , on_delete=models.RESTRICT)
       fecha_orden =models.DateTimeField (auto_now_add=True)
       descripcion =models.TextField()

       def _str_(self):
         return self.id_Ordenes
       
    



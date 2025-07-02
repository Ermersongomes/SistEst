from django.db import models

class Usuarios(models.Model):
    idUsuario = models.BigAutoField(primary_key=True)
    nome = models.CharField(max_length=300, null=False)
    cpf = models.CharField(max_length=15, null=False)
    num_CNH = models.CharField(max_length=15, null=True)
    validade_CNH = models.DateField(
        null=True,
        help_text="Formato <em>YYYY-MM-DD</em>"
    )
    telefone = models.CharField(max_length=15, null=False)
    email = models.CharField(max_length=300, null=True)

    class Meta:
        verbose_name_plural = "Usuários"
    
    def __str__(self):
        return f"{self.cpf} - {self.nome}"

class Carros(models.Model):
    idCarro = models.BigAutoField(primary_key=True)
    placa = models.CharField(max_length=10, null=False)
    marca = models.CharField(max_length=300, null=False)
    cor = models.CharField(max_length=50, null=False)
    fk_idUsuario = models.ForeignKey(Usuarios, on_delete=models.PROTECT)

    class Meta: 
        verbose_name_plural = "Carros"

    def __str__(self):
        return self.placa + " - " + self.marca
    

class Estacionamentos(models.Model):
    idEstacionamento = models.BigAutoField(primary_key=True)
    data_entrada = models.DateField(auto_now_add=True, null=False, help_text="Formato <em>YYYY-MM-DD</em>")
    hora_entrada = models.TimeField(auto_now_add=True, null=False, help_text="Formato <em>YYYY-MM-DD</em>")
    data_saida = models.TimeField(auto_now_add=True, null=True, help_text="Formato <em>YYYY-MM-DD</em>")
    saida_saida = models.TimeField(auto_now_add=True, null=True, help_text="Formato <em>YYYY-MM-DD</em>")
    fk_idCarro = models.ForeignKey(Carros, on_delete=models.PROTECT)

    class Meta:
        verbose_name_plural = "Estacionamentos"

    def __str__(self):
        return self.data_entrada.strftime("%d/%m/%Y") + " - " + self.hora_entrada.strftime("%H:%M:%S")
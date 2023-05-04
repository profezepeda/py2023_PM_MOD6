class Animal():
  identificacion: str = None
  es_vertebrado: bool = False
  tiene_patas: bool = False
  tiene_alas: bool = False

  def __init__(self, **kwargs):
    self.identificacion = kwargs["identificacion"] if "identificacion" in kwargs else None
    self.es_vertebrado = kwargs["es_vertebrado"] if "es_vertebrado" in kwargs else False
    self.tiene_patas = kwargs["tiene_patas"] if "tiene_patas" in kwargs else False
    self.tiene_alas = kwargs["tiene_alas"] if "tiene_alas" in kwargs else False
    pass

  def comer(self):
    print("Animal comiendo")

  def respirar(self):
    print("Animal respirando")

class Felino(Animal):

  def __init__(self, **kwargs):
    super().__init__(**kwargs)

  def comer(self, **kwargs):
    if "cantidad" in kwargs and "comida" in kwargs:
      print(f"Comiendo {kwargs['cantidad']} {kwargs['comida']}")
    elif "cantidad" not in kwargs and "comida" in kwargs:
      print(f"Comiendo {kwargs['comida']}")
    else:
      super().comer()

  def caminar(self):
    pass
  
  def cazar(self):
    pass

class Pez(Animal):
  def __init__(self):
    super().__init__(identificacion="Pez", es_vertebrado=True, tiene_patas=False, tiene_alas=False)

  def nadar(self):
    print("Nadando")

print("ANIMAL")
animal: Animal = Animal()
animal.respirar()

print("FELINO")
gato: Felino = Felino(identificacion="Gato", es_vertebrado=True, tiene_patas=True, tiene_alas=False)
gato.comer()
gato.comer(comida="Pollo")
gato.comer(comida="Jurel", cantidad=2)

pez: Pez = Pez()
print(pez.identificacion)
pez.comer()

dori: Pez = None
nemo: Pez = Pez()
dori = Pez()
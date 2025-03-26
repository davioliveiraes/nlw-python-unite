class exemplo_alguma_coisa:
   def __enter__(self):
      print("Entrou")
   
   def __exit__(self, exc_type, exc_val, exc_tb):
      print("Saiu")

with exemplo_alguma_coisa() as ola:
   print("Estou no meio")

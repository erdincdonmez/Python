import os
if os.path.exists("rehber2.txt"):
  os.remove("rehber2.txt")
else:
  print("Silmek istediğiniz dosya yok")

os.rmdir("Yeni klasör")

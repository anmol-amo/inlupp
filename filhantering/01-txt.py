# with open("data.txt", "w") as file:
#    file.write("Name, Age, City\nAnna, 25, Stockholm\n")

# with open("data.txt", "r") as file:
#    print(file.read())

with open("data.txt", "a") as file:
   file.write("Anna, 30, Göteborg\n")
   file.write("björn, 30, stockholm")

with open("data.txt", "r") as file:
   print(file.read())

   keyword = "björn"
   # vi öppnar vår data .txt fil, i läs-läge
   with open("data.txt", "r") as file:
      # vi looar igenom alla rader i filen
      for line in file:
         # vi kollar vårt nyckelord existerar per rad
         if keyword in line:
            # om vi matchar så skrivar vi resultat
            print(line.strip())
         else:
            print(f"ingen {keyword}")

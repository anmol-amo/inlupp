print("hello, world")

with open("data,txt", "w") as file:

     file.write("name,age,city\n")
     file.write("Anna,25,stockholm\n")
     file.write("Björn,30,Göteborg\n")

     # nu är filen stängd

with open("data.csv" , "a") as file:
     #men kom ihåg att lägga till n 
     file.write("Anna,25,stockholm\n")
     file.write("Björn,30,göteborg\n")
     file.write("cecelia,27,stockholm\n")
# vi kanske vill jobba rad för rad 
with open("data.csv") as file:
     #skriv ut innehållet
     for line in file:
          # strip tar bort den extra radbrytningen
          print(line.strip())
          letaEfter = "cecilia"
          if letaEfter in line:
               print(f"{letaEfter} är bäst!")
               




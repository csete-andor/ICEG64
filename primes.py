with open("primes.txt", "r") as file:
    fileContent = file.read()
fileContent = str(fileContent).replace("\n", "")
fileContent = str(fileContent).replace(" ", "")
with open("primes.txt", "w") as filer:
    filer.write(fileContent)
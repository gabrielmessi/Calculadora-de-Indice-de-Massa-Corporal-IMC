def calcular_imc():

  while True:
    print("\n=== Menu ===")
    print("1. Calcular IMC.")
    print("2. Sair.\n")
    
    try:
      
      escolha = int(input("Digite o número que corresponde a sua escolha: "))
      if escolha == 2:
        print("\nEncerrando programa...")
        break
      elif escolha == 1:
        sexo = input("\nMasculino/Feminino: ")
        if sexo.lower() == "masculino" or sexo.lower() == "feminino":
          kg = float(input("Peso: "))
          a = kg
          altura = float(input("Comprimento: "))
          b = altura
        else:
          print("Sexo inválido.")
          continue
      else:
        print("Opção inválida.")
        continue

    except ValueError:
      print("Apenas valores numéricos.")
      continue

    imc = a / b ** 2
    print(f"\nIMC = {imc:.2f}")
    if imc < 18.5:
      print("Baixo peso.")
    elif imc <= 24.9:
      print("Peso adequado.")
    elif imc <= 29.9:
      print("Sobrepeso.")
    elif imc <= 34.9:
      print("Obesidade grau 1.")
    elif imc <= 39.9:
      print("Obesidade grau 2.")
    else:
      print("Obesidade grau 3.")
calcular_imc()

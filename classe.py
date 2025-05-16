class ComicShop:
    def __init__(self):
        self.comics = []
        self.total_de_hqs = 0

    def add_hq(self):
        titulo = input("Digite o titulo da HQ: ")
        autor = input("Digite o nome do autor da HQ: ")
        preco = float(input("Digite o preço da HQ: "))
        quantidade_estoque = int(input("Digite a quantidade de unidades da HQ que deseja adicionar: "))
        self.comics.append({"Titulo": titulo, "Autor": autor, "Preço": preco, "Quantidade em estoque": quantidade_estoque})
        print("\033[97mHQ adicionada com sucesso\033[0m")

    def deletar_hq(self):
        titulo = input("Digte o titulo da HQ que deseja deletar: ")
        for comic in self.comics:
            if comic["Titulo"] == titulo:
                self.comics.remove(comic)
                print("HQ excluida com sucesso")
                return
        print("HQ nao encontrada no estoque ou dados incorretos, tente novamente")

    def listar_hqs(self):
        print("Lista de HQs disponiveis no estoque:\n")
        for comic in self.comics:
            print(f"HQ: \033[1;33m{comic['Titulo']}\033[0m ({comic['Quantidade em estoque']} unidades) - Autor: {comic['Autor']} - Preço: R$ {comic['Preço']:.2f}")


    def calcular_valor_da_venda(self):
        carrinho = []

        while True:
            titulo = input("Digite o titulo da HQ que vai ser realizada a venda: ")
            if titulo.lower() == "sair":
                break

            for comic in self.comics:
                if comic["Titulo"] == titulo:
                    try:
                        quantidade_comprada = int(input(f"Digite a quantidade de unidades de '{titulo}' que deseja realizar acomprar: "))
                    except ValueError:
                        print("Erro: Quantidade de unidades inválida. Tente novamente.")
                        continue

                    if quantidade_comprada <= comic["Quantidade em estoque"]:
                        valor_total = comic["Preço"] * quantidade_comprada
                        print(f"Valor total da compra: R$ {valor_total:.2f}")
                        carrinho.append({
                            "Titulo": titulo,
                            "Quantidade": quantidade_comprada,
                            "Preço": valor_total
                        })
                        print("HQ adicionada ao carrinho!")
                    else:
                        print("Quantidade de unidades solicitadas é maior que a quantidade em estoque.")
                    break 
            else:
                print("HQ nao encontrada no estoque ou dados incorretos, tente novamente")

        print("\nCarrinho:")
        for item in carrinho:
            print(f"{item['Titulo']} x {item['Quantidade']} = R$ {item['Preço']:.2f}")

        resposta = input("Deseja finalizar a compra? (s/n): ")
        if resposta.lower() == "s":
            print("Compra efetuada com sucesso")
            for item in carrinho:
                for comic in self.comics:
                    if comic["Titulo"] == item["Titulo"]:
                        comic["Quantidade em estoque"] -= item["Quantidade"]
                        self.total_de_hqs += comic["Preço"] * item["Quantidade"]

            print(f"Total da compra: R$ {self.total_de_hqs:.2f}")
            carrinho = []

        elif resposta.lower() == "n":
            print("Compra cancelada!")
            carrinho = []

        else:
            print("Opção inválida, tente novamente")

    
    def menu(self):
        while True:
              
            print("\033[1;34m" + "Bem-vindo ao Sistema de Gerenciamento de HQs da Comic Shop!" + "\033[0m")
            print("\033[1;32m" + "Escolha uma opção:" + "\033[0m")
            print("\033[1;31m" + "1. Adicionar HQ" + "\033[0m")
            print("\033[1;31m" + "2. Deletar HQ" + "\033[0m")
            print("\033[1;31m" + "3. Listar HQs" + "\033[0m")
            print("\033[1;31m" + "4. Calcular Valor da Venda" + "\033[0m")
            print("\033[1;31m" + "5. Sair" + "\033[0m")

            opcao = input("Escolha uma opcao: ")

            if opcao == "1":
                self.add_hq()
            elif opcao == "2":
                self.deletar_hq()
            elif opcao == "3":
                self.listar_hqs()
            elif opcao == "4":
                self.calcular_valor_da_venda()
            elif opcao == "5":
                break
            else:
                print("Opcao invalida, tente novamente")

                

    

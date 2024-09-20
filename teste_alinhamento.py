import tkinter as tk

# Funções fictícias para os botões (substitua pelas suas funções reais)
def registrar_veiculo():
    print("Registrar Veículo")

def atualizar_lista_veiculos():
    print("Exibir Veículos")

# Função para abrir a janela de veículos
def abrir_janela_veiculos():
    janela_veiculos = tk.Toplevel(root)
    janela_veiculos.title("Gerenciamento de Veículos")
    janela_veiculos.geometry("1300x900")
    janela_veiculos.configure(bg='#d0f3e1')

    label_veiculo = tk.Label(janela_veiculos, text="Gerenciamento de Veículos", font=("Arial", 16, "bold"), bg='#d0f3e1')
    label_veiculo.pack(pady=10)

    # Frame para os botões (para colocá-los lado a lado)
    frame_botoes = tk.Frame(janela_veiculos, bg='#d0f3e1')
    frame_botoes.pack(pady=10)

    # Botões lado a lado
    btn_registrar_veiculo = tk.Button(frame_botoes, text="Registrar Veículo", font=("Arial", 12), command=registrar_veiculo)
    btn_registrar_veiculo.pack(side='left', padx=10)

    btn_exibir_veiculos = tk.Button(frame_botoes, text="Exibir Veículos", font=("Arial", 12), command=atualizar_lista_veiculos)
    btn_exibir_veiculos.pack(side='left', padx=10)

# Configurações da janela principal
root = tk.Tk()
root.geometry("1300x900")

# Botão na janela principal para abrir a janela de veículos
btn_abrir_veiculos = tk.Button(root, text="Gerenciamento de Veículos", font=("Arial", 12), command=abrir_janela_veiculos)
btn_abrir_veiculos.pack(pady=20)

root.mainloop()

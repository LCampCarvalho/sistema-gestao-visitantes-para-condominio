import tkinter as tk
from tkinter import messagebox
from database import create_db, add_visitante, add_veiculo, get_visitantes, get_veiculos, registrar_saida_visitante, \
    registrar_saida_veiculo, get_visitantes_presentes, get_veiculos_presentes, excluir_registro_visitante, excluir_registro_veiculo
from mailer import send_notification
from datetime import datetime

# Função para verificar CPF válido (11 dígitos numéricos)
def validar_cpf(cpf):
    return cpf.isdigit() and len(cpf) == 11


# Função para adicionar visitante
def registrar_visitante():
    nome = entry_nome.get()
    cpf = entry_cpf.get()
    apartamento = entry_apartamento.get()
    data_visita = datetime.now().strftime("%d/%m/%Y")
    hora_entrada = datetime.now().strftime("%H:%M")

    if nome and validar_cpf(cpf):
        add_visitante(nome, cpf, apartamento, data_visita, hora_entrada)
        send_notification('condominio.solimar@gmail.com', 'Novo Visitante', f'O visitante {nome} foi registrado.')
        messagebox.showinfo("Sucesso", "Visitante registrado com sucesso.")
        entry_nome.delete(0, tk.END)
        entry_cpf.delete(0, tk.END)
        entry_apartamento.delete(0, tk.END)
        exibir_visitantes()
    else:
        messagebox.showwarning("Atenção", "Por favor, insira um CPF válido.")


# Função para exibir visitantes
def exibir_visitantes():
    visitantes = get_visitantes()
    lista_visitantes.delete(0, tk.END)
    for visitante in visitantes:
        lista_visitantes.insert(tk.END,
                                f"Nome: {visitante[1]}, CPF: {visitante[2]}, Apto: {visitante[3]}, Entrada: {visitante[4]}, Saída: {visitante[5]}")


# Função para adicionar veículo
def registrar_veiculo():
    placa = entry_placa.get()
    modelo = entry_modelo.get()
    cor = entry_cor.get()
    apartamento = entry_apartamento_veiculo.get()
    hora_entrada = datetime.now().strftime("%H:%M")

    if placa and modelo and cor:
        add_veiculo(placa, modelo, cor, apartamento, hora_entrada)
        send_notification('condominio.solimar@gmail.com', 'Novo Veículo', f'O veículo {placa} foi registrado.')
        messagebox.showinfo("Sucesso", "Veículo registrado com sucesso.")
        entry_placa.delete(0, tk.END)
        entry_modelo.delete(0, tk.END)
        entry_cor.delete(0, tk.END)
        entry_apartamento_veiculo.delete(0, tk.END)
        atualizar_lista_veiculos()
    else:
        messagebox.showwarning("Atenção", "Por favor, preencha todos os campos.")


# Função para registrar a saída de um visitante
def registrar_saida_visitante_interface():
    cpf = entry_cpf_saida.get()
    hora_saida = datetime.now().strftime("%H:%M")
    registrar_saida_visitante(cpf, hora_saida)
    messagebox.showinfo("Sucesso", "Saída registrada com sucesso.")
    exibir_visitantes()


# Função para registrar a saída de um veículo
def registrar_saida_veiculo_interface():
    placa = entry_placa_saida.get()
    hora_saida = datetime.now().strftime("%H:%M")
    registrar_saida_veiculo(placa, hora_saida)
    messagebox.showinfo("Sucesso", "Saída registrada com sucesso.")
    atualizar_lista_veiculos()


def atualizar_lista_veiculos():
    veiculos = get_veiculos()
    lista_veiculos.delete(0, tk.END)
    for veiculo in veiculos:
        lista_veiculos.insert(tk.END,
                              f"Placa: {veiculo[1]}, Modelo: {veiculo[2]}, Cor: {veiculo[3]}, Apartamento: {veiculo[4]}, Entrada: {veiculo[5]}")


# Função para consultar visitantes presentes
def consultar_visitantes_presentes():
    visitantes = get_visitantes_presentes()
    lista_visitantes.delete(0, tk.END)
    for visitante in visitantes:
        lista_visitantes.insert(tk.END, f"Nome: {visitante[1]}, CPF: {visitante[2]}, Entrada: {visitante[4]}")


# Função para consultar veículos presentes
def consultar_veiculos_presentes():
    veiculos = get_veiculos_presentes()
    lista_veiculos.delete(0, tk.END)
    for veiculo in veiculos:
        lista_veiculos.insert(tk.END, f"Placa: {veiculo[1]}, Modelo: {veiculo[2]}, Entrada: {veiculo[4]}")

# Função para excluir um visitante
def excluir_visitante():
    cpf = entry_cpf_exclusao.get()
    if cpf and validar_cpf(cpf):
        # Chama a função de exclusão do banco de dados
        excluir_registro_visitante(cpf)
        messagebox.showinfo("Sucesso", "Visitante excluído com sucesso.")
        exibir_visitantes()
    else:
        messagebox.showwarning("Atenção", "Por favor, insira um CPF válido.")

# Função para excluir um veículo
def excluir_veiculo():
    placa = entry_placa_exclusao.get()
    if placa:
        # Chama a função de exclusão do banco de dados
        excluir_registro_veiculo(placa)
        messagebox.showinfo("Sucesso", "Veículo excluído com sucesso.")
        atualizar_lista_veiculos()
    else:
        messagebox.showwarning("Atenção", "Por favor, insira uma placa válida.")

def abrir_controle_visitantes():
    janela_visitantes = tk.Toplevel(root)
    janela_visitantes.title("Gestão de Visitantes")
    janela_visitantes.geometry("1300x900")
    janela_visitantes.configure(bg='#ceddf2')

    label_visitante = tk.Label(janela_visitantes, text="Gerenciamento de visitantes", font=fonte_titulo, bg='#ceddf2')
    label_visitante.pack(pady=10)

    frame_nome_do_visitante = tk.Frame(janela_visitantes, bg='#ceddf2')
    frame_nome_do_visitante.pack()

    tk.Label(frame_nome_do_visitante, width=20, text="Nome do visitante:", font=fonte_padrao, bg='#ceddf2').pack(anchor=tk.W, padx=5, side='left')
    global entry_nome
    entry_nome = tk.Entry( frame_nome_do_visitante, width=100, font=fonte_padrao)
    entry_nome.pack(padx=15, pady=10)

    frame_cpf_do_visitante = tk.Frame(janela_visitantes, bg='#ceddf2')
    frame_cpf_do_visitante.pack()

    tk.Label(frame_cpf_do_visitante, width=20, text="CPF do visitante:", font=fonte_padrao, bg='#ceddf2').pack(anchor=tk.W, padx=10, side='left')
    global entry_cpf
    entry_cpf = tk.Entry(frame_cpf_do_visitante, width=100, font=fonte_padrao)
    entry_cpf.pack(padx=10, pady=5)

    frame_apartamento = tk.Frame(janela_visitantes, bg='#ceddf2')
    frame_apartamento.pack()

    tk.Label(frame_apartamento, width=20, text="Apartamento:", font=fonte_padrao, bg='#ceddf2').pack(anchor=tk.W, padx=10, side='left')
    global entry_apartamento
    entry_apartamento = tk.Entry(frame_apartamento, width=100, font=fonte_padrao)
    entry_apartamento.pack(padx=10, pady=5)

    # Botões registrar e exibir

    frame_btn_registrar_exibir_visitante = tk.Frame(janela_visitantes, bg='#ceddf2')
    frame_btn_registrar_exibir_visitante.pack(pady=10)

    btn_registrar_visitante = tk.Button(frame_btn_registrar_exibir_visitante, text="Registrar Visitante", font=fonte_padrao,bg='#659962',
                                        command=registrar_visitante)
    btn_registrar_visitante.pack(side='left', pady=10, padx=10)

    btn_exibir_visitantes = tk.Button(frame_btn_registrar_exibir_visitante, text="Exibir registro dos visitantes", font=fonte_padrao, bg='#f4d451', command=exibir_visitantes)
    btn_exibir_visitantes.pack(side='left', pady=5, padx=10)

    # Campo para CPF de exclusão

    frame_cpf_para_exclusao = tk.Frame(janela_visitantes, bg='#ceddf2')
    frame_cpf_para_exclusao.pack()

    tk.Label(frame_cpf_para_exclusao, width=20, text="CPF para Exclusão:", font=fonte_padrao, bg='#ceddf2').pack(anchor=tk.W, padx=10,side='left')
    global entry_cpf_exclusao
    entry_cpf_exclusao = tk.Entry(frame_cpf_para_exclusao, width=100, font=fonte_padrao)
    entry_cpf_exclusao.pack(padx=10, pady=5)

    # Botão para excluir visitante

    btn_excluir_visitante = tk.Button(janela_visitantes, text="Excluir Visitante", font=fonte_padrao, bg='#db1640',
                                      command=excluir_visitante)
    btn_excluir_visitante.pack(padx=10, pady=5)

    # Lista de visitantes
    frame_lista_visitante = tk.Frame(janela_visitantes, bg='#ceddf2')
    frame_lista_visitante .pack()

    tk.Label(frame_lista_visitante, width=20, text="Lista de visitantes:", font=fonte_padrao, bg='#ceddf2').pack(
        anchor=tk.W, padx=10, side='left')
    global lista_visitantes
    lista_visitantes = tk.Listbox(frame_lista_visitante, width=100, height=15, font=fonte_padrao)
    lista_visitantes.pack(side='left', padx=10, pady=10)

    frame_cpf_para_saida = tk.Frame(janela_visitantes, bg='#ceddf2')
    frame_cpf_para_saida.pack()

    tk.Label(frame_cpf_para_saida,width=20, text="CPF para Saída:", font=fonte_padrao, bg='#ceddf2').pack(anchor=tk.W, padx=10,side='left')
    global entry_cpf_saida
    entry_cpf_saida = tk.Entry(frame_cpf_para_saida, width=100, font=fonte_padrao)
    entry_cpf_saida.pack(padx=10, pady=5)

    # lado a lado botões resgistrar saída / consultar visitantes presentes
    frame_btn_registrar_consultar_visitante = tk.Frame(janela_visitantes, bg='#ceddf2')
    frame_btn_registrar_consultar_visitante.pack(pady=10)

    btn_registrar_saida_visitante = tk.Button(frame_btn_registrar_consultar_visitante, text="Registrar Saída Visitante", font=fonte_padrao, bg='#659962',
                                              command=registrar_saida_visitante_interface)
    btn_registrar_saida_visitante.pack(side='left', pady=10, padx=10)

    btn_consultar_visitantes_presentes = tk.Button(frame_btn_registrar_consultar_visitante, text="Consultar Visitantes Presentes",
                                                   font=fonte_padrao, bg='#f4d451', command=consultar_visitantes_presentes)
    btn_consultar_visitantes_presentes.pack(side='left', pady=5, padx=10)


def abrir_controle_veiculos():
    janela_veiculos = tk.Toplevel(root)
    janela_veiculos.title("Gestão de Veículos")
    janela_veiculos.geometry("1300x900")
    janela_veiculos.configure(bg='#d0f3e1')

    label_veiculo = tk.Label(janela_veiculos, text="Gerenciamento de Veículos", font=fonte_titulo, bg='#d0f3e1')
    label_veiculo.pack(pady=10)

    frame_placa_do_veiculo=tk.Frame(janela_veiculos, bg='#d0f3e1')
    frame_placa_do_veiculo.pack()

    tk.Label(frame_placa_do_veiculo, width=20, text="Placa do Veículo:", font=fonte_padrao, bg='#d0f3e1').pack(anchor=tk.W, padx=10, side='left')
    global entry_placa
    entry_placa = tk.Entry(frame_placa_do_veiculo, width=100, font=fonte_padrao)
    entry_placa.pack(padx=10, pady=5, side='left')

    frame_modelo_do_veiculo = tk.Frame(janela_veiculos, bg='#d0f3e1')
    frame_modelo_do_veiculo.pack()

    tk.Label(frame_modelo_do_veiculo, width=20, text="Modelo do Veículo:", font=fonte_padrao, bg='#d0f3e1').pack(anchor=tk.W, padx=10, side='left')
    global entry_modelo
    entry_modelo = tk.Entry(frame_modelo_do_veiculo, width=100, font=fonte_padrao, )
    entry_modelo.pack(padx=10, pady=5)

    frame_cor_do_veiculo = tk.Frame(janela_veiculos, bg='#d0f3e1')
    frame_cor_do_veiculo.pack()

    tk.Label(frame_cor_do_veiculo, width=20, text="Cor do Veículo:", font=fonte_padrao, bg='#d0f3e1').pack(anchor=tk.W, padx=10, side='left')
    global entry_cor
    entry_cor = tk.Entry(frame_cor_do_veiculo, width=100, font=fonte_padrao)
    entry_cor.pack(padx=10, pady=5)

    frame_apartamento = tk.Frame(janela_veiculos, bg='#d0f3e1')
    frame_apartamento.pack()

    tk.Label(frame_apartamento, width=20, text="Apartamento:", font=fonte_padrao, bg='#d0f3e1').pack(anchor=tk.W, padx=10, side='left')
    global entry_apartamento_veiculo
    entry_apartamento_veiculo = tk.Entry(frame_apartamento, width=100, font=fonte_padrao)
    entry_apartamento_veiculo.pack(padx=10, pady=5)

    # Frame para os botões (para colocá-los lado a lado)
    frame_btn_registrar_exibir = tk.Frame(janela_veiculos, bg='#d0f3e1')
    frame_btn_registrar_exibir.pack(pady=10)

    btn_registrar_veiculo = tk.Button(frame_btn_registrar_exibir, text="Registrar Veículo", font=fonte_padrao, bg='#659962',
                                      command=registrar_veiculo)
    btn_registrar_veiculo.pack(side='left', pady=10, padx=10)

    btn_exibir_veiculos = tk.Button(frame_btn_registrar_exibir, text="Exibir registro dos veículos", font=fonte_padrao, bg='#f4d451',
                                    command=atualizar_lista_veiculos)
    btn_exibir_veiculos.pack(side='left', pady=5, padx=10)

    # Campo para placa de exclusão

    frame_placa_para_exclusao = tk.Frame(janela_veiculos, bg='#d0f3e1')
    frame_placa_para_exclusao.pack()

    tk.Label(frame_placa_para_exclusao, width=20, text="Placa para Exclusão:", font=fonte_padrao, bg='#d0f3e1').pack(anchor=tk.W, padx=10, side='left')
    global entry_placa_exclusao
    entry_placa_exclusao = tk.Entry(frame_placa_para_exclusao, width=100, font=fonte_padrao)
    entry_placa_exclusao.pack(padx=10, pady=5)

    # Botão para excluir veículo
    btn_excluir_veiculo = tk.Button(janela_veiculos, text="Excluir Veículo", font=fonte_padrao, bg='#db1640', command=excluir_veiculo)
    btn_excluir_veiculo.pack(pady=5)

    # Lista de veículos

    frame_lista_veiculos = tk.Frame(janela_veiculos, bg='#d0f3e1')
    frame_lista_veiculos.pack()

    tk.Label(frame_lista_veiculos, width=20, text="Lista de Veículos:", font=fonte_padrao, bg='#d0f3e1').pack(anchor=tk.W, padx=10, side='left')
    global lista_veiculos
    lista_veiculos = tk.Listbox(frame_lista_veiculos, width=100, height=12, font=fonte_padrao)
    lista_veiculos.pack(padx=10, pady=10)

    frame_placa_para_saida = tk.Frame(janela_veiculos, bg='#d0f3e1')
    frame_placa_para_saida.pack()

    tk.Label(frame_placa_para_saida,width=20, text="Placa para Saída:", font=fonte_padrao, bg='#d0f3e1').pack(anchor=tk.W, padx=10, side='left')
    global entry_placa_saida
    entry_placa_saida = tk.Entry(frame_placa_para_saida, width=100, font=fonte_padrao)
    entry_placa_saida.pack(padx=10, pady=5)

    # Frame para os botões (para colocá-los lado a lado)
    frame_btn_saida_consulta = tk.Frame(janela_veiculos, bg='#d0f3e1')
    frame_btn_saida_consulta.pack(pady=10)

    btn_registrar_saida_veiculo = tk.Button(frame_btn_saida_consulta, text="Registrar Saída Veículo", font=fonte_padrao, bg='#659962',
                                            command=registrar_saida_veiculo_interface)
    btn_registrar_saida_veiculo.pack(side='left', pady=10, padx=10)

    btn_consultar_veiculos_presentes = tk.Button(frame_btn_saida_consulta, text="Consultar Veículos Presentes",
                                                 font=fonte_padrao,bg='#f4d451', command=consultar_veiculos_presentes)
    btn_consultar_veiculos_presentes.pack(side='left', pady=5, padx=10)


# Configuração da janela principal
root = tk.Tk()
root.title("Edifício Solimar")
root.geometry("400x300")

fonte_titulo = ("Arial", 16, "bold")
fonte_padrao = ("Arial", 12)

# Tela inicial com botões para abrir os controles
frame_principal = tk.Frame(root, bg='#626466')
frame_principal.pack(fill=tk.BOTH, expand=True)

btn_abrir_controle_visitantes = tk.Button(frame_principal, text="Gestão de Visitantes", font=('Arial', 15),
                                          width=35,
                                          height=3,
                                          bg='#ceddf2',
                                          command=abrir_controle_visitantes)
btn_abrir_controle_visitantes.pack(pady=20)

btn_abrir_controle_veiculos = tk.Button(frame_principal, text="Gestão de Veículos", font=('Arial', 15),
                                        width=35,
                                        height=3,
                                        bg='#d0f3e1',
                                        command=abrir_controle_veiculos)
btn_abrir_controle_veiculos.pack(pady=20)

root.mainloop()
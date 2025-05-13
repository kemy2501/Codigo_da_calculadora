import tkinter as tk 
def soma():
    num1 = float(entrada1.get())
    num2 = float(entrada2.get())
    resultado = num1 + num2
    exibe_resultado.config(text=f"Resultado:{resultado}")
def subtrair():
    numero1 = float(entrada1.get())
    numero2 = float(entrada2.get())
    resultado = numero1 - numero2
    exibe_resultado.config(text=f"Resultado: {resultado}")
def multiplicação():
    num1 = float(entrada1.get())
    num2 = float(entrada2.get())
    resultado = num1 * num2
    exibe_resultado.config(text=f"Resultado: {resultado}")
def dividir():
    num1 = float(entrada1.get())
    num2 = float(entrada2.get())
    resultado = num1 % num2
    exibe_resultado.config(text=f"Resultado:{resultado}")
def fechar():
    janela.destroy()

janela = tk. Tk()
janela.title("Calculadora")
janela.geometry("650x650")
janela.configure( bg="black")

label1 = tk.Label(janela, text="primeiro número:" , font=("Arial", 20)).pack(pady = 5)
entrada1 = tk.Entry(janela)
entrada1.pack(pady = 5)
label2 = tk.Label(janela, text="segundo número:" , font=("Arial", 20)).pack(pady = 5)
entrada2 = tk.Entry(janela)
entrada2.pack(pady = 5)

frame_botoes = tk.Frame(janela , bg="black") 
frame_botoes.pack(side = "left", pady = 10) 

btn_soma = tk.Button(frame_botoes, text= "soma", command = soma  , width=10 , bg="white" , font=("Arial" , 12))
btn_soma.pack(side = "left" , pady=10)

btn_subtrair = tk.Button(frame_botoes, text= "subtrair" ,command = subtrair , width=10 , bg="white" , font=("Arial" , 12))
btn_subtrair.pack(side = "left" , pady=10)

btn_multiplicação = tk.Button(frame_botoes, text= "multiplicação", command = multiplicação  , width=10 , bg="white" , font=("Arial" , 12))
btn_multiplicação.pack(side = "left" , pady=10)

btn_dividir = tk.Button(frame_botoes, text= "dividir" ,command = dividir , width=10 , bg="white" , font=("Arial" , 12))
btn_dividir.pack(side = "left" , pady=10)

janela_resultado = tk.Frame(janela , bg="black")
exibe_resultado = tk.Label(janela , text= "resultado:" , font=("Arial", 20) , bg="white" )
exibe_resultado.pack(side= "left" , pady = 15)



janela.mainloop()


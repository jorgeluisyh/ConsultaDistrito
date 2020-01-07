# -*- coding: utf-8 -*-
import Tkinter as tk
import tkMessageBox, os
import tkFont
from PIL import ImageTk, Image
import difflib as df
import webbrowser

currt = __file__
from distritos import ubig
baseDistritos = ubig

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

icon = resource_path("peru.ico")
imag = resource_path("peru_fisico.png")

# icon = os.path.join(os.path.dirname(__file__), "peru.ico")
# imag = os.path.join(os.path.dirname(__file__), "peru_fisico.png")

def callback(url):
  webbrowser.open(url)
def estructura():
    x= busqueda()
    if type(x)== str:
      return x
    elif type(x[0]) == str:
      dep = x[2]
      prov = x[1]
      dist = x[0]
      texto = "Departamento: {0} \nProvincia : {1}\nDistrito: {2}"
      return texto.format(dep,prov,dist)
    else:
      textazo =[]
      for i in x:
        dep = i[2]
        prov = i[1]
        dist = i[0]
        ubi  = i[3]
        texto = "Ubigeo: {3}\nDepartamento: {0} \nProvincia : {1}\nDistrito: {2}".format(dep,prov,dist,ubi)
        textazo.append(texto)
      return "\n---------------\n".join(textazo)


def show_entry_fields():
    label["text"]=estructura().replace('\u00d1','Ñ')
    label["fg"]='black'
    # tk.Label(master, text=estructura()).grid(row=2,column=1,sticky=tk.W,pady=4,)
def busqueda():
    var = e1.get()
    if var[0].isdigit():
      print u"número"
      if baseDistritos.get(var):
        return baseDistritos.get(var)
      else:
        return "Este Ubigeo no existe"
    else:
      # var.replace('Ñ',u'\u00d1')
      print "letra"
      var = var.upper()
      var.replace(u'Ñ','\u00d1')
      lista=[]
      for k,v in baseDistritos.items():
        name = unicode(v[0]).replace('\u00d1',u'Ñ')
        if df.SequenceMatcher(None,var.upper(), name).ratio()>0.8:
          print var,v[0]
          lista.append([v[0],v[1],v[2],k])
      
      if len (lista)>0:
        return lista
      else:
        return  "No fue encontrado"


#comienza el gui
master = tk.Tk()
master.title("Buscar distrito")
master.iconbitmap(icon)

img = ImageTk.PhotoImage(Image.open(imag))
# img = ImageTk.PhotoImage(Image.open(img))
panel = tk.Label(master, image = img)
panel.grid(column=0, row=2)

tk.Label(master,text="Ingrese Nombre \nDistrito o Ubigeo",justify = 'left').grid(row=0)

e1 = tk.Entry(master)


e1.grid(row=0, column=1, padx =5, pady = 5)


label =tk.Label(master, text="Sin consulta realizada",fg="blue")
autor =tk.Label(master,text="J.Yupanqui", fg="blue",)
autor.grid(row=3,column=0)
autor.bind("<Button-1>", lambda e: callback("https://jorgeluisyh.github.io/blog/"))
label.grid(row=2,column=1,sticky=tk.W,pady=4)

f = tkFont.Font(autor,autor.cget("font"))
f.configure(underline = True)
autor.configure(font = f)


tk.Button(master, 
          text='Cerrar', 
          command=master.quit).grid(row=3, 
                                    column=1, 
                                    sticky=tk.W, 
                                    pady=4)
tk.Button(master, 
          text='Mostrar', justify = 'right' ,command=show_entry_fields).grid(row=3, 
                                                       column=1, 
                                                       sticky=tk.E, 
                                                       padx = 5,
                                                       pady=4)
def func(event):
    show_entry_fields()
    # print("You hit return.")
    print'\a'
    
    
master.bind('<Return>', func)

tk.mainloop()



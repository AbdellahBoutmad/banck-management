from tkinter import *
import ttkbootstrap as tb
import random
import json

root = tb.Window(themename="morph")
root.geometry("350x600")

label = tb.Label(text="Gestion de Banque", font="Helvetica 30", bootstyle="warning")
label.pack(pady=30)

list_compte = []
class Compte:
    def __init__(self, client="", solde=0, rib=0, num_compte=0):
        self.client = client
        self.num_compte = num_compte
        self.solde = solde
        self.rib = rib

    def add_compte(self):
        self.solde = solde.get()
        self.client = client.get()
        with open("ban-data.json", "r") as fichier:
            x = json.loads(fichier.read())
        self.num_compte = random.randint(1, 1000000000)
        for i in range(len(x)):
            if self.num_compte == x[i]["num_compte"]:
                self.num_compte += 1
        self.rib = str(random.randint(1, 99)) + str(self.num_compte) + str(random.randint(1, 100))
        compte_info = {
            "client": self.client,
            "num_compte": self.num_compte,
            "rib": self.rib,
            "solde": int(self.solde)
        }
        x.append(compte_info)
        with open("ban-data.json", "w") as fichier:
            fichier.write(json.dumps(x, indent=4))
              
#initialise class to add new client
def add():
    client = Compte()
    client.add_compte()
#menu agent to add client graphik inputs
def menu_add():
    global client
    global solde
    menu_add = tb.Window(themename="morph")
    menu_add.geometry("350x600")
    label = Label(menu_add, text="MENU TO ADD CLIENT", font="Helvetica 20")
    label.pack(pady=40)
    label = Label(menu_add, text="Nom de client :", font="Helvetica 15")
    label.pack()
    client = tb.Entry(menu_add, width=20, font="Helvetica 20")
    client.pack(pady=30)
    label = Label(menu_add, text="Le solde a ajouter :", font="Helvetica 15")
    label.pack()
    solde = tb.Entry(menu_add, width=20, font="Helvetica 20")
    solde.pack(pady=30)
    button = Button(menu_add, text="Save client", width="20", font="Helvetica 20", command=add)
    button.pack(pady=20)
    

#menu agent suprime client check
def suprime():
    
    fichier = open ("ban-data.json", "r" ) 
    x=json.loads(fichier.read( ) )
    
    for i in range(len(x)):
        print(x[i])
        if client.get() == x[i]["client"]:
            if int(num.get()) == x[i]["num_compte"]:
                del(x[i])
                fichier=open ("ban-data.json","w") #ouvrir un fichier en écriture
                fichier.write(json.dumps(x,indent=4)) #transformer le dictionnaire en texte json
                fichier.close()
            
#menu agent graphik inputs to delete client
def delete():
    global client
    global num
    menu_delete = tb.Window(themename="morph")
    menu_delete.geometry("350x600")
    label = Label(menu_delete, text="MENU TO DELETE CLIENT", font="Helvetica 20")
    label.pack(pady=40)
    label = Label(menu_delete, text="Nom de client :", font="Helvetica 15")
    label.pack()
    client = tb.Entry(menu_delete, width=20, font="Helvetica 20")
    client.pack(pady=30)
    label = Label(menu_delete, text="Le numero de client :", font="Helvetica 15")
    label.pack()
    num = tb.Entry(menu_delete, width=20, font="Helvetica 20")
    num.pack(pady=30)
    

    
    button = Button(menu_delete, text="Delete client", width="20", font="Helvetica 20", command=suprime)
    button.pack(pady=20)
#menu agent graphik buttons
def menu_agent():
    agent = tb.Window(themename="morph")
    agent.geometry("350x600")
    label = Label(agent, text="MENU AGENT", font="Helvetica 30")
    label.pack(pady=30)
    button1 = Button(agent, text="Add client", width="20", font="Helvetica 20", command=menu_add)
    button1.pack(pady=20)
    button2 = Button(agent, text="Delete client", width="20", font="Helvetica 20",command=delete)
    button2.pack(pady=20)
    button3 = Button(agent, text="Add solde", width="20", font="Helvetica 20",command=anviste)
    button3.pack(pady=20)
    button4 = Button(agent, text="Retirer solde", width="20", font="Helvetica 20",command=retre)
    button4.pack(pady=20)
    button5 = Button(agent, text="Afficher client", width="20", font="Helvetica 20",command=affiche)
    button5.pack(pady=20)
#menu inviste inputs
def anviste():
    global cash
    global num
    menu_inviste = tb.Window(themename="morph")
    menu_inviste.geometry("350x600")
    label = Label(menu_inviste, text="MENU TO inviste argent", font="Helvetica 20")
    label.pack(pady=40)
    label = Label(menu_inviste, text="l'argent a ajouter au compte :", font="Helvetica 15")
    label.pack()
    cash = tb.Entry(menu_inviste, width=20, font="Helvetica 20")
    cash.pack(pady=30)
    label = Label(menu_inviste, text="Le numero de client :", font="Helvetica 15")
    label.pack()
    num = tb.Entry(menu_inviste, width=20, font="Helvetica 20")
    num.pack(pady=30)
  
    button = Button(menu_inviste, text="ajoute l'argent", width="20", font="Helvetica 20", command=lambda : invister(num.get(),cash.get()))
    button.pack(pady=20)
#menu inviste chekc enters
def invister(number,cash_toadd):
        num=int(number)
        fichier = open ( "ban-data.json", "r" ) #ouvrir le fichier exemple.json en lecture
        x=json.loads(fichier.read( ) )
        for i in range(len(x)):           
            if num == x[i]['num_compte']:
                cash = int(cash_toadd)
                # self.solde += cash 
                # x[i]["solde"] +=self.solde
                x[i]['solde'] += cash
                fichier=open ("ban-data.json","w") #ouvrir un fichier en écriture
                fichier.write(json.dumps(x,indent=4)) #transformer le dictionnaire en texte json
                fichier.close() #fermer le fichier
                print("le solde ajouter ! ")
               
                return True
#menu retre inputs
def retre():
    global cash
    global num
    global menu_retrer
    menu_retrer = tb.Window(themename="morph")
    menu_retrer.geometry("350x600")
    label = Label(menu_retrer, text="MENU TO retrer argent", font="Helvetica 20")
    label.pack(pady=40)
    label = Label(menu_retrer, text="l'argent a retrer :", font="Helvetica 15")
    label.pack()
    cash = tb.Entry(menu_retrer, width=20, font="Helvetica 20")
    cash.pack(pady=30)
    label = Label(menu_retrer, text="Le numero de client :", font="Helvetica 15")
    label.pack()
    num = tb.Entry(menu_retrer, width=20, font="Helvetica 20")
    num.pack(pady=30)
  
    button = Button(menu_retrer, text="Retrer l'argent", width="20", font="Helvetica 20", command=lambda : retrer(num.get(),cash.get()))
    button.pack(pady=20)
#menu retrer chekc enters
def retrer(number,cash_retrer):
        operation = Label(menu_retrer, text="", font="Helvetica 10")
        operation.pack(pady=40)        
        num=int(number)
        fichier = open ( "ban-data.json", "r" ) #ouvrir le fichier exemple.json en lecture
        x=json.loads(fichier.read( ) )
        for i in range(len(x)):
            
            if num == x[i]['num_compte']:
                cash = int(cash_retrer)
                # self.solde += cash 
                # x[i]["solde"] +=self.solde
                if cash <= x[i]["solde"]:
                    x[i]['solde'] -= cash
                    fichier=open ("ban-data.json","w") #ouvrir un fichier en écriture
                    fichier.write(json.dumps(x,indent=4)) #transformer le dictionnaire en texte json
                    fichier.close() #fermer le fichier
                    operation.config(text="operation a passé avec success !")
                    print("le solde ajouter ! ")
                else:
                    operation.config(text="operation a echouer !!")

               
                return True
#menu graphik client affich all client
def affiche():
    tableau = tb.Window(themename="morph")
    tableau.geometry("350x600")
    title=Label(tableau,text="Les client de banque",font="Helvetica 20")
    title.pack(pady=20)
    fichier = open ("ban-data.json", "r" ) 
    x=json.loads(fichier.read( ) )
    tabl_titre=Label(tableau,text="client-----num_compte---solde-----rib------",font="Helvetica 13",bg='black')
    tabl_titre.pack()
    for i in range(len(x)):
        a=x[i]["client"] ,"|", x[i]["num_compte"] ,"|", x[i]["solde"] ,"|", x[i]["rib"]
        result=Label(tableau,text="------------------------------------------------------------------------------------------")
        result.pack()
        ligne=Label(tableau,text=a,font="Helvetica 12")
        ligne.pack()

     
     #espace client************************************************
#menu client buttons all
def menu_client():
    client_window = tb.Window(themename="morph")
    client_window.geometry("350x600")
    label = Label(client_window, text="MENU CLIENT", font="Helvetica 30")
    label.pack(pady=30)
    button1 = Button(client_window, text="mon compte", width="20", font="Helvetica 20",command=affiche_client_graph)
    button1.pack(pady=20)
    button2 = Button(client_window, text="invister argent", width="20", font="Helvetica 20",command=anviste)
    button2.pack(pady=20)
    button3 = Button(client_window, text="retrer argent", width="20", font="Helvetica 20",command=retre)
    button3.pack(pady=20)
    button4 = Button(client_window, text="transfere d'argent", width="20", font="Helvetica 20",command=client_transfere_graph)
    button4.pack(pady=20)
#menu client affich his cont inputs graphik
def affiche_client_graph():   
    global nom
    global num
    menu_client_graph = tb.Window(themename="morph")
    menu_client_graph.geometry("350x600")
    label = Label(menu_client_graph, text="MENU TO client compte", font="Helvetica 20")
    label.pack(pady=40)
    label = Label(menu_client_graph, text="entrer votre nom :", font="Helvetica 15")
    label.pack()
    nom = tb.Entry(menu_client_graph, width=20, font="Helvetica 20")
    nom.pack(pady=30)
    label = Label(menu_client_graph, text="Le numero de compte :", font="Helvetica 15")
    label.pack()
    num = tb.Entry(menu_client_graph, width=20, font="Helvetica 20")
    num.pack(pady=30)
  
    button = Button(menu_client_graph, text="Afficher mon compte", width="20", font="Helvetica 20", command=lambda : affiche_client(num.get(),nom.get()))
    button.pack(pady=20)
#menu client affich his cont inputs check and affiche
def affiche_client(num,nom):
    tableau_client = tb.Window(themename="morph")
    tableau_client.geometry("350x600")
    title=Label(tableau_client,text="Les iformation de votre compte banquaire",font="Helvetica 14")
    title.pack(pady=20)
    fichier = open ("ban-data.json", "r" ) 
    x=json.loads(fichier.read( ) )
    label = Label(tableau_client,text="")
    label.pack()
    for i in range(len(x)):
                if nom == x[i]['client']:
                    if int(num) == x[i]['num_compte']:
                        a ="nom client : " +  x[i]["client"] +"\n" + "numero de compte : " + str(x[i]["num_compte"]) + "\n" + "RIB : " + str(x[i]["rib"]) + "\n"+"solde : " + str(x[i]["solde"])
                        label.config(text=a,font="Helvetica 15")
                    else:
                        label.config(text='la numero de compte est incorrect',font="Helvetica 15")
#menu client transfere argent inputs graphik
def client_transfere_graph():
    menu_transfere = tb.Window(themename="morph")
    menu_transfere.geometry("350x600")
    label = Label(menu_transfere, text="Menu to transfere argent", font="Helvetica 20")
    label.pack(pady=40)
    label = Label(menu_transfere, text="entrer votre numero de compte :", font="Helvetica 15")
    label.pack(pady=10)
    num_sender = tb.Entry(menu_transfere, width=20, font="Helvetica 20")
    num_sender.pack(pady=10)
    label = Label(menu_transfere, text="entrer le numero de recepteur", font="Helvetica 15")
    label.pack(pady=10)
    num_recept = tb.Entry(menu_transfere, width=20, font="Helvetica 20")
    num_recept.pack()
    label = Label(menu_transfere, text="entrer l'argent a transfere :", font="Helvetica 15")
    label.pack(pady=10)
    cash = tb.Entry(menu_transfere, width=20, font="Helvetica 20")
    cash.pack(pady=10)
    button = Button(menu_transfere, text="TRANSFERE", width="20", font="Helvetica 20", command=lambda : transfere(num_sender.get(),num_recept.get(),cash.get()))
    button.pack(pady=40)
#menu client transfere argent inputs check
def transfere(num_sender,num_recept,cash):
    fichier = open ("ban-data.json", "r" ) 
    x=json.loads(fichier.read( ) )
    for i in range(len(x)):
        
        if int(num_sender) == x[i]['num_compte']:
            x[i]["solde"]-=int(cash)
        elif int(num_recept) == x[i]['num_compte']:
            x[i]["solde"]+=int(cash)
        fichier=open ("ban-data.json","w") #ouvrir un fichier en écriture
        fichier.write(json.dumps(x,indent=4)) #transformer le dictionnaire en texte json
        fichier.close() #fermer le fichier
    

my_style = tb.Style()
my_style.configure('primary.Outline.TButton', font="Helvetica 20", bootstyle="outline")
button1 = tb.Button(text="Agent", width=20, style="primary.Outline.TButton", command=menu_agent)
button1.pack(pady=120)
button2 = tb.Button(text="Client", width=20, style="primary.Outline.TButton", command=menu_client)
button2.pack()

root.mainloop()
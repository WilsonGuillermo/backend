import tkinter

import tkinter.messagebox



def FNC_Icon ( Q ) :
    print("1")
    tkinter.messagebox.showinfo ( message = f"Boite de dialogue\navec l'icone { Q } ..." , icon = Q )



TKI_Principal = tkinter.Tk()


tkinter.Label ( TKI_Principal , text = "Tester l'icone ..." ).pack()

tkinter.Button ( TKI_Principal , text = "Fautif." , command = lambda : FNC_Icon ( "error" ) ).pack()
print("2")
tkinter.Button ( TKI_Principal , text = "Informatif." , command = lambda : FNC_Icon ( "info" ) ).pack()

tkinter.Button ( TKI_Principal , text = "Interrogatif." , command = lambda : FNC_Icon ( "question" ) ).pack()

tkinter.Button ( TKI_Principal , text = "Attentif." , command = lambda : FNC_Icon ( "warning" ) ).pack()
tkinter.Button ( TKI_Principal , text = "Quitter" , command = TKI_Principal.destroy ).pack()


TKI_Principal.mainloop()
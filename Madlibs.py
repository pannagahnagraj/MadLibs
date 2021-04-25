from tkinter import *

root = Tk()
root.geometry('400x400')
root.title('MadLibs')
Label(root,text='MADLIBS', font='arial 20 bold').pack()
Label(root, text = 'Choose a topic :', font = 'arial 15 bold').place(x=40, y=80)

def madlib1():
   
    Toys = input('Enter a Toy : ')
    Musical_Instrument = input('Enter a Musical Instrument : ')
    Noun1 = input('Enter a Noun :')
    Dessert = input('Enter a Dessert : ')
    Snacks= input('Enter a Snack : ')
    Verb3 = input('Enter a Verb : ')
    Animal= input('Enter an animal : ')
    Noun2 = input('Enter a Noun : ')
    Number = input('Enter a Number : ')
    Noun3 = input('Enter a Noun : ')
    Number1 = input('Enter a Number : ')
    Number2 = input('Enter a Number : ')
    Vehicle = input('Enter a Vehicle : ')
    Animal1 = input('Enter an animal : ')

    print('If I was principal of my school, I would put '+Toys+' and '+Musical_Instrument+' in every '+Noun1+' and have the cafeteria serve '+Dessert+' and '+Snacks+' for lunch. We would have '+Verb3+' everyday, where students can bring '+Animal+' and '+Noun2+' to share in class. Students would give teachers homework, like '+Number+' page book reports about '+Noun3+' and '+Number1+' math problems. Recess would last for '+Number2+' hours, instead of buses, I would have '+Vehicle+' and '+Animal1+' take the kids to and from school.')
    


def madlib2():
    Noun = input('Enter a Noun: ')
    Plural_Noun1 = input('Enter a Plural Noun: ')
    Verb1 = input('Enter a Verb in Present Tense: ')
    Verb2 = input('Enter a Verb in Present Tense: ')
    Part_of_Body= input('Enter a Part of Body(Plural): ')
    Adjective1 = input('Enter an adjective: ')
    Plural_Noun2 = input('Enter a Plural Noun: ')
    Adjective2 = input('Enter an Adjective: ')

    print('Today, every student has a computer small enough to fit into his '+Noun+'. He can solve any math problem by simply pushing the computers little '+Plural_Noun1+'. Compiters can add, multiply, divide and '+Verb1+'. They can also '+Verb2+' better than a human. Some computers are '+Part_of_Body+'. Others have a/an '+Adjective1+' screen that shows all kinds of '+Plural_Noun2+' and '+Adjective2+' figures.')
  
   
Button(root, text= 'If I were a principal', font ='arial 15', command= madlib1, bg = 'ghost white').place(x=60, y=140)
Button(root, text= 'The Computer', font ='arial 15', command = madlib2, bg = 'ghost white').place(x=60, y=200)



root.mainloop()


from tkinter import Tk, BOTH, LEFT,RIGHT, SUNKEN,TOP, RAISED,DISABLED, NORMAL
from tkinter import N,E,W,X,IntVar
from tkinter.ttk import Frame, Style,Label, Button , Radiobutton
from tkinter import messagebox




questions=['Is Python case sensitive when dealing with identifiers?',
           'What is the maximum possible length of an identifier?',
           'Which of the following is invalid?',
           'Which of the following is an invalid variable?',
           'Why are local variable names beginning with an underscore discouraged?',
           'Python is a ___object-oriented programming language',
           'Amongst the following, who is the developer of Python programming?',
           'Python Dictionary is used to store the data in a ___ format.',
           'Conditional statements are also known as ___ statements.',
           'Which of the following is not used as conditional statement in Python?',         
          ]

options=[( 'a) yes','b) no','c) machine dependent', 
           'd) none of the mentioned'),
         
         ('a) 31 characters','b) 63 characters','c) 79 characters',
          'd) none of the mentioned'),
         
         ('a) _a = 1','b) __a = 1','c) __str__ = 1',
          'd) none of the mentioned'),
         
         ('a) my_string_1','b) 1st_string','c) foo','d) _'),
         
         ('a) they are used to indicate a private variables of a class',
          'b) they confuse the interpreter',
          'c) they are used to indicate global variables',
          'd) they slow down execution'),

          ('a) Special purpose', 
           'b) General purpose', 
           'c) Medium level programming language', 
           'd) All of the mentioned above'),

          ('a) Guido van Rossum', 
           'b) Denis Ritchie', 
           'c) Y.C. Khenderakar', 
           'd) None of the mentioned above'),

          ('a) Key value pair', 
           'b) Group value pair', 
           'c) Select value pair', 
           'd) None of the mentioned above'),

          ('a) Decision-making', 
           'b) Array', 
           'c) List', 
           'd) None of the mentioned above'),

          ('a) switch', 
           'b) if...else', 
           'c) if...else', 
           'd) None of the mentioned above'),
          ]

answers=['a','d','d','b','a','b','a','a','a','a']

solution={}

zipped = zip(questions,options,answers)
list1 = list(zipped)
print(list1)

class ExamFrame(Frame):
    def __init__(self,parent):
        Frame.__init__(self,parent)
        self.parent = parent
        self.question_no=0
        self.initUI()
        
    def initUI(self):
        self.rvar = IntVar()
        self.style = Style()
        self.style.theme_use("alt")
        self.parent.title("EXAM DEMO")
        self.pack(fill=BOTH , expand=1)
    
        frameQuestion = Frame(self,width=500, height=400,relief=SUNKEN)
        self.lbquestion = Label(frameQuestion, text="Question No.:",
                           width=150)
        self.lbquestion.pack(anchor=N+W,side=LEFT,padx=5, pady=5) 
        frameQuestion.pack(anchor=N+W, ipadx=20, fill=X,ipady=20, padx=15,pady=15)
        
        frameOptions = Frame(self,relief=SUNKEN)
        self.radioOption1 = Radiobutton(frameOptions, text='Option1',
                                        command=self.onOptionSelect1,
                                   variable=self.rvar,value=1)
        self.radioOption2 = Radiobutton(frameOptions, text='Option2',
                                        command=self.onOptionSelect1,
                                   variable=self.rvar,value=2)
        self.radioOption3 = Radiobutton(frameOptions, text='Option3',
                                        command=self.onOptionSelect1,
                                   variable=self.rvar,value=3)
        self.radioOption4 = Radiobutton(frameOptions, text='Option4',
                                        command=self.onOptionSelect1,
                                   variable=self.rvar,value=4)
        self.radioOption1.pack(anchor=N+W,side=TOP,padx=5, pady=5)
        self.radioOption2.pack(anchor=N+W,side=TOP,padx=5)
        self.radioOption3.pack(anchor=N+W,side=TOP,padx=5, pady=5)
        self.radioOption4.pack(anchor=N+W,side=TOP,padx=5)
        frameOptions.pack(anchor=N+W, ipadx=20, fill=X,
                      ipady=20, padx=15,pady=15)
        
        frameBottom = Frame(self,relief=SUNKEN,width=400)
        self.buttonStart= Button(frameBottom, text="Start Test",
                            command=self.onButtonStartClick)
      
        self.buttonStart.pack(side=LEFT, padx=25)
        buttonNext = Button(frameBottom, text="Next",
                            command=self.onButtonNextClick)
        buttonNext.pack(side=LEFT)
        buttonPrevious = Button(frameBottom, text="Previous",
                                command=self.onButtonPreviousClick)
        buttonPrevious.pack(side=LEFT, padx=25)
        self.buttonEndTest = Button(frameBottom, text="End Test",
                               command=self.onButtonEndTestClick, state=DISABLED)  
        self.buttonEndTest.pack(side=LEFT) 
        frameBottom.pack(anchor=N+W, ipadx=20, fill=X, expand=True,
                      ipady=20, padx=15,pady=15)
        

    def saveAns(self,currentAns):
        solution[self.question_no]=currentAns
        print(solution)

    def getSelectedOption(self):
        val = self.rvar.get()
        if val==1:
            selectedOption='a'
        elif val==2:
            selectedOption='b'
        elif val==3:
            selectedOption='c'
        elif val==4:
            selectedOption='d'
        else: selectedOption=''
        return selectedOption

    def getOldAns(self):
        return solution.get(self.question_no)

    def onOptionSelect1(self):
        selectedOption = self.getSelectedOption()
        solution[self.question_no]=selectedOption
        print(len(solution))
        if len(solution)==len(questions):
            self.buttonEndTest.config(state=NORMAL)

    def resetRadioButtons(self):
        self.rvar.set(0)
        

    def setRadioButtons(self,oldAns):
        if oldAns=='a': self.rvar.set(1)
        elif oldAns=='b': self.rvar.set(2)
        elif oldAns=='c': self.rvar.set(3)
        elif oldAns=='d': self.rvar.set(4)

    def setOldAnsOption(self,oldAns):
        self.resetRadioButtons()
        self.setRadioButtons(oldAns)
        
        
    def onButtonStartClick(self):
        self.question_no=0
        self.buttonStart.config(state=DISABLED)
        q=list1[self.question_no][0]
        q = f'Question No.{self.question_no+1}: {q}'
        print(q)
        self.lbquestion.config(text=q)
        options=list1[self.question_no][1]
        self.radioOption1.config(text=options[0])
        self.radioOption2.config(text=options[1])
        self.radioOption3.config(text=options[2])
        self.radioOption4.config(text=options[3])
        
    def onButtonNextClick(self):
        currentAns = self.getSelectedOption()
        self.saveAns(currentAns)
        self.question_no +=1
        if self.question_no>=len(list1):
            self.question_no=len(list1)-1 #setting to last question
            return
        
        oldAns = self.getOldAns()
        if oldAns != None:
            self.setOldAnsOption(oldAns)
        else:
            self.resetRadioButtons()
        q=list1[self.question_no][0]
        q = f'Question No.{self.question_no+1}: {q}'
        self.lbquestion.config(text=q)
        options=list1[self.question_no][1]
        self.radioOption1.config(text=options[0])
        self.radioOption2.config(text=options[1])
        self.radioOption3.config(text=options[2])
        self.radioOption4.config(text=options[3])
        
    def onButtonPreviousClick(self):
        currentAns = self.getSelectedOption()
        self.saveAns(currentAns)
        self.question_no -=1
        if self.question_no<0:
            self.question_no=0 # setting to fist question
            return
        oldAns = self.getOldAns()
        if oldAns != None:
            self.setOldAnsOption(oldAns)
        else:
            self.resetRadioButtons()
        q=list1[self.question_no][0]
        q = f'Question No.{self.question_no+1}: {q}'
        self.lbquestion.config(text=q)
        options=list1[self.question_no][1]
        self.radioOption1.config(text=options[0])
        self.radioOption2.config(text=options[1])
        self.radioOption3.config(text=options[2])
        self.radioOption4.config(text=options[3])

            
    def onButtonEndTestClick(self):
        print('End Button Clicked')
        totalMarks=len(answers)
        obtainedMarks=0
        qno=0
        for correctAns in answers:
            if correctAns==solution[qno]:
                obtainedMarks +=1
            qno +=1
        print(f"Total Marks :{totalMarks}")
        print(f"Marks Obtained:{obtainedMarks}")
        messagebox.showinfo("Result",f"Total Marks :{totalMarks*10}\n\nMarks Obtained:{obtainedMarks*10}")
            
      
def main():
    root = Tk()
   

    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    # Set the geometry size to full screen
    root.geometry(f"{screen_width}x{screen_height}+0+0")

    app = ExamFrame(root)
    root.mainloop()

if __name__=='__main__':
    main()

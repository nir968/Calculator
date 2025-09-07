import os
import tkinter as tk
from tkinter import ttk

# אם ה-venv לא מזהה את הנתיב של Tcl/Tk, נוסיף ידנית:
os.environ['TCL_LIBRARY'] = r"C:\Users\nir96\AppData\Local\Programs\Python\Python313\tcl\tcl8.6"
os.environ['TK_LIBRARY']  = r"C:\Users\nir96\AppData\Local\Programs\Python\Python313\tcl\tk8.6"


class CalculatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculator")
        self.root.geometry("300x400")
        #self.root.resizable(True, True)
        self.root.resizable(False,False )

        self.expression = ""

        # create a string Variable to display the text
        self.display_text = tk.StringVar()

        self.last_answer = ""

        #self.is_dark = False

        # create the display frame
        #display_frame = ttk.Frame(self.root)
        #display_frame.pack(fill=tk.BOTH, expand=True)

        #toggle_button = ttk.Button(self.root, text="Dark Mode",command=self.toggle_theme )
        #toggle_button.pack(side=tk.BOTTOM, fill=tk.X)
        #toggle_button = ttk.Button(display_frame, text="Dark Mode", command=self.toggle_theme)
        #toggle_button.grid(row=0, column=0, sticky="nsew")


        # create the display frame
        display_frame = ttk.Frame(self.root)
        display_frame.pack(fill=tk.BOTH, expand=True)

        # create the display label
        display_label = ttk.Label(
            display_frame,
            textvariable=self.display_text,
            font=("Arial", 26),
            anchor="e",
            background="white",
            foreground="black",
            padding=6
        )
        display_label.pack(fill=tk.BOTH, expand=True)
        #display_label.grid(row=0, column=1, sticky="nsew")

        #display_frame.columnconfigure(0, weight=0)  # הכפתור ישאר צר
        #display_frame.columnconfigure(1, weight=1)  # התצוגה תתפוס את כל השאר

        # Create Button Frame
        button_frame = ttk.Frame(self.root)
        button_frame.pack(fill=tk.BOTH, expand=True)

        self.create_buttons(button_frame)

    def create_buttons(self, frame):
        buttons = [
            ('7',1,0),('8',1,1),('9',1,2),('+',1,3),('%',1,4),
            ('4',2,0),('5',2,1),('6',2,2),('-',2,3),('.',2,4),
            ('1',3,0),('2',3,1),('3',3,2),('*',3,3),('Ans',3,4),
            ('0',4,0),('AC',4,1),('C',4,2),('/',4,3),('=',4,4),
        ]

        for (text, row, col) in buttons:
            button = ttk.Button(frame, text=text, command=lambda t=text: self.on_button_click(t))
            button.grid(row=row, column=col, sticky="nsew", padx=2, pady=2)

        for i in range(5):
            frame.rowconfigure(i, weight=1)
        for j in range(5):
            frame.columnconfigure(j, weight=1)


    def on_button_click(self, button_text):

        if button_text == "AC":
            self.expression = ""


        elif button_text == "C":
            self.expression = self.expression[:-1]


        elif button_text == "=":
            try:
                result = eval(self.expression)
                self.expression = str(result)
                self.last_answer = result
            except Exception:
                self.expression = "Error"


        elif button_text == "%":
            try:
                self.expression = str(eval(self.expression + "/100"))
            except Exception:
                self.expression = "Error"


        elif button_text == ".":
            if not self.expression.endswith("."):
                self.expression += button_text


        elif button_text == "Ans":
            if self.expression == "":
                self.expression = str(self.last_answer)
            else:
                try:
                   result = eval(self.expression + "*" + str(self.last_answer))
                   self.expression = str(result)
                   self.last_answer = result
                except Exception:
                    self.expression = "Error"

        else:
            self.expression += button_text

        self.display_text.set(self.expression)

    # def toggle_theme(self):
    #     if not self.is_dark:
    #         # Dark Mode
    #         self.root.configure(bg="black")
    #         self.display_text.set("Dark Mode On")
    #         self.is_dark = True
    #     else:
    #         # Light Mode
    #         self.root.configure(bg="white")
    #         self.display_text.set("Light Mode Off")
    #         self.is_dark = False


if __name__ == "__main__":
    root = tk.Tk()
    app = CalculatorApp(root)
    root.mainloop()

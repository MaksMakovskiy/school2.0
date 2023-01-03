from tkinter import Frame, Label, Button, Tk


class calculator(Frame):
    def init(self, root):
        super(calculator, self).init(root)
        self.build()

    def build(self):
        self.formula = "0"
        self.lbl = Label(
            text=self.formula,
            font=("Times New Roman", 21, "bold"),
            bg="#000",
            foreground="#FFF",
        )
        self.lbl.place(x=11, y=50)

        btns = [
            "C",
            "DEL",
            "*",
            "=",
            "1",
            "2",
            "3",
            "/",
            "4",
            "5",
            "6",
            "+",
            "7",
            "8",
            "9",
            "-",
            "(",
            "0",
            ")",
            "X^2",
        ]

        x = 10
        y = 140
        for bt in btns:
            com = lambda x=bt: self.logicalc(x)
            Button(text=bt, bg="#FFF", font=("Times New Roman", 15), command=com).place(
                x=x, y=y, width=115, height=79
            )
            x += 117
            if x > 400:
                x = 10
                y += 81

    def logicalc(self, operation):
        if operation == "C":
            self.formula = ""
        elif operation == "DEL":
            self.formula = self.formula[0:-1]
        elif operation == "X^2":
            self.formula = str((eval(self.formula)) ** 2)
        elif operation == "=":
            self.formula = str(eval(self.formula))
        else:
            if self.formula == "0":
                self.formula = ""
            self.formula += operation
        self.update()

    def update(self):
        if self.formula == "":
            self.formula = "0"
        self.lbl.configure(text=self.formula)


def calck():
    while True:
        a = float(input("Введите первое число >>>: "))
        change = str(input("**, *, /, +, -, %, // >>>: "))
        b = float(input("Введите второе число >>>: "))
        if a == 0 and b == 0:
            break
        elif change == "**":
            print(f"<<<: {a**b}")
        elif change == "*":
            print(f"<<<: {a*b}")
        elif change == "/":
            print(f"<<<: {a/b}")
        elif change == "+":
            print(f"<<<: {a+b}")
        elif change == "-":
            print(f"<<<: {a-b}")
        elif change == "%":
            print(f"<<<: {a%b}")
        elif change == "//":
            print(f"<<<: {a//b}")
        else:
            print("Выбранно неизвестное действие, пожалуйста выберите из списака <<<:")


if __name__ == "__main__":
    

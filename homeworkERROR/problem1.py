def squre(x):
    return x**2
def input_number():
    while True:
        try:
            y=int(input("Enter number: "))
            # return squre(y)
        except ValueError:
            print("Not a int_num, Enter number!")
        else:
            return squre(y)
            break
        finally:
            print("thank you")
                                                                                                     
if __name__=='__main__':
    print(input_number())
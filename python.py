from flask import Flask

app = Flask(__name__)

@app.route('/')
def lista_primos():
    primos = []
    num = 2

    while len(primos) < 100:
        eh_primo = True
        for i in range(2, num):
            if num % i == 0:
                eh_primo = False
                break
        if eh_primo:
            primos.append(num)
        num += 1


    output = ""
    for i, num in enumerate(primos):
        if i % 10 == 0 and i != 0:
            output += "<br>"
        output += str(num) + " "
    return output      
  
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

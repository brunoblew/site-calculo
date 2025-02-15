from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    valor = None  # Definir a variável valor
    resultado_1 = None
    resultado_2 = None

    if request.method == "POST":
        try:
            valor = float(request.form["valor"])  # Obter o valor do formulário

            # Cálculos para a primeira coluna
            agua_1 = valor * 2
            acucar_1 = agua_1 * 0.2
            fermento_1 = valor * 3 * 0.0045

            # Cálculos para a segunda coluna
            agua_2 = valor * 3
            acucar_2 = agua_2 * 0.2
            fermento_2 = valor * 4 * 0.0045

            resultado_1 = {
                "agua": agua_1,
                "acucar": acucar_1,
                "fermento": fermento_1
            }

            resultado_2 = {
                "agua": agua_2,
                "acucar": acucar_2,
                "fermento": fermento_2
            }

        except ValueError:
            resultado_1 = resultado_2 = "Por favor, insira um valor numérico válido."

    return render_template("index.html", valor=valor, resultado_1=resultado_1, resultado_2=resultado_2)

if __name__ == "__main__":
    app.run(debug=True)

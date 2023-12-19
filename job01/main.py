from forex_python.converter import CurrencyRates
import json
import os

def convert_currency(amount, from_currency, to_currency, history):
    c = CurrencyRates()
    
    try:
        rate = c.get_rate(from_currency, to_currency)
        converted_amount = amount * rate
        print(f"{amount} {from_currency} équivaut à {converted_amount:.2f} {to_currency}")
        
        # Enregistrement de l'historique
        history_entry = {
            "amount": amount,
            "from_currency": from_currency,
            "to_currency": to_currency,
            "converted_amount": converted_amount
        }
        history.append(history_entry)
        
        return history

    except Exception as e:
        print(f"Erreur de conversion : {e}")
        return history

def save_history(history, filename="conversion_history.json"):
    with open(filename, "w") as file:
        json.dump(history, file)
    print(f"L'historique a été enregistré dans le fichier {filename}")

def load_history(filename="conversion_history.json"):
    if os.path.exists(filename):
        with open(filename, "r") as file:
            history = json.load(file)
        return history
    else:
        return []

def main():
    history = load_history()

    amount = float(input("Entrez le montant à convertir : "))
    from_currency = input("Entrez la devise d'origine (code ISO) : ").upper()
    to_currency = input("Entrez la devise de destination (code ISO) : ").upper()

    history = convert_currency(amount, from_currency, to_currency, history)

    save_history(history)

if __name__ == "__main__":
    main()
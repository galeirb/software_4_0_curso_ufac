import math

plays_json = {
    "hamlet": {"name": "Hamlet", "type": "tragedy"},
    "as-like": {"name": "As You Like It", "type": "comedy"},
    "othello": {"name": "Othello", "type": "tragedy"}
}

invoices_json = {
    "customer": "BigCo",
    "performances": [
        {"playID": "hamlet", "audience": 55},
        {"playID": "as-like", "audience": 35},
        {"playID": "othello", "audience": 40}
    ]
}


def calculate_amount(perf, play):
    if play['type'] == "tragedy":
        this_amount = 40000
        if perf['audience'] > 30:
            this_amount += 1000 * (perf['audience'] - 30)
        return this_amount
    elif play['type'] == "comedy":
        this_amount = 30000
        if perf['audience'] > 20:
            this_amount += 10000 + 500 * (perf['audience'] - 20)
        this_amount += 300 * perf['audience']
        return this_amount
    else:
        print('unknown type: ' + play['type'])


def statement(invoice, plays):
    total_amount = 0
    volume_credits = 0
    result = f"Statement for {invoice['customer']}\n"
    for perf in invoice['performances']:

        play = plays[perf['playID']]
        this_amount = calculate_amount(perf, play)

        # soma créditos por volume
        if perf['audience'] - 30 > 0:
            volume_credits += perf['audience'] - 30

        # soma um crédito extra para cada dez espectadores de comédia
        if "comedy" == play['type']:
            volume_credits += math.floor(perf['audience'] / 5)
        # exibe a linha para esta requisição
        result += f"    {play['name']}: R${str((this_amount / 100))}" + \
                  f" ({str(perf['audience'])} seats)\n"

        total_amount += this_amount
    

    result += f'Amount owed is R${str(total_amount / 100)}\n'
    result += f'You earned {str(volume_credits)} credits\n'
    return result

if __name__ == '__main__':
    print(statement(invoices_json, plays_json))
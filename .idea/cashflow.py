from flask import Flask, request, jsonify, render_template
from collections import defaultdict

app = Flask(__name__)

def add_edge(graph, u, v, w):
    graph[u][v] = graph[u].get(v, 0) + w

def min_cash_flow(graph):
    N = len(graph)
    amount = [0] * N
    for u in range(N):
        for v in range(N):
            amount[u] += (graph[v].get(u, 0) - graph[u].get(v, 0))
    
    print("Net Amounts: ", amount)
    
    def get_min(arr):
        min_index = 0
        for i in range(1, len(arr)):
            if arr[i] < arr[min_index]:
                min_index = i
        return min_index
    def get_max(arr):
        max_index = 0
        for i in range(1, len(arr)):
            if arr[i] > arr[max_index]:
                max_index = i
        return max_index
    def min_cash_flow_rec(amount):
        max_credit = get_max(amount)
        max_debit = get_min(amount)
        if amount[max_credit] == 0 and amount[max_debit] == 0:
            return []

        min_amount = min(-amount[max_debit], amount[max_credit])
        amount[max_credit] -= min_amount
        amount[max_debit] += min_amount

        print(f"Person {max_debit} pays Person {max_credit} an amount of {min_amount}")
        print("Updated Net Amounts: ", amount)

        result = [(max_debit, max_credit, min_amount)] + min_cash_flow_rec(amount)
        return result

    return min_cash_flow_rec(amount)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/minimize_cash_flow', methods=['POST'])
def minimize_cash_flow():
    data = request.json
    graph = defaultdict(dict)
    
    for transaction in data['transactions']:
        u, v, w = transaction
        add_edge(graph, u, v, w)
    
    print("Graph:", dict(graph))
    result = min_cash_flow(graph)
    print("Result:", result)
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)

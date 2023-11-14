import cirq

# Создаем схему на четырех кубитах
qubits = cirq.LineQubit.range(4)
circuit = cirq.Circuit()

# Применяем операции NOT к первым трём кубитам
circuit.append([cirq.X(qubits[i]) for i in range(3)])

# Создаем оракул для функции f(x1,x2,x3) = x1 ⊕ x2 ⊕ x3
circuit.append(cirq.CCX(qubits[0], qubits[1], qubits[3]))
circuit.append(cirq.CX(qubits[2], qubits[3]))

# Выводим схему
print(circuit)

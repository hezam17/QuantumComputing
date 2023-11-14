import cirq

# Функция для создания гейта Balanced
def balanced_gate(qubits):
    return [
        cirq.X(qubits[0]),
        cirq.CNOT(qubits[0], qubits[3]),
        cirq.CNOT(qubits[1], qubits[3]),
        cirq.CNOT(qubits[2], qubits[3]),
        cirq.X(qubits[0]),
        cirq.X(qubits[1]),
        cirq.X(qubits[2]),
    ]

# Функция для создания гейта Const
def const_gate(qubits):
    return [cirq.X(qubits[3])]

# Создаем схему на четырех кубитах
qubits = cirq.LineQubit.range(4)
circuit_balanced = cirq.Circuit(balanced_gate(qubits))
circuit_const = cirq.Circuit(const_gate(qubits))

# Выводим схемы
print("Balanced Gate Circuit:")
print(circuit_balanced)
print("\nConst Gate Circuit:")
print(circuit_const)

# Применяем алгоритм Дойча-Йожи с несколькими итерациями
iterations = 3  # Количество итераций алгоритма
for i in range(iterations):
    print(f"\nIteration {i + 1}:")
    result_balanced = cirq.Simulator().simulate(circuit_balanced)
    result_const = cirq.Simulator().simulate(circuit_const)

  # Выводим результаты
print("\nDeutsch-Jozsa Algorithm - Balanced Gate:")
for key, value in result_balanced.measurements.items():
    print(f"\t{key}: {value}")

print("\nDeutsch-Jozsa Algorithm - Const Gate:")
for key, value in result_const.measurements.items():
    print(f"\t{key}: {value}")

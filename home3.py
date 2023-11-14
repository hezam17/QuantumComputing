import cirq
import numpy as np

def increment_oracle(qubits):
    yield cirq.X(qubits[0])
    yield cirq.X(qubits[1])
    yield cirq.CCX(qubits[0], qubits[1], qubits[2])
    yield cirq.X(qubits[0])
    yield cirq.X(qubits[1])

def check_oracle(qubits):
    yield cirq.CCX(qubits[0], qubits[1], qubits[2])

def grover_algorithm(oracle, qubits, repetitions):
    circuit = cirq.Circuit()
    
    # Применяем преобразование Адамара ко всем кубитам
    circuit.append(cirq.H.on_each(*qubits))
    
    # Применяем оракул
    circuit.append(oracle)
    
    # Применяем преобразование Гровера
    for _ in range(repetitions):
        circuit.append(grover_iteration(qubits, oracle))
    
    # Добавляем измерения
    circuit.append(cirq.measure(*qubits, key='result'))
    
    return circuit

def grover_iteration(qubits, oracle):
    circuit = cirq.Circuit()
    
    # Применяем преобразование Адамара ко всем кубитам
    circuit.append(cirq.H.on_each(*qubits))
    
    # Применяем оракул
    circuit.append(oracle)
    
    # Применяем отражение по среднему
    circuit.append(reflection_about_average(qubits))
    
    return circuit

def reflection_about_average(qubits):
    return [
        cirq.H.on_each(*qubits),
        cirq.X.on_each(*qubits),
        cirq.CCX(qubits[0], qubits[1], qubits[2]),
        cirq.X.on_each(*qubits),
        cirq.H.on_each(*qubits)
    ]

# Создаем схему для оракула, добавляющего единицу
qubits_increment = cirq.LineQubit.range(3)
oracle_increment = cirq.Circuit(increment_oracle(qubits_increment))

# Создаем схему для оракула, проверяющего x+1 = 3
qubits_check = cirq.LineQubit.range(3)
oracle_check = cirq.Circuit(check_oracle(qubits_check))

# Запускаем алгоритм Гровера для нахождения решения уравнения x+1 = 3
qubits_grover = cirq.LineQubit.range(3)
grover_circuit = grover_algorithm(oracle_check, qubits_grover, repetitions=1)

# Выводим схемы
print("Oracle for Increment:")
print(oracle_increment)
print("\nOracle for Check:")
print(oracle_check)
print("\nGrover Circuit:")
print(grover_circuit)

# Запускаем схему Гровера на симуляторе
simulator = cirq.Simulator()
result = simulator.run(grover_circuit, repetitions=100)

# Выводим результаты
print("\nMeasurement Results:")
print(result.histogram(key='result'))

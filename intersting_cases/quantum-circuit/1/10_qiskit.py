from qiskit import QuantumRegister, ClassicalRegister
from qiskit import QuantumCircuit, execute, Aer
import numpy as np

shots = 8192

qc = QuantumCircuit()

q = QuantumRegister(8, 'q')
m6 = ClassicalRegister(1, 'm6')
m0 = ClassicalRegister(1, 'm0')
m3 = ClassicalRegister(1, 'm3')
m1 = ClassicalRegister(1, 'm1')
m2 = ClassicalRegister(1, 'm2')
m4 = ClassicalRegister(1, 'm4')
m5 = ClassicalRegister(1, 'm5')
m7 = ClassicalRegister(1, 'm7')

qc.add_register(q)
qc.add_register(m6)
qc.add_register(m0)
qc.add_register(m3)
qc.add_register(m1)
qc.add_register(m2)
qc.add_register(m4)
qc.add_register(m5)
qc.add_register(m7)

qc.x(q[0])
qc.h(q[1])
qc.x(q[2])
qc.x(q[3])
qc.x(q[4])
qc.x(q[5])
qc.h(q[7])
qc.measure(q[6], m6[0])
qc.h(q[1])
qc.h(q[2])
qc.h(q[4])
qc.h(q[5])
qc.h(q[7])
qc.measure(q[0], m0[0])
qc.measure(q[3], m3[0])
qc.measure(q[1], m1[0])
qc.measure(q[2], m2[0])
qc.measure(q[4], m4[0])
qc.measure(q[5], m5[0])
qc.measure(q[7], m7[0])
qc.x(q[0])
qc.h(q[1])
qc.x(q[2])
qc.x(q[3])
qc.x(q[4])
qc.h(q[5])
qc.h(q[6])
qc.h(q[7])
qc.h(q[1])
qc.h(q[2])
qc.h(q[3])
qc.h(q[4])
qc.h(q[7])
qc.measure(q[0], m0[0])
qc.measure(q[5], m5[0])
qc.measure(q[6], m6[0])
qc.h(q[2])
qc.h(q[4])
qc.measure(q[1], m1[0])
qc.measure(q[3], m3[0])
qc.measure(q[7], m7[0])
qc.measure(q[2], m2[0])
qc.measure(q[4], m4[0])

backend = Aer.get_backend('qasm_simulator')
job = execute(qc, backend=backend, shots=shots)
job_result = job.result()
print(job_result.get_counts(qc))

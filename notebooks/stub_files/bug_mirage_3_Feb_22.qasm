OPENQASM 2.0;
include "qelib1.inc";
qreg q[5];
creg c[5];
x q[1];
y q[3];
id q[3];
y q[4];
y q[0];
t q[3];
rx(2.713990594641554) q[1];
h q[0];
ry(4.933406064175189) q[0];
z q[1];
u2(2.8305702808704267,0.08334620905998126) q[4];
h q[2];
u1(1.5144076667907493) q[4];
rz(1.0892822437043135) q[4];
u1(1.9585384533701249) q[2];
rz(5.292231320196365) q[0];
u1(3.756716362028796) q[4];
u2(2.442131435811337,1.7049362495591496) q[2];
t q[1];
rx(5.040352282937607) q[1];
measure q -> c;
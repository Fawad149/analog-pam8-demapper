v {xschem version=3.4.8RC file_version=1.3}
G {}
K {}
V {}
S {}
F {}
E {}
N -50 -200 110 -200 {lab=vdd}
N 110 -200 110 -150 {lab=vdd}
N 40 -150 70 -150 {lab=ibias}
N -50 -200 -50 -150 {lab=vdd}
N 50 20 110 20 {lab=#net1}
N -180 20 -140 20 {lab=#net2}
N 110 20 110 80 {lab=#net1}
N -50 20 -10 20 {lab=#net3}
N -50 -120 -50 20 {lab=#net3}
N -80 20 -50 20 {lab=#net3}
N -90 230 70 230 {lab=#net4}
N 110 150 260 150 {lab=#net5}
N 110 110 110 150 {lab=#net5}
N 360 230 440 230 {lab=#net5}
N 260 170 360 170 {lab=#net5}
N 260 150 260 170 {lab=#net5}
N 360 170 360 230 {lab=#net5}
N 300 230 360 230 {lab=#net5}
N 110 -200 480 -200 {lab=vdd}
N 480 -200 480 60 {lab=vdd}
N -180 160 -90 160 {lab=#net4}
N -90 160 -90 230 {lab=#net4}
N -140 230 -90 230 {lab=#net4}
N 260 340 480 340 {lab=gnd}
N -180 340 110 340 {lab=gnd}
N 110 340 260 340 {lab=gnd}
N -180 20 -180 80 {lab=#net2}
N 40 -150 40 -120 {lab=ibias}
N -10 -150 40 -150 {lab=ibias}
N 40 -120 110 -120 {lab=ibias}
N -180 230 -180 340 {lab=gnd}
N -180 160 -180 200 {lab=#net4}
N -180 110 -180 160 {lab=#net4}
N 110 230 110 340 {lab=gnd}
N 110 150 110 200 {lab=#net5}
N 260 230 260 340 {lab=gnd}
N 480 230 480 340 {lab=gnd}
N 480 120 480 200 {lab=vout}
N 260 170 260 200 {lab=#net5}
C {sg13g2_pr/sg13_lv_pmos.sym} -30 -150 0 1 {name=M1
l=0.14u
w=1u
ng=1
m=1
mm_ok=1
model=sg13_lv_pmos
spiceprefix=X
}
C {sg13g2_pr/sg13_lv_pmos.sym} 90 -150 0 0 {name=M3
l=0.14u
w=1u
ng=1
m=1
mm_ok=1
model=sg13_lv_pmos
spiceprefix=X
}
C {sg13g2_pr/sg13_lv_pmos.sym} -200 80 0 0 {name=M4
l=0.14u
w=1u
ng=1
m=1
mm_ok=1
model=sg13_lv_pmos
spiceprefix=X
}
C {sg13g2_pr/sg13_lv_pmos.sym} 130 80 0 1 {name=M5
l=0.14u
w=1u
ng=1
m=1
mm_ok=1
model=sg13_lv_pmos
spiceprefix=X
}
C {res.sym} -110 20 3 0 {name=R1
value=500
footprint=1206
device=resistor
m=1}
C {res.sym} 20 20 3 0 {name=R2
value=500
footprint=1206
device=resistor
m=1}
C {res.sym} 480 90 2 0 {name=R3
value=3k
footprint=1206
device=resistor
m=1}
C {ipin.sym} 70 -200 1 0 {name=p1 lab=vdd}
C {ipin.sym} 190 340 3 0 {name=p3 lab=gnd}
C {opin.sym} 480 150 0 0 {name=p4 lab=vout}
C {ipin.sym} 110 -120 3 0 {name=p5 lab=ibias}
C {ipin.sym} 150 80 2 0 {name=p2 lab=Vin}
C {ipin.sym} -220 80 0 0 {name=p6 lab=vref}
C {sg13g2_pr/npn13G2v.sym} -160 230 0 1 {name=Q1
model=npn13G2v
spiceprefix=X
 Nx=1
 El=1.0
  mm_ok=1
 }
C {sg13g2_pr/npn13G2.sym} 90 230 0 0 {name=Q2
model=npn13G2
 spiceprefix=X
 Nx=1
  mm_ok=1
 }
C {sg13g2_pr/npn13G2.sym} 280 230 0 1 {name=Q3
model=npn13G2
 spiceprefix=X
 Nx=1
  mm_ok=1
 }
C {sg13g2_pr/npn13G2.sym} 460 230 0 0 {name=Q4
model=npn13G2
 spiceprefix=X
 Nx=1
  mm_ok=1
 }

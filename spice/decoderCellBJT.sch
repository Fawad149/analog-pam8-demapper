v {xschem version=3.4.8RC file_version=1.3}
G {}
K {}
V {}
S {}
F {}
E {}
N 50 -40 210 -40 {lab=vdd}
N 210 -40 210 10 {lab=vdd}
N 140 10 170 10 {lab=ibias}
N 50 -40 50 10 {lab=vdd}
N 150 180 210 180 {lab=#net1}
N -80 180 -40 180 {lab=#net2}
N 210 180 210 240 {lab=#net1}
N 50 180 90 180 {lab=#net3}
N 50 40 50 180 {lab=#net3}
N 20 180 50 180 {lab=#net3}
N 10 390 170 390 {lab=#net4}
N 210 310 360 310 {lab=#net5}
N 210 270 210 310 {lab=#net5}
N 460 390 540 390 {lab=#net5}
N 360 330 460 330 {lab=#net5}
N 360 310 360 330 {lab=#net5}
N 460 330 460 390 {lab=#net5}
N 400 390 460 390 {lab=#net5}
N 210 -40 580 -40 {lab=vdd}
N 580 -40 580 220 {lab=vdd}
N -80 320 10 320 {lab=#net4}
N 10 320 10 390 {lab=#net4}
N -40 390 10 390 {lab=#net4}
N 360 500 580 500 {lab=gnd}
N -80 500 210 500 {lab=gnd}
N 210 500 360 500 {lab=gnd}
N -80 180 -80 240 {lab=#net2}
N 140 10 140 40 {lab=ibias}
N 90 10 140 10 {lab=ibias}
N 140 40 210 40 {lab=ibias}
N -80 390 -80 500 {lab=gnd}
N -80 320 -80 360 {lab=#net4}
N -80 270 -80 320 {lab=#net4}
N 210 390 210 500 {lab=gnd}
N 210 310 210 360 {lab=#net5}
N 360 390 360 500 {lab=gnd}
N 580 390 580 500 {lab=gnd}
N 580 280 580 360 {lab=vout}
N 360 330 360 360 {lab=#net5}
C {sg13g2_pr/sg13_lv_pmos.sym} 70 10 0 1 {name=M1
l=0.14u
w=0.15u
ng=1
m=1
mm_ok=1
model=sg13_lv_pmos
spiceprefix=X
}
C {sg13g2_pr/sg13_lv_pmos.sym} 190 10 0 0 {name=M3
l=0.14u
w=0.15u
ng=1
m=1
mm_ok=1
model=sg13_lv_pmos
spiceprefix=X
}
C {sg13g2_pr/sg13_lv_pmos.sym} -100 240 0 0 {name=M4
l=0.14u
w=0.15u
ng=1
m=1
mm_ok=1
model=sg13_lv_pmos
spiceprefix=X
}
C {sg13g2_pr/sg13_lv_pmos.sym} 230 240 0 1 {name=M5
l=0.14u
w=0.15u
ng=1
m=1
mm_ok=1
model=sg13_lv_pmos
spiceprefix=X
}
C {res.sym} -10 180 3 0 {name=R1
value=500
footprint=1206
device=resistor
m=1}
C {res.sym} 120 180 3 0 {name=R2
value=500
footprint=1206
device=resistor
m=1}
C {res.sym} 580 250 2 0 {name=R3
value=3k
footprint=1206
device=resistor
m=1}
C {ipin.sym} 170 -40 1 0 {name=p1 lab=vdd}
C {ipin.sym} 290 500 3 0 {name=p3 lab=gnd}
C {opin.sym} 580 310 0 0 {name=p4 lab=vout}
C {ipin.sym} 210 40 3 0 {name=p5 lab=ibias}
C {ipin.sym} 250 240 2 0 {name=p2 lab=Vin}
C {ipin.sym} -120 240 0 0 {name=p6 lab=vref}
C {sg13g2_pr/npn13G2.sym} 190 390 0 0 {name=Q2
model=npn13G2
 spiceprefix=X
 Nx=1
  mm_ok=1
 }
C {sg13g2_pr/npn13G2.sym} 380 390 0 1 {name=Q3
model=npn13G2
 spiceprefix=X
 Nx=1
  mm_ok=1
 }
C {sg13g2_pr/npn13G2.sym} 560 390 0 0 {name=Q4
model=npn13G2
 spiceprefix=X
 Nx=1
  mm_ok=1
 }
C {sg13g2_pr/npn13G2.sym} -60 390 0 1 {name=Q1
model=npn13G2
 spiceprefix=X
 Nx=1
  mm_ok=1
 }

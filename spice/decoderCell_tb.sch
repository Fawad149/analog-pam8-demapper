v {xschem version=3.4.8RC file_version=1.3}
G {}
K {}
V {}
S {}
F {}
E {}
B 2 210 -250 1010 150 {flags=graph
y1=1.5
y2=1.6
ypos1=0
ypos2=2
divy=5
subdivy=1
unity=1
x1=0
x2=0.64
divx=5
subdivx=1
xlabmag=1.0
ylabmag=1.0
node=vout
dataset=-1
unitx=1
logx=0
logy=0
rawfile=$netlist_dir/decoderCell.raw
autoload=1
color=4}
B 2 210 160 1010 560 {flags=graph
y1=5.6e-12
y2=1.2e-05
ypos1=0
ypos2=2
divy=5
subdivy=1
unity=1
x1=0
x2=0.64
divx=5
subdivx=1
xlabmag=1.0
ylabmag=1.0
node=iout
color=4
dataset=-1
unitx=1
logx=0
logy=0
autoload=1
rawfile=$netlist_dir/decoderCell.raw}
C {decoderCell.sym} -10 -10 0 0 {name=x1}
C {vsource.sym} -430 120 0 0 {name=V1 value=1.6 savecurrent=false}
C {vsource.sym} -360 120 0 0 {name=V2 value=0.32 savecurrent=false}
C {vsource.sym} -300 120 0 0 {name=V3 value=0.32 savecurrent=false}
C {isource.sym} -230 120 0 0 {name=I0 value=100u}
C {gnd.sym} -160 30 0 0 {name=l1 lab=GND}
C {gnd.sym} -300 150 0 0 {name=l2 lab=GND}
C {gnd.sym} -360 150 0 0 {name=l3 lab=GND}
C {gnd.sym} -430 150 0 0 {name=l4 lab=GND}
C {gnd.sym} -230 150 0 0 {name=l5 lab=GND}
C {lab_pin.sym} -430 90 0 0 {name=p1 sig_type=std_logic lab=VDD}
C {lab_pin.sym} -360 90 0 0 {name=p2 sig_type=std_logic lab=Vin}
C {lab_pin.sym} -300 90 0 0 {name=p3 sig_type=std_logic lab=Vref}
C {lab_pin.sym} -230 90 0 0 {name=p4 sig_type=std_logic lab=ibias}
C {lab_pin.sym} -160 -30 0 0 {name=p5 sig_type=std_logic lab=ibias}
C {lab_pin.sym} -160 -10 0 0 {name=p6 sig_type=std_logic lab=Vref}
C {lab_pin.sym} -160 -50 0 0 {name=p7 sig_type=std_logic lab=VDD}
C {lab_pin.sym} -160 10 0 0 {name=p8 sig_type=std_logic lab=Vin}
C {opin.sym} 140 -50 0 0 {name=p9 lab=vout}
C {devices/code_shown.sym} -100 130 0 0 {name=MODEL only_toplevel=true
format="tcleval( @value )"
value="
.lib cornerMOShv.lib mos_tt
.lib cornerHBT.lib hbt_typ
.lib cornerRES.lib res_typ
.lib cornerDIO.lib dio_tt
"}
C {devices/code_shown.sym} -580 -140 0 0 {name=NGSPICE
only_toplevel=true
value="
.control
save all
op
dc V2 0 0.64 1m
wrdata bjt_min.txt v(vout) v(x1.net4) v(x1.net5)
.endc
" }
C {launcher.sym} 280 590 0 0 {name=h5
descr="load waves" 
tclcommand="xschem raw_read $netlist_dir/untitled.raw tran"
}

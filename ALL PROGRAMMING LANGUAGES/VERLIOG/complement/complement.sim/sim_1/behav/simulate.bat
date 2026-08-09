@echo off
set xv_path=D:\\Vivado\\Vivado\\2015.4\\bin
call %xv_path%/xsim comptb_behav -key {Behavioral:sim_1:Functional:comptb} -tclbatch comptb.tcl -log simulate.log
if "%errorlevel%"=="0" goto SUCCESS
if "%errorlevel%"=="1" goto END
:END
exit 1
:SUCCESS
exit 0

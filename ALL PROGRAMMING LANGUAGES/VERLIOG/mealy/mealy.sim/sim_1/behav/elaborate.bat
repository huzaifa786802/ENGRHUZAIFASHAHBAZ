@echo off
set xv_path=D:\\Vivado1\\Vivado\\2015.4\\bin
call %xv_path%/xelab  -wto f81d372df2994d1ba390748140e29a1a -m64 --debug typical --relax --mt 2 -L xil_defaultlib -L unisims_ver -L unimacro_ver -L secureip --snapshot TestBench_behav xil_defaultlib.TestBench xil_defaultlib.glbl -log elaborate.log
if "%errorlevel%"=="0" goto SUCCESS
if "%errorlevel%"=="1" goto END
:END
exit 1
:SUCCESS
exit 0

@echo off
set xv_path=D:\\Vivado\\Vivado\\2015.4\\bin
call %xv_path%/xelab  -wto 0a791b0bce3d4c89a49e2a275dfdefaa -m64 --debug typical --relax --mt 2 -L xil_defaultlib -L unisims_ver -L unimacro_ver -L secureip --snapshot comptb_behav xil_defaultlib.comptb xil_defaultlib.glbl -log elaborate.log
if "%errorlevel%"=="0" goto SUCCESS
if "%errorlevel%"=="1" goto END
:END
exit 1
:SUCCESS
exit 0

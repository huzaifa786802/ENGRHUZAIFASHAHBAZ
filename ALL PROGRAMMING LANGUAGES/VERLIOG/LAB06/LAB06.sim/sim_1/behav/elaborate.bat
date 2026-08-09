@echo off
set xv_path=D:\\Vivado\\Vivado\\2015.4\\bin
call %xv_path%/xelab  -wto 0ae5d76285d74e84a9001fb62e231fb8 -m64 --debug typical --relax --mt 2 -L xil_defaultlib -L unisims_ver -L unimacro_ver -L secureip --snapshot CODE1_behav xil_defaultlib.CODE1 xil_defaultlib.glbl -log elaborate.log
if "%errorlevel%"=="0" goto SUCCESS
if "%errorlevel%"=="1" goto END
:END
exit 1
:SUCCESS
exit 0

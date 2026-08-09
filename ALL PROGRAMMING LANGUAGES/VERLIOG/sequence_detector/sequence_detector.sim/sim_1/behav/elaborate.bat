@echo off
set xv_path=D:\\Vivado1\\Vivado\\2015.4\\bin
call %xv_path%/xelab  -wto 4e77030b74004b7ebb22d4b08c9ee0b7 -m64 --debug typical --relax --mt 2 -L xil_defaultlib -L unisims_ver -L unimacro_ver -L secureip --snapshot sequence_detector_tb_behav xil_defaultlib.sequence_detector_tb xil_defaultlib.glbl -log elaborate.log
if "%errorlevel%"=="0" goto SUCCESS
if "%errorlevel%"=="1" goto END
:END
exit 1
:SUCCESS
exit 0

Clamshell PCB Project - Initial KiCad Skeleton
=============================================

What is included:
- README.txt (this file)
- BOM.csv (initial parts list with suggested components)
- block_diagram.pdf (block-level circuit diagram)
- project_skeleton/ (KiCad project skeleton with placeholder files)

Design defaults used for this initial revision (you can request changes):
1) GSM/cellular: NOT included
2) Battery: Single thin Li-Po (~1400 mAh)
3) USB-C: PD-capable charger (TI BQ25895 recommended)
4) Display interface: MIPI-DSI
5) MCU: ESP32-S3 (WROOM series module)
6) PCB form-factor: two rigid halves joined by a flex region (rigid-flex)
7) Board dimensions: 85 mm x 55 mm footprint (two halves in a clamshell)

Next actions I will take after your review:
- Replace placeholder schematic with detailed netlist and symbols for each selected component.
- Add display connector pinouts once you confirm exact display module P/Ns.
- Create full PCB layout including rigid-flex bend area and high-speed routing for MIPI lanes.
- Provide Gerbers, BOM, Pick&Place files, and datasheets pack.

If you want to change defaults (add GSM, use SPI display, split battery, or remove PD), reply and I'll update and re-generate files.


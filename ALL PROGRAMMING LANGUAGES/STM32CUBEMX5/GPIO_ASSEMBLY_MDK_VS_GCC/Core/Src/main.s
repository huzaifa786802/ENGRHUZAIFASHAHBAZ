; Assuming the use of STM32 microcontroller and GPIO port A
; Base address of GPIOA
.equ GPIOA_BASE, 0x48000000
; Register offsets
.equ GPIOA_MODER_OFFSET, 0x00  ; Mode register offset
.equ GPIOA_OTYPER_OFFSET, 0x04 ; Output type register offset
.equ GPIOA_OSPEEDR_OFFSET, 0x08 ; Output speed register offset
.equ GPIOA_PUPDR_OFFSET, 0x0C  ; Pull-up/pull-down register offset
; Clock enable register (specific to microcontroller family)
.equ RCC_AHBENR, 0x40021014     ; RCC AHB peripheral clock enable register
.equ RCC_IOPAEN, 0x00020000     ; Bit for enabling GPIOA clock
; Addresses
.equ GPIOA_MODER, GPIOA_BASE + GPIOA_MODER_OFFSET
.equ GPIOA_OTYPER, GPIOA_BASE + GPIOA_OTYPER_OFFSET
.equ GPIOA_OSPEEDR, GPIOA_BASE + GPIOA_OSPEEDR_OFFSET
.equ GPIOA_PUPDR, GPIOA_BASE + GPIOA_PUPDR_OFFSET
.global main
.syntax unified
main:
    ; Enable clock for GPIOA
    LDR R0, =RCC_AHBENR
    LDR R1, [R0]                ; Load current RCC_AHBENR value
    ORR R1, R1, #RCC_IOPAEN     ; Set bit for GPIOA clock enable
    STR R1, [R0]                ; Write back to RCC_AHBENR
    ; Configure GPIOA pin 0 as output
    LDR R0, =GPIOA_MODER
    LDR R1, [R0]                ; Load current GPIOA_MODER value
    BIC R1, R1, #(0x3 << (0 * 2)); Clear mode bits for pin 0
    ORR R1, R1, #(0x1 << (0 * 2)); Set mode bits to output (01)
    STR R1, [R0]                ; Write back to GPIOA_MODER
    ; Configure GPIOA pin 0 as push-pull (default, so no need to set GPIOA_OTYPER)
    ; Set GPIO speed to medium for pin 0 (01)
    LDR R0, =GPIOA_OSPEEDR
    LDR R1, [R0]                ; Load current GPIOA_OSPEEDR value
    BIC R1, R1, #(0x3 << (0 * 2)); Clear speed bits for pin 0
    ORR R1, R1, #(0x1 << (0 * 2)); Set speed bits to medium speed (01)
    STR R1, [R0]                ; Write back to GPIOA_OSPEEDR
    ; Disable pull-up/pull-down for pin 0 (00)
    LDR R0, =GPIOA_PUPDR
    LDR R1, [R0]                ; Load current GPIOA_PUPDR value
    BIC R1, R1, #(0x3 << (0 * 2)); Clear pull-up/pull-down bits for pin 0
    STR R1, [R0]                ; Write back to GPIOA_PUPDR
    ; End of configuration
    B . ; Infinite loop to keep the program running

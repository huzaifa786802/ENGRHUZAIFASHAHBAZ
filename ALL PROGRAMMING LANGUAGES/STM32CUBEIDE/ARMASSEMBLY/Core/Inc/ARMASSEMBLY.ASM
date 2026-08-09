    .syntax unified
    .cpu cortex-m4
    .thumb
    .equ GPIOA_BASE, 0x40020000       // Base address of GPIOA
    .equ RCC_BASE, 0x40023800         // Base address of RCC
    .equ RCC_AHB1ENR, RCC_BASE + 0x30 // RCC AHB1 peripheral clock enable register
    .equ GPIOA_MODER, GPIOA_BASE + 0x00 // GPIOA mode register
    .equ GPIOA_ODR, GPIOA_BASE + 0x14  // GPIOA output data register
    .equ LED_PIN, 5                   // Pin number for the LED

    .global _start

_start:
    // Enable GPIOA clock
    LDR R0, =RCC_AHB1ENR
    LDR R1, [R0]
    ORR R1, R1, #1   // Set bit 0 to enable GPIOA clock
    STR R1, [R0]

    // Set GPIOA pin 5 to output mode
    LDR R0, =GPIOA_MODER
    LDR R1, [R0]
    LSL R2, #10      // LED_PIN * 2 because each pin has 2 bits in MODER
    ORR R1, R1, #(1 << R2)
    STR R1, [R0]

    // Main loop: toggle LED
loop:
    // Toggle GPIOA pin 5
    LDR R0, =GPIOA_ODR
    LDR R1, [R0]
    EOR R1, R1, #(1 << LED_PIN)
    STR R1, [R0]

    // Delay
    BL delay

    B loop

delay:
    // Simple delay loop
    MOV R2, #500000
delay_loop:
    SUBS R2, R2, #1
    BNE delay_loop
    BX LR

    .end

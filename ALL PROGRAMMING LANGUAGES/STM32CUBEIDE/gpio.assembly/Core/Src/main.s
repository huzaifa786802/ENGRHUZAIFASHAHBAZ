    .section .text
    .global _start
_start:
    /* Set up the stack pointer */
    LDR     R0, =_stack_top
    MOV     SP, R0
    /* Enable GPIO clock */
    LDR     R0, =RCC_AHB1ENR
    LDR     R1, =0x00000001        /* Enable clock for GPIOA (bit 0) */
    STR     R1, [R0]
    /* Set GPIO pin mode (e.g., output) */
    LDR     R0, =GPIOA_MODER
    LDR     R1, [R0]
    BIC     R1, R1, #(0x3 << (2 * 5))  /* Clear mode for pin PA5 */
    ORR     R1, R1, #(0x1 << (2 * 5))  /* Set mode to output for PA5 */
    STR     R1, [R0]
    /* Turn on LED connected to PA5 */
    LDR     R0, =GPIOA_ODR
    LDR     R1, [R0]
    ORR     R1, R1, #(0x1 << 5)    /* Set PA5 high */
    STR     R1, [R0]
loop:
    B loop

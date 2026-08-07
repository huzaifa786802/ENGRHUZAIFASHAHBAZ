#include <reg51.h>
#include <string.h>
// LCD pin definitions
sbit RS = P2^0;
sbit EN = P2^1;
sbit KEY1 = P1^0;  // Start/Resume key
sbit KEY2 = P1^1;  // Pause/Reset key
// Global variables for time
unsigned char seconds = 0;
unsigned char minutes = 0;
unsigned char hours = 0;
unsigned char running = 0;
unsigned int ms_count = 0;
// Function prototypes
void init_timer0(void);
void delay_ms(unsigned int ms);
void lcd_cmd(unsigned char cmd);
void lcd_data(unsigned char dat);
void lcd_init(void);
void lcd_string(unsigned char *str);
void update_display(void);
void check_keys(void);
// Timer0 ISR
void timer0_isr(void) interrupt 1 {
    TH0 = 0xFC;   // Reload timer for 1ms delay
    TL0 = 0x66;   
    ms_count++;
    if(ms_count >= 1000 && running) {  // 1 second has passed
        ms_count = 0;
        seconds++;
        if(seconds >= 60) {
            seconds = 0;
            minutes++;
            if(minutes >= 60) {
                minutes = 0;
                hours++;
                if(hours >= 24) {
                    hours = 0;
                }
            }
        }
        update_display();
    }
}
// Initialize Timer0
void init_timer0(void) {
    TMOD = 0x01;    // Timer0 in mode 1 (16-bit)
    TH0 = 0xFC;     // Initial values for 1ms delay
    TL0 = 0x66;
    ET0 = 1;        // Enable Timer0 interrupt
    EA = 1;         // Enable global interrupts
    TR0 = 1;        // Start Timer0
}
// Millisecond delay function
void delay_ms(unsigned int ms) {
    unsigned int i;
    for(i = 0; i < ms; i++) {
        TH0 = 0xFC;   // 1ms delay values
        TL0 = 0x66;
        TR0 = 1;
        while(!TF0);
        TR0 = 0;
        TF0 = 0;
    }
}
// LCD functions
void lcd_cmd(unsigned char cmd) {
    P0 = cmd;
    RS = 0;
    EN = 1;
    delay_ms(5);
    EN = 0;
}
void lcd_data(unsigned char dat) {
    P0 = dat;
    RS = 1;
    EN = 1;
    delay_ms(5);
    EN = 0;
}
void lcd_init(void) {
    lcd_cmd(0x38);    // 2 lines, 5x7 matrix
    lcd_cmd(0x0C);    // Display ON, cursor OFF
    lcd_cmd(0x01);    // Clear display
    lcd_cmd(0x80);    // Move cursor to beginning of first line
}
void lcd_string(unsigned char *str) {
    while(*str) {
        lcd_data(*str++);
    }
}
// Update LCD display
void update_display(void) {
    unsigned char time_str[9];
    lcd_cmd(0x85);    // Position cursor at center of first line
    // Format time string
    time_str[0] = (hours/10) + '0';
    time_str[1] = (hours%10) + '0';
    time_str[2] = ':';
    time_str[3] = (minutes/10) + '0';
    time_str[4] = (minutes%10) + '0';
    time_str[5] = ':';
    time_str[6] = (seconds/10) + '0';
    time_str[7] = (seconds%10) + '0';
    time_str[8] = '\0';   
    lcd_string(time_str);
}
// Check key inputs
void check_keys(void) {
    if(!KEY1) {           // Start/Resume
        delay_ms(20);     // Debounce
        if(!KEY1) {
            running = 1;
            while(!KEY1);  // Wait for key release
        }
    }   
    if(!KEY2) {           // Pause/Reset
        delay_ms(20);     // Debounce
        if(!KEY2) {
            if(running) {  // If running, pause first
                running = 0;
            } else {      // If already paused, reset
                hours = 0;
                minutes = 0;
                seconds = 0;
                update_display();
            }
            while(!KEY2);  // Wait for key release
        }
    }
}
// Main function
void main(void) {
    // Initialize LCD and Timer
    lcd_init();
    init_timer0();
    // Display initial time
    update_display();  
    // Main loop
    while(1) {
        check_keys();
    }
}
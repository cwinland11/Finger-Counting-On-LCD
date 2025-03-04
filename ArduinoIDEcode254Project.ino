#include <LiquidCrystal.h>

// Initialize the LCD library with the numbers of the interface pins:
// For example, RS = 7, E = 8, D4 = 9, D5 = 10, D6 = 11, D7 = 12
LiquidCrystal lcd(7, 8, 9, 10, 11, 12);

void setup() {
  // Set up the LCD's columns and rows:
  lcd.begin(16, 2);
  lcd.print("Number:       :)");
  
  // Start serial communication at 9600 baud
  Serial.begin(9600);
}

void loop() {
  // Check if data is available in the serial buffer
  if (Serial.available() > 0) {
    // Read a single character from the serial port (the predicted digit)
    char predictedDigit = Serial.read();
    
   
    
    // Clear the LCD and display the prediction only if it's different from the last one
    
      lcd.setCursor(9, 0);  // Set cursor to 10th digit
      lcd.print("    ");  // Clear the previous value
      lcd.setCursor(9, 0);  // Set cursor back to 10th digit
      lcd.print(predictedDigit);  // Print the new predicted digit
    }
  }


import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

public class SimpleCalculator {
    
    public static void main(String[] args) {
        // 1. Create the Window (Frame)
        JFrame frame = new JFrame("CA Suite: Engineering Calculator");
        frame.setSize(400, 300);
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setLayout(new FlowLayout());

        // 2. Create Components
        JLabel label = new JLabel("Enter Value (mm):");
        JTextField inputField = new JTextField(10);
        JButton calculateBtn = new JButton("Calculate Stress");
        JLabel resultLabel = new JLabel("Result: ---");

        // 3. Add Logic (Action Listener)
        calculateBtn.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                try {
                    // Parse input
                    double val = Double.parseDouble(inputField.getText());
                    
                    // Fake Engineering Calculation (Stress = Force / Area)
                    double result = val * 5.5; 
                    
                    // Update UI
                    resultLabel.setText("Stress: " + result + " MPa");
                } catch (NumberFormatException ex) {
                    resultLabel.setText("Error: Invalid Number");
                }
            }
        });

        // 4. Assemble the Interface
        frame.add(label);
        frame.add(inputField);
        frame.add(calculateBtn);
        frame.add(resultLabel);

        // 5. Show it
        frame.setVisible(true);
    }
}
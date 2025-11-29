#include <iostream>
#include <string>

// --- CLASS DEFINITION ---
class KinematicsSolver {
private:
    double velocity;
    double acceleration;
    double time;

public:
    // Constructor
    KinematicsSolver(double v, double a, double t) {
        velocity = v;
        acceleration = a;
        time = t;
    }

    // Method to calculate Displacement: d = vit + 0.5at^2
    double calculateDisplacement() {
        return (velocity * time) + (0.5 * acceleration * time * time);
    }

    // Method to calculate Final Velocity: vf = vi + at
    double calculateFinalVelocity() {
        return velocity + (acceleration * time);
    }

    void printReport() {
        std::cout << "--- KINEMATICS REPORT ---" << std::endl;
        std::cout << "Initial Velocity: " << velocity << " m/s" << std::endl;
        std::cout << "Acceleration:     " << acceleration << " m/s^2" << std::endl;
        std::cout << "Time Elapsed:     " << time << " s" << std::endl;
        std::cout << "-------------------------" << std::endl;
        std::cout << "Displacement:     " << calculateDisplacement() << " m" << std::endl;
        std::cout << "Final Velocity:   " << calculateFinalVelocity() << " m/s" << std::endl;
        std::cout << "-------------------------" << std::endl;
    }
};

// --- MAIN EXECUTION ---
int main(int argc, char* argv[]) {
    // Default values (v=0, a=9.81, t=10.0)
    double v = 0.0; 
    double a = 9.81; 
    double t = 10.0; 

    // Instantiate and Solve
    KinematicsSolver solver(v, a, t);
    solver.printReport();

    return 0;
}
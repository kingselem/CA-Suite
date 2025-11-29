import argparse
import logging
import sys
import json

# --- CONFIGURATION ---
# Set up professional logging (better than just print statements)
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    datefmt='%H:%M:%S'
)
logger = logging.getLogger(__name__)

def main(args):
    """
    Main logic engine.
    Args:
        args (Namespace): Parsed command line arguments.
    """
    logger.info("--- Starting Engineering Script ---")
    
    # 1. Receive Input
    logger.info(f"Input Value Received: {args.input_val}")
    
    # 2. Perform Calculation 
    # (Example: Calculating a Factor of Safety or converting units)
    # For now, we just multiply by 2.5 as a placeholder.
    result = args.input_val * 2.5 
    
    # 3. Output results
    logger.info(f"Calculation Complete. Result: {result}")
    logger.info("--- Operation Finished Successfully ---")

if __name__ == "__main__":
    # Initialize Argument Parser
    parser = argparse.ArgumentParser(
        description="CA Suite: Standard Engineering CLI Template"
    )

    # Define Inputs (This allows you to type flags like -i 50 later)
    parser.add_argument(
        "-i", "--input", 
        dest="input_val", 
        type=float, 
        default=10.0,
        help="Input value (e.g., length, force, ratio)"
    )

    # Parse arguments and run main
    args = parser.parse_args()
    main(args)
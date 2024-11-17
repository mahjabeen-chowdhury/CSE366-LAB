import random,os

class StudentIDManager:
    def __init__(self, path):
        self.path = path
        self.student_id_counters = []
        self.student_id_insert_read()

    def student_id_insert_read(self):
        directory = os.path.dirname(self.path)
        if directory and not os.path.exists(directory):
            os.makedirs(directory)

        if not os.path.exists(self.path):
            with open(self.path, 'w') as file:
    # Generate 200 student IDs for each semester with an initial counter of 0 USE TUPPLE FIRST ONE ID AND 2ND ONE COUNTER 
                for i in range(1, 200):
                    student_id = f"2021-1-60-{i:03}"
                    file.write(f"{student_id},0\n")  
                for i in range(1, 200):
                    student_id = f"2021-2-60-{i:03}"
                    file.write(f"{student_id},0\n")  
                for i in range(1, 200):
                    student_id = f"2021-3-60-{i:03}"
                    file.write(f"{student_id},0\n")  
            print(f"Specific roll numbers generated and saved to {self.path}.")
        else:
            print(f"File '{self.path}' already exists. No new rolls generated.")

    def get_random_student_ids_with_viva_count(self, num_to_pick):
        with open(self.path, 'r') as file:
            self.student_id_counters = [line.strip().split(',') for line in file.readlines()]

        # Filter for IDs with  counter of 0 (not USED  yet)
        available_ids = [entry for entry in self.student_id_counters if entry[1] == '0']
        
        if num_to_pick > len(available_ids):
            print("You requested more IDs than are available in the file.")

        # Select random IDs and update their counter to 1
        selected_ids = random.choices(available_ids, num_to_pick)

        for student_id, _ in selected_ids:
            for i in range(len(self.student_id_counters)):
                if self.student_id_counters[i][0] == student_id:
                    viva_count = int(self.student_id_counters[i][1]) + 1
                    self.student_id_counters[i][1] = str(viva_count)  # Increment  counter

        # Write back to the file with updated  counters
        with open(self.path, 'w') as file:
            for student_id, viva_count in self.student_id_counters:
                file.write(f"{student_id},{viva_count}\n")
        
        return selected_ids  # Only returning the selected IDs

    def reset_viva_counts(self):
        # Reset  counters for all student IDs to 0
        with open(self.path, 'r') as file:
            self.student_id_counters = [line.strip().split(',') for line in file.readlines()]

        # Update all  counters to 0
        for i in range(len(self.student_id_counters)):
            self.student_id_counters[i][1] = '0'  # Set  counter to 0

        # Write back to the file with reset counters
        with open(self.path, 'w') as file:
            for student_id, viva_count in self.student_id_counters:
                file.write(f"{student_id},{viva_count}\n")
        print(f"All student ID viva counters have been reset to 0 in {self.path}.")

# Main program
if __name__ == "__main__":
    path = "C:\\CSE366-AI-SEC-1-ID-2019-3-60-006\\lab1\\student_id.txt"
    manager = StudentIDManager(path)

    while True:
        user_input = input("How many random student IDs would you like to pick (between 1 and 10)? (Type 'exit' to quit) ")
        if user_input.lower() == 'exit':
            manager.reset_viva_counts()  # Reset  counters to 0 before exiting
            print("Exiting the program and resetting student ID  counters to 0.")
            break
        try:
            num_to_pick = int(user_input)
            if 1 <= num_to_pick <= 10:
                selected_ids = manager.get_random_student_ids_with_viva_count(num_to_pick)
                print(f"Randomly selected student IDs: {selected_ids}")
            else:
                print("Please enter a number between 1 and 10.")
        except ValueError:
            print("Invalid input. Please enter a numeric value or 'exit' to quit.")
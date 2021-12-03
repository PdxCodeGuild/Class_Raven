import random, json

class StudentPicker:
    def __init__(self):
        with open('students.json', 'r') as json_file:
            self.students = json.loads(json_file.read())

    def reset(self):
        with open('students.json', 'r') as json_file:
            self.students = json.loads(json_file.read())

    def run(self):
        total_students = len(self.students)
        random.shuffle(self.students)
        curr = 0
        nxt = 1
        while self.students:
            
            if curr < total_students - 1:
                print(f"\n\n\nNow presenting: {self.students[curr]}")
                curr += 1
            else: 
                break
            
            if nxt < total_students - 1:
                print(f"Next up: {self.students[nxt]}")
                nxt += 1
                print(f"{total_students - (curr)} students remaining")
                
            else:
                print("No more students!")


            input("\nPress 'Enter' to continue...")


if __name__ == "__main__":
    StudentPicker().run()
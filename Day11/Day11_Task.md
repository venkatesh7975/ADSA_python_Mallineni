# Day 11 Capstone Task: Printer Spooler Simulator

## Objective
Build a program that simulates a printer spooler (queue) handling multiple print jobs. This tests your understanding of FIFO (First In, First Out) operations.

## Requirements

1. **The System:**
   - You have a printer that can hold multiple print jobs in a queue.
   - You receive a stream of actions as a list of dictionaries.
   - An action can either be a new print job added to the queue, or a command to print the next job.

2. **The Logic:**
   - Use `collections.deque` for efficient queue operations.
   - If the action is a job, e.g., `{"type": "add", "document": "Resume.pdf"}`, you **enqueue** it.
   - If the action is `{"type": "print"}`, you **dequeue** the next document and print it to the screen. If the queue is empty, print "No jobs to print."

3. **Execution:**
   - Define your actions: 
     ```python
     actions = [
         {"type": "add", "document": "Resume.pdf"},
         {"type": "add", "document": "Photo.jpg"},
         {"type": "print"},
         {"type": "add", "document": "Notes.txt"},
         {"type": "print"},
         {"type": "print"},
         {"type": "print"}
     ]
     ```
   - Process the actions using your queue.

## Example Output
```text
Processing printer actions...
Added 'Resume.pdf' to the print queue.
Added 'Photo.jpg' to the print queue.
Printing: Resume.pdf
Added 'Notes.txt' to the print queue.
Printing: Photo.jpg
Printing: Notes.txt
Printer Error: No jobs to print.
```

Good luck! This is exactly how your computer handles multiple print requests!

### Day 1
- C# and NUnit

**Practice** 
- TDD, domain modelling and separation of concerns

### Day 2
- Typescript and Vitest
- Implement task from day 1 and then day 2

**Practice** 
- TDD and creating small, single purpose functions

**Lessons learned**
- If you get stuck, take smaller steps
- Vitest is probably the best testing framework out of any frameworks and out of any languages
- Needed to create a minimal `tsconfig.json` file to make `fs` module work
- Prepare test and file reading infrastructure before opening the task for the day to save time

### Day 3
- Rust and `cargo test`
- Implement task from day 2 and then day 3

**Practice** 
- TDD and learning Rust

**Lessons learned**
- Github Copilot is your friend when learning Rust syntax
- This task took much longer than needed, because initially I went with a brute force approach, later got moving when decided to step by characters

### Day 4
- Python and `pytest`
- Implement task from day 4 and then day 3

**Practice** 
- TDD and learning Python
- C simple test runner

**Lessons learned**
- Github Copilot is amazing at moving forward fast
- Binding folder into container: `docker run -it --mount "type=bind,src=$($pwd),target=/usr/src/5" -w /usr/src/5 --name aoc-gcc gcc:15.2`
- Building: `gcc -o build/main main.c`
- Running from `c` folder: `cd build/ && ./main && cd ..`
- Using devcontainers: https://blog.mandraketech.in/vscode-devcontainer-setup-for-cpp-programmers
- Decided to scratch the idea to implement day 5 in C - at least not the initial implementation, it takes way too much time
- Devcontainers are cool and save time

### Day 5
- Python

**Practice** 
- Planning AI agent in VS Code
- TDD and learning Rust

**Lessons learned**
- Spend a good while on tuning the plan. You can make manual changes, but it's better to make AI make them for you
- Insist on the AI to specify implementation steps in detail
- Github Copilot is amazing at moving forward fast

### Day 6
- Python

**Practice** 
- Write tests first, then let AI do the implementation
- Planning agent
- TDD in Typescript

**Lessons learned**
- AI had a really hard time with this one. Part one was done quite fast, but the second one it could not get even after tens of tries. I had to complete that manually. Decided to scratch that and move on.
- Sometimes the regular agent mode can be better at making a plan than the dedicated Plan agent

### Day 7
- Typescript

**Practice** 
- TDD in Typescript

**Lessons learned**
- Did part one quite fast, but got stuck at part two - set of in the wrong direction - next time try implementing the task as the description tries to guide you and don't come up with anything clever

### Day 8
- Python

**Practice** 
- TDD in Python

### Day 9
- Rust

**Practice** 
- TDD in Rust

**Lessons learned**
- This one was very difficult for me, the second part. I didn't really understand the requirements at first, so had to go back and forth using tests
- TDD proved most valuable here, because as I was making changes, I was sure I did not break anything that worked before. This has only shown me that my original idea to skip tests and do more debugging could prove fatal here. The real answer is to use a combination
- Performance optimizations were necessary on this one. A huge time saver was achieved in `is_vertical_range_disallowed()`. When I only used the filtered disallowed ranges, the speedup was very large
- Github Copilot was again of great help - mainly with syntax, but for smaller function also with the entire logic. It helps to have a descriptive name for the function for one, your future self, and two, for context for Copilot

### Day 10
- Python

**Practice** 
- Genetic algorithms and local search

**Lessons learned**
- Initially set of in C#, but quickly switched to Python because I realized that I could use genetic algorithms to perform a heuristic search - worked for part one, not for part two

### Day 11
- Language TBD
- Try finishing day 10 part two

**Practice** 
- Try implementing any of the previous tasks in SQL, for shits and giggles
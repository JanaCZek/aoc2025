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
- Language TBD

**Practice** 
- Try implementing any of the previous tasks in SQL, for shits and giggles
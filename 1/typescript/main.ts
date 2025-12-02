export type Dial = {
    value: number;
}

export type Command = {
    direction: 'L' | 'R';
    amount: number;
}

export function createDial(): Dial {
    return { value: 50 };
}

export function clickRight(dial: Dial): void {
    dial.value = (dial.value + 1) % 100;
}

export function clickLeft(dial: Dial): void {
    dial.value = (dial.value - 1 + 100) % 100;
}

export function countResultingValues(commands: Command[], valueOfInterest: number): number {
    const dial = createDial();
    let occurrences = 0;
    for (const command of commands) {
        for (let i = 0; i < command.amount; i++) {
            if (command.direction === 'R') {
                clickRight(dial);
            } else {
                clickLeft(dial);
            }
        }
        if (dial.value === valueOfInterest) {
            occurrences++;
        }
    }
    return occurrences;
}

export function countOccurredValues(commands: Command[], valueOfInterest: number): number {
    const dial = createDial();
    let occurrences = 0;
    for (const command of commands) {
        for (let i = 0; i < command.amount; i++) {
            if (command.direction === 'R') {
                clickRight(dial);
            } else {
                clickLeft(dial);
            }
            if (dial.value === valueOfInterest) {
                occurrences++;
            }
        }
    }
    return occurrences;
}

export function parseCommand(commands: string[]): Command[] {
    return commands.map(cmd => {
        const direction = cmd.charAt(0) as 'L' | 'R';
        const amount = parseInt(cmd.slice(1), 10);
        return { direction, amount };
    });
}
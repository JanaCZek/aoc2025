import { describe, it, expect, beforeAll } from 'vitest';
import { clickLeft, clickRight, countOccurredValues, countResultingValues, createDial, parseCommand } from './main';
import { readFile, readFileSync } from 'fs';

// Run using "npm run test"
describe('Dial tests', () => {
    it('has value 50 by default', () => {
        const dial = createDial();
        expect(dial.value).toBe(50);
    });

    it('turns right by 1', () => {
        const dial = createDial();
        clickRight(dial);
        expect(dial.value).toBe(51);
    });

    it('turns left by 1', () => {
        const dial = createDial();
        clickLeft(dial);
        expect(dial.value).toBe(49);
    });

    it('wraps around when turning right from 100', () => {
        const dial = createDial();
        dial.value = 99;
        clickRight(dial);
        expect(dial.value).toBe(0);
    });

    it('wraps around when turning left from 0', () => {
        const dial = createDial();
        dial.value = 0;
        clickLeft(dial);
        expect(dial.value).toBe(99);
    });

    it('starts and ends at 50 after 100 rotations to the right', () => {
        const dial = createDial();
        for (let i = 0; i < 100; i++) {
            clickRight(dial);
        }
        expect(dial.value).toBe(50);
    });

    it('starts and ends at 50 after 100 rotations to the left', () => {
        const dial = createDial();
        for (let i = 0; i < 100; i++) {
            clickLeft(dial);
        }
        expect(dial.value).toBe(50);
    });
});

describe('Command parser tests', () => {
    it('R1 command maps to turning the dial right by 1', () => {
        const commands = parseCommand(['R1']);

        expect(commands).toEqual([{ direction: 'R', amount: 1 }]);
    });

    it('L1 command maps to turning the dial left by 1', () => {
        const commands = parseCommand(['L1']);

        expect(commands).toEqual([{ direction: 'L', amount: 1 }]);
    });

    it('R10 command maps to turning the dial right by 10', () => {
        const commands = parseCommand(['R10']);

        expect(commands).toEqual([{ direction: 'R', amount: 10 }]);
    });

    it('L10 command maps to turning the dial left by 10', () => {
        const commands = parseCommand(['L10']);

        expect(commands).toEqual([{ direction: 'L', amount: 10 }]);
    });

    it('R100 command maps to turning the dial right by 100', () => {
        const commands = parseCommand(['R100']);

        expect(commands).toEqual([{ direction: 'R', amount: 100 }]);
    });

    it('L100 command maps to turning the dial left by 100', () => {
        const commands = parseCommand(['L100']);

        expect(commands).toEqual([{ direction: 'L', amount: 100 }]);
    });
});

describe('Value counter tests', () => {
    it('detects resulting value 51 once after turning right by 1 from 50', () => {
        const commands = parseCommand(['R1']);
        const count = countResultingValues(commands, 51);
        expect(count).toBe(1);
    });

    it('detects resulting value 51 twice after turning right by 1 from 50 and from 51 to 51 again', () => {
        const commands = parseCommand(['R1', 'R100']);
        const count = countResultingValues(commands, 51);
        expect(count).toBe(2);
    });

    it('detects resulting value 49 once after turning left by 1 from 50', () => {
        const commands = parseCommand(['L1']);
        const count = countResultingValues(commands, 49);
        expect(count).toBe(1);
    });

    it('detects resulting value 49 twice after turning left by 1 from 50 and from 49 to 49 again', () => {
        const commands = parseCommand(['L1', 'L100']);
        const count = countResultingValues(commands, 49);
        expect(count).toBe(2);
    });

    it('detects occurrence of value 51 once after turning right by 1 from 50', () => {
        const commands = parseCommand(['R1']);
        const count = countOccurredValues(commands, 51);
        expect(count).toBe(1);
    });

    it('detects occurrence of value 51 twice after turning right by 101 from 50', () => {
        const commands = parseCommand(['R101']);
        const count = countOccurredValues(commands, 51);
        expect(count).toBe(2);
    });

    it('detects occurrence of value 51 three times after turning right by 201 from 50', () => {
        const commands = parseCommand(['R201']);
        const count = countOccurredValues(commands, 51);
        expect(count).toBe(3);
    });
});

describe('Real input tests', () => {
    let inputCommands: string[] = [];

    beforeAll(() => {
        const data = readFileSync('../input.txt', 'utf-8');
        inputCommands = data.trim().split('\n');
    });

    it('detects how many times the resulting value 0 was encountered', () => {
        const commands = parseCommand(inputCommands);
        const count = countResultingValues(commands, 0);

        console.log(`Resulting value 0 was encountered ${count} times.`);

        expect(count).toBeTruthy();
    });

    it('detects how many times the occurred value 0 was encountered', () => {
        const commands = parseCommand(inputCommands);
        const count = countOccurredValues(commands, 0);

        console.log(`Resulting value 0 was encountered ${count} times.`);

        expect(count).toBeTruthy();
    });
});
import { describe, it, expect, beforeAll } from 'vitest';
import { readFileSync } from 'fs';
import { findOperatorIndexes, performOperation, splitIntoColumns } from './main';

// Run using "npm run test"
describe('Vertical parser tests', () => {
    it('finds operator indexes', () => {
        const input = ['*  +  '];
        const expected = [0, 3];

        expect(findOperatorIndexes(input[0])).toEqual(expected);
    });

    it('splits into columns', () => {
        const input = [
            '966 185 147 2533\n',
            '513 247 496 9374\n',
            '72  656  21  499\n',
            '1   914  15  398\n',
            '*   *   +   +   \n',
        ];
        const expected = [
            '966\n513\n72\n1\n*',
            '185\n247\n656\n914\n*',
            '147\n496\n21\n15\n+',
            '2533\n9374\n499\n398\n+',
        ];

        expect(splitIntoColumns(input)).toEqual(expected);
    });

    it('perform operation on columns', () => {
        const input = [
            '123\n45\n6\n*',
            '328\n64\n98\n+',
            '51\n387\n215\n*',
            '64\n23\n314\n+',
        ];
        const expected = [33210, 490, 4243455, 401];

        const results = input.map(column => performOperation(column));

        expect(results).toEqual(expected);
    });
});

describe('Real input tests', () => {
    let lines: string[] = [];

    beforeAll(() => {
        const data = readFileSync('../input.txt', 'utf-8');
        lines = data.trim().split('\n');
    });

    it('part one', () => {
        const columns = splitIntoColumns(lines);
        const results = columns.map(column => performOperation(column));
        const sum = results.reduce((acc, curr) => acc + curr, 0);

        console.log('Part one solution:', sum);
        expect(true).toBe(true);
    });

    it('part two', () => {
        expect(true).toBe(true);
    });
});
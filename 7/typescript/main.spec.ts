import { describe, it, expect, beforeAll } from 'vitest';
import { readFileSync } from 'fs';
import { Beam } from './main';

// Run using "npm run test"
describe('Tachyon beam tests', () => {
    let path: string[] = [];

    beforeAll(() => {
        path = [
            '.......S.......',
            '...............',
            '.......^.......',
            '...............',
            '......^.^......',
            '...............',
            '.....^.^.^.....',
            '...............',
            '....^.^...^....',
            '...............',
            '...^.^...^.^...',
            '...............',
            '..^...^.....^..',
            '...............',
            '.^.^.^.^.^...^.',
            '...............',
        ];
    });

    it('starts at S', () => {
        let beam = new Beam();
        beam.processPath(path);

        expect(beam.locations.length).greaterThanOrEqual(1);

        const startLocation = beam.locations[0];
        expect(startLocation).toEqual({ row: 1, col: 7 });
    });

    it('splits at ^', () => {
        let beam = new Beam();
        beam.processPath(path);

        expect(beam.locations.length).greaterThanOrEqual(2);

        const splitOne = beam.locations[1];
        const splitTwo = beam.locations[2];
        expect(splitOne).toEqual({ row: 2, col: 6 });
        expect(splitTwo).toEqual({ row: 2, col: 8 });
    });

    it('passes through .', () => {
        let beam = new Beam();
        beam.processPath(path);

        const passThroughOne = beam.locations[3];
        const passThroughTwo = beam.locations[4];
        expect(passThroughOne).toEqual({ row: 3, col: 6 });
        expect(passThroughTwo).toEqual({ row: 3, col: 8 });
    });
});

describe('Real input tests', () => {
    let lines: string[] = [];

    beforeAll(() => {
        const data = readFileSync('../input.txt', 'utf-8');
        lines = data.trim().split('\n');
    });

    it('part one', () => {
        let beam = new Beam();
        beam.processPath(lines);

        console.log('Part one solution:', beam.splitCount);
        expect(true).toBe(true);
    });

    it('part two', () => {
        expect(true).toBe(true);
    });
});
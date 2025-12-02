import { describe, it, expect, beforeAll } from 'vitest';
import { readFileSync } from 'fs';
import { createRange, detectNumbersWithDuplicateDigits, sumOfNumericStrings } from './main';

describe('Duplicate tests', () => {
    it('detects 11 and 22 in range 11-22', () => {
        const detected = detectNumbersWithDuplicateDigits("11", "22");
        expect(detected).toEqual(["11", "22"]);
    });

    it('detects 99 in range 95-115', () => {
        const detected = detectNumbersWithDuplicateDigits("95", "115");
        expect(detected).toEqual(["99"]);
    });

    it('detects 1010 in range 998-1012', () => {
        const detected = detectNumbersWithDuplicateDigits("998", "1012");
        expect(detected).toEqual(["1010"]);
    });

    it('detects 1188511885 in range 1188511880-1188511890', () => {
        const detected = detectNumbersWithDuplicateDigits("1188511880", "1188511890");
        expect(detected).toEqual(["1188511885"]);
    });

    it('detects 222222 in range 222220-222224', () => {
        const detected = detectNumbersWithDuplicateDigits("222220", "222224");
        expect(detected).toEqual(["222222"]);
    });

    it('detects no duplicates in range 1698522-1698528', () => {
        const detected = detectNumbersWithDuplicateDigits("1698522", "1698528");
        expect(detected).toEqual([]);
    });

    it('detects 446446 in range 446443-446449', () => {
        const detected = detectNumbersWithDuplicateDigits("446443", "446449");
        expect(detected).toEqual(["446446"]);
    });

    it('detects 38593859 in range 38593856-38593862', () => {
        const detected = detectNumbersWithDuplicateDigits("38593856", "38593862");
        expect(detected).toEqual(["38593859"]);
    });
});

describe('Range tests', () => {
    it('creates range from 0 to 1', () => {
        const range = createRange("0", "1");
        expect(range).toEqual(["0", "1"]);
    });

    it('creates range from 0 to 2', () => {
        const range = createRange("0", "2");
        expect(range).toEqual(["0", "1", "2"]);
    });

    it('creates range from 10 to 20', () => {
        const range = createRange("10", "20");
        expect(range).toEqual(["10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20"]);
    });
});

describe('Sum tests', () => {
    it('summing 0 and 0 results in 0', () => {
        const sum = sumOfNumericStrings(["0", "0"]);
        expect(sum).toEqual(BigInt(0));
    });

    it('summing 0 and 1 results in 1', () => {
        const sum = sumOfNumericStrings(["0", "1"]);
        expect(sum).toEqual(BigInt(1));
    });

    it('summing 1 and 1 results in 2', () => {
        const sum = sumOfNumericStrings(["1", "1"]);
        expect(sum).toEqual(BigInt(2));
    });
});

describe('Real input test', () => {
    let rangeStrings: string[] = [];

    beforeAll(() => {
        const fileContent = readFileSync('../input.txt', 'utf-8');
        rangeStrings = fileContent.split(',');
    });

    it('detects duplicate digit numbers in real input range', () => {
        let totalSum = BigInt(0);

        for (let rangeString of rangeStrings) {
            const [start, end] = rangeString.split('-');
            const detected = detectNumbersWithDuplicateDigits(start, end);
            totalSum += sumOfNumericStrings(detected);
        }
        console.log(totalSum);
    });
});
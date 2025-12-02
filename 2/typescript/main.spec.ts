import { describe, it, expect, beforeAll, test } from 'vitest';
import { readFileSync } from 'fs';
import { createRange, detectNumbersWithDuplicateDigits, detectNumbersWithMultipleDuplicateDigits, partitionStringToChunks, splitNumericStringUpToHalfPoint, sumOfNumericStrings } from './main';

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

describe('String split up to half point tests', () => {
    it('splits "11" into ["1"]', () => {
        const parts = splitNumericStringUpToHalfPoint("11");
        expect(parts).toEqual(["1"]);
    });

    it('splits "1111" into ["1", "11"]', () => {
        const parts = splitNumericStringUpToHalfPoint("1111");
        expect(parts).toEqual(["1", "11"]);
    });

    it('splits "111111" into ["1", "11", "111"]', () => {
        const parts = splitNumericStringUpToHalfPoint("111111");
        expect(parts).toEqual(["1", "11", "111"]);
    });
});

describe('Partition string into chunks tests', () => {
    it('partitions "1111" into chunks of size 1 resulting in ["1", "1", "1", "1"]', () => {
        const chunks = partitionStringToChunks("1111", 1);
        expect(chunks).toEqual(["1", "1", "1", "1"]);
    });

    it('partitions "1111" into chunks of size 2 resulting in ["11", "11"]', () => {
        const chunks = partitionStringToChunks("1111", 2);
        expect(chunks).toEqual(["11", "11"]);
    });

    it('partitions "111111" into chunks of size 3 resulting in ["111", "111"]', () => {
        const chunks = partitionStringToChunks("111111", 3);
        expect(chunks).toEqual(["111", "111"]);
    });
});

describe('Duplicate multidigit simple tests', () => {
    it('detects 11 and 22 in range 11-22', () => {
        const detected = detectNumbersWithMultipleDuplicateDigits("11", "22");
        expect(detected).toEqual(["11", "22"]);
    });

    it('detects 1111 in range 1111-1112', () => {
        const detected = detectNumbersWithMultipleDuplicateDigits("1111", "1112");
        expect(detected).toEqual(["1111"]);
    });

    it('detects 12341234 in range 12341234-12341235', () => {
        const detected = detectNumbersWithMultipleDuplicateDigits("12341234", "12341235");
        expect(detected).toEqual(["12341234"]);
    });
});

describe('Duplicate multidigit tests', () => {
    it('detects 11 and 22 in range 11-22', () => {
        const detected = detectNumbersWithMultipleDuplicateDigits("11", "22");
        expect(detected).toEqual(["11", "22"]);
    });

    it('detects 99 and 111 in range 95-115', () => {
        const detected = detectNumbersWithMultipleDuplicateDigits("95", "115");
        expect(detected).toEqual(["99", "111"]);
    });

    it('detects 999 and 1010 in range 998-1012', () => {
        const detected = detectNumbersWithMultipleDuplicateDigits("998", "1012");
        expect(detected).toEqual(["999", "1010"]);
    });

    it('detects 1188511885 in range 1188511880-1188511890', () => {
        const detected = detectNumbersWithMultipleDuplicateDigits("1188511880", "1188511890");
        expect(detected).toEqual(["1188511885"]);
    });

    it('detects 222222 in range 222220-222224', () => {
        const detected = detectNumbersWithMultipleDuplicateDigits("222220", "222224");
        expect(detected).toEqual(["222222"]);
    });

    it('detects no duplicates in range 1698522-1698528', () => {
        const detected = detectNumbersWithMultipleDuplicateDigits("1698522", "1698528");
        expect(detected).toEqual([]);
    });

    it('detects 446446 in range 446443-446449', () => {
        const detected = detectNumbersWithMultipleDuplicateDigits("446443", "446449");
        expect(detected).toEqual(["446446"]);
    });

    it('detects 38593859 in range 38593856-38593862', () => {
        const detected = detectNumbersWithMultipleDuplicateDigits("38593856", "38593862");
        expect(detected).toEqual(["38593859"]);
    });

    it('detects 565656 in range 565653-565659', () => {
        const detected = detectNumbersWithMultipleDuplicateDigits("565653", "565659");
        expect(detected).toEqual(["565656"]);
    });

    it('detects 824824824 in range 824824821-824824827', () => {
        const detected = detectNumbersWithMultipleDuplicateDigits("824824821", "824824827");
        expect(detected).toEqual(["824824824"]);
    });

    it('detects 2121212121 in range 2121212118-2121212124', () => {
        const detected = detectNumbersWithMultipleDuplicateDigits("2121212118", "2121212124");
        expect(detected).toEqual(["2121212121"]);
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

    it('detects duplicate multidigit numbers in real input range', () => {
        let totalSum = BigInt(0);

        for (let rangeString of rangeStrings) {
            const [start, end] = rangeString.split('-');
            const detected = detectNumbersWithMultipleDuplicateDigits(start, end);
            totalSum += sumOfNumericStrings(detected);
        }
        console.log(totalSum);
    });
});
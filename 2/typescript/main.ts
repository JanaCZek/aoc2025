export function detectNumbersWithDuplicateDigits(intervalStart: string, intervalEnd: string): string[] {
    let range = createRange(intervalStart, intervalEnd);
    let duplicates: string[] = [];

    for (const item of range) {
        const halfPoint = Math.floor(item.length / 2);
        const firstHalf = item.slice(0, halfPoint);
        const secondHalf = item.slice(halfPoint);

        if (firstHalf === secondHalf) {
            duplicates.push(item);
        }
    }

    return duplicates;
}

export function createRange(intervalStart: string, intervalEnd: string): string[] {
    let range: string[] = [];
    for (let i = BigInt(intervalStart); i <= BigInt(intervalEnd); i++) {
        range.push(i.toString());
    }
    return range;
}

export function sumOfNumericStrings(numbers: string[]): bigint {
    let sum = BigInt(0);
    for (const numStr of numbers) {
        sum += BigInt(numStr);
    }
    return sum;
}
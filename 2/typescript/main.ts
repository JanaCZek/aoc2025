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

export function detectNumbersWithMultipleDuplicateDigits(intervalStart: string, intervalEnd: string): string[] {
    let range = createRange(intervalStart, intervalEnd);
    let duplicates: string[] = [];

    for (const item of range) {
        let patterns = splitNumericStringUpToHalfPoint(item);
        for (const pattern of patterns) {
            const chunks = partitionStringToChunks(item, pattern.length);
            const allMatch = chunks.every(chunk => chunk === pattern);

            if (allMatch) {
                duplicates.push(item);
                break;
            }
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

export function splitNumericStringUpToHalfPoint(numStr: string): string[] {
    const halfPoint = Math.floor(numStr.length / 2);
    let parts: string[] = [];
    for (let i = 0; i < halfPoint; i++) {
        parts.push(numStr.slice(0, i + 1));
    }
    return parts;
}

export function partitionStringToChunks(numStr: string, chunkSize: number): string[] {
    let chunks: string[] = [];
    for (let i = 0; i < numStr.length; i += chunkSize) {
        chunks.push(numStr.slice(i, i + chunkSize));
    }
    return chunks;
}
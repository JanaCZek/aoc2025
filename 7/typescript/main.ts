export class Beam {
    locations: Location[] = [];
    splitCount: number = 0;

    processPath(path: string[]) {
        const start = path[0].indexOf('S');
        this.locations.push({ row: 1, col: start });
        let lineIndex = 1;

        for (let line of path.slice(1)) {
            const splitIndexes = line.split('').map((char, idx) => char === '^' ? idx : -1).filter(idx => idx !== -1);

            for (let split of splitIndexes) {
                if (this.locations.some(loc => loc.row === lineIndex - 1 && loc.col === split)) {
                    this.locations.push({ row: lineIndex, col: split - 1 });
                    this.locations.push({ row: lineIndex, col: split + 1 });
                    this.splitCount += 1;
                }
            }

            const passThroughIndexes = line.split('').map((char, idx) => char === '.' ? idx : -1).filter(idx => idx !== -1);

            for (let passThrough of passThroughIndexes) {
                if (this.locations.some(loc => loc.row === lineIndex - 1 && loc.col === passThrough)) {
                    this.locations.push({ row: lineIndex, col: passThrough });
                }
            }

            ++lineIndex;
        }
    }
}

export type Location = {
    row: number;
    col: number;
}
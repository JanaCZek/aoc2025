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

export function allTimelinesCount(path: string[]): number {
    let beam = new Beam();
    beam.processPath(path);

    console.log('Total locations:', beam.locations);
    const locations = beam.locations.splice(1).filter((loc, index, self) =>
        index === self.findIndex((t) => (
            t.row === loc.row && t.col === loc.col
        )) && loc.row % 2 === 0
    );
    
    let count = 0;
    const uniqueRowIndexes = Array.from(new Set(locations.map(loc => loc.row)));

    for (let uniqueRow of uniqueRowIndexes) {
        const rowLocations = locations.filter(loc => loc.row === uniqueRow);
        count += rowLocations.length;
    }
    
    return count;
}
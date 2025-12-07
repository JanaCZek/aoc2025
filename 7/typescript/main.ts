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

    processAllPaths(path: string[]): number {
        const start = path[0].indexOf('S');

        let pendingLocations: CountedLocation[] = [{ row: 1, col: start, count: 1 }];

        const noPassthroughs = path.filter(line => line.includes('^'));
        
        let lineIndex = 2;

        for (let line of noPassthroughs) {
            const splitIndexes = line.split('').map((char, idx) => char === '^' ? idx : -1).filter(idx => idx !== -1);
            let newPendingLocations: CountedLocation[] = [];

            const toSplit = pendingLocations.filter(loc => splitIndexes.includes(loc.col));
            const toPassThrough = pendingLocations.filter(loc => !splitIndexes.includes(loc.col));

            for (let loc of toSplit) {
                const existingLeft = newPendingLocations.find(l => l.row === lineIndex && l.col === loc.col - 1);
                if (existingLeft) {
                    existingLeft.count += loc.count;
                }
                else {
                    newPendingLocations.push({ row: lineIndex, col: loc.col - 1, count: loc.count });
                }
                const existingRight = newPendingLocations.find(l => l.row === lineIndex && l.col === loc.col + 1);
                if (existingRight) {
                    existingRight.count += loc.count;
                }
                else {
                    newPendingLocations.push({ row: lineIndex, col: loc.col + 1, count: loc.count });
                }
            }
            
            for (let loc of toPassThrough) {
                newPendingLocations.push(loc);
            }

            ++lineIndex;

            pendingLocations = newPendingLocations;
        }

        const counts = pendingLocations.map(loc => loc.count);
        return counts.reduce((a, b) => a + b, 0);
    }
}

export type Location = {
    row: number;
    col: number;
}

export type CountedLocation = Location & {
    count: number;
}

export function allTimelinesCount(path: string[]): number {
    let beam = new Beam();
    beam.processPath(path);

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
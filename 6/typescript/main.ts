const operatorChars = ['+', '*'];

export function performOperation(column: string): number {
    const items = column.split('\n');
    const numbers = items.slice(0, -1).map(item => parseInt(item, 10));
    const operator = items[items.length - 1];
    
    switch (operator) {
        case '+':
            return numbers.reduce((acc, curr) => acc + curr, 0);
        case '*':
            return numbers.reduce((acc, curr) => acc * curr, 1);
    }
}
export function splitIntoColumns(input: string[]): string[] {
    const operatorRow = input[input.length - 1];
    const operatorIndexes = findOperatorIndexes(operatorRow);

    let indexStart = operatorIndexes[0];
    let indexEnd = operatorIndexes[1];
    let indexer = 1;
    let columns: string[] = [];

    while (indexer < operatorIndexes.length) {
        const column = input.map(row => row.slice(indexStart, indexEnd).trim());
        columns.push(column.join('\n'));

        indexStart = indexEnd;
        ++indexer;
        indexEnd = operatorIndexes[indexer];        
    }

    const lastColumn = input.map(row => row.slice(indexStart).trim());
    columns.push(lastColumn.join('\n'));

    return columns;
}

export function findOperatorIndexes(row: string): number[] {
    return row.split('')
        .map((char, index) => (operatorChars.includes(char) ? index : -1))
        .filter((index) => index !== -1);
}
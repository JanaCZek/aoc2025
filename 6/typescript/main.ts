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

export function splitIntoColumnsPadded(input: string[]): string[] {
    const operatorRow = input[input.length - 1];
    const operatorIndexes = findOperatorIndexes(operatorRow);

    let indexStart = operatorIndexes[0];
    let indexEnd = operatorIndexes[1];
    let indexer = 1;
    let columns: string[] = [];

    while (indexer < operatorIndexes.length) {
        let column = input.map(row => row.slice(indexStart, indexEnd - 1));
        const maxCharacters = Math.max(...column.map(item => item.length));
        let digits: string[] = [];

        for (let i = 0; i < maxCharacters; i++) {
            let collectedDigits = '';
            for (let j = 0; j < column.length - 1; j++) {
                collectedDigits += column[j][i];
            }
            digits.push(collectedDigits.trim());
        }
        digits.push(column[column.length - 1].trim());

        columns.push(digits.join('\n'));

        indexStart = indexEnd;
        ++indexer;
        indexEnd = operatorIndexes[indexer];
    }

    const lastColumn = input.map(row => row.slice(indexStart));
    const maxCharacters = Math.max(...lastColumn.map(item => item.length));
    let digits: string[] = [];
   
    for (let i = 0; i < maxCharacters; i++) {
        let collectedDigits = '';
        for (let j = 0; j < lastColumn.length - 1; j++) {
            collectedDigits += lastColumn[j][i];
        }
        digits.push(collectedDigits.trim());
    }
    digits.push(lastColumn[lastColumn.length - 1].trim());

    columns.push(digits.join('\n'));

    return columns;
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
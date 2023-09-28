/**
 * @return {Generator<number>}
 */
const fibGenerator = function* () {
    let x = 0
    let y = 1
    let x_old
    let i = 0

    // i=0 -> [0]
    yield x

    while (true) {
        i += 1
        yield y // i=1 -> 1 | i=2 -> 2 | i=3 -> 3
        x_old = x // i=1 -> 0 | i=2 -> 1 | i=3 -> 2
        x = y // i=1 -> 1 | i=2 -> 2 | i=3 -> 3
        y = x + x_old // i=1 -> 2 | i=2 -> 3 | i=3 -> 5
    }
}

/**
 * const gen = fibGenerator();
 * gen.next().value; // 0
 * gen.next().value; // 1
 */

export { fibGenerator }

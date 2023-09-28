import { fibGenerator } from '../2648_generate_fibonacci_sequence.js'

describe('generator produces correct sequence of fibonacci', () => {
    test('n=1', () => {
        const gen = fibGenerator()
        const n = 1
        for (let i = 0; i < n; i++) {
            const nextValue = gen.next().value
            // console.log(nextValue)
        }
        const finalValue = gen.next().value
        expect(finalValue).toStrictEqual(1)
    })
    test('n=2', () => {
        const gen = fibGenerator()
        const n = 2
        for (let i = 0; i < n; i++) {
            const nextValue = gen.next().value
            // console.log(nextValue)
        }
        const finalValue = gen.next().value
        expect(finalValue).toStrictEqual(1)
    })
    test('n=3', () => {
        const gen = fibGenerator()
        const n = 3
        for (let i = 0; i < n; i++) {
            const nextValue = gen.next().value
            // console.log(nextValue)
        }
        const finalValue = gen.next().value
        expect(finalValue).toStrictEqual(2)
    })
    test('n=4', () => {
        const gen = fibGenerator()
        const n = 4
        for (let i = 0; i < n; i++) {
            const nextValue = gen.next().value
            // console.log(nextValue)
        }
        const finalValue = gen.next().value
        expect(finalValue).toStrictEqual(3)
    })
    test('n=5', () => {
        const gen = fibGenerator()
        const n = 5
        for (let i = 0; i < n; i++) {
            const nextValue = gen.next().value
            // console.log(nextValue)
        }
        const finalValue = gen.next().value
        expect(finalValue).toStrictEqual(5)
    })
    test('n=6', () => {
        const gen = fibGenerator()
        const n = 6
        for (let i = 0; i < n; i++) {
            const nextValue = gen.next().value
            // console.log(nextValue)
        }
        const finalValue = gen.next().value
        expect(finalValue).toStrictEqual(8)
    })
})

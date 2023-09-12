import { compose } from '../2629_function_composition.js'

test('Test function composition with x=4', () => {
    const fn = compose([x => x + 1, x => 2 * x])
    expect(fn(4)).toBe(9)
})
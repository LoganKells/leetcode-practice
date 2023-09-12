import { filter } from '../2634_filter_elements_from_array.js'

test('test filtering from array', () => {
    let arr = [0, 10, 20, 30]
    let fn = function greaterThan10(n) {
        return n > 10
    }

    expect(filter(arr, fn)).toStrictEqual([20, 30])
})
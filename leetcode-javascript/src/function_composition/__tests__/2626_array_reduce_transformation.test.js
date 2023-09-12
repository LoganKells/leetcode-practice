import { reduce } from '../2626_array_reduce_transformation.js'

test('Test the reduce function', () => {
    let nums = [1, 2, 3, 4]
    let fn = function sum(accum, curr) {
        return accum + curr
    }
    let init = 0
    expect(reduce(nums, fn, init)).toBe(10)
})
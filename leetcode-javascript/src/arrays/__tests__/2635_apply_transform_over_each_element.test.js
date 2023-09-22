import { map } from '../2635_apply_transform_over_each_element.js'

test('test transformation over array of numbers', () => {
    let nums = [1, 2, 3]
    const plusI = (n, i) => {
        return n + i
    }
    let result = map(nums, plusI)
    expect(result).toStrictEqual([1, 3, 5])
})

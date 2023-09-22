import { map, map2, map3 } from '../2635_apply_transform_over_each_element.js'

describe('test transformation over array of numbers using unique functions.', () => {
    test('using map()', () => {
        let nums = [1, 2, 3]
        const plusI = (n, i) => {
            return n + i
        }
        let result = map(nums, plusI)
        expect(result).toStrictEqual([1, 3, 5])
    })

    test('using map2()', () => {
        let nums = [1, 2, 3]
        const plusI = (n, i) => {
            return n + i
        }
        let result = map2(nums, plusI)
        expect(result).toStrictEqual([1, 3, 5])
    })

    test('using map3()', () => {
        let nums = [1, 2, 3]
        const plusI = (n, i) => {
            return n + i
        }
        let result = map3(nums, plusI)
        expect(result).toStrictEqual([1, 3, 5])
    })
})

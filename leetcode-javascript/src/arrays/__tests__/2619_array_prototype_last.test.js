import {myArrayType} from "../2619_array_prototype_last.js";

describe('test Array.prototype.last method', () => {
    // Assign the prototype to add the .last method to Array objects.
    Object.assign(Array.prototype, myArrayType);

    test('returns value of last array element as 3', () => {
            const arr = [1, 2, 3];
            arr.last(); // 3
            expect(arr.last()).toBe(3);
        }
    )

    test('returns value of last array element as -1', () => {
            const arr = [];
            arr.last(); // -1
            expect(arr.last()).toBe(-1);
        }
    )
})

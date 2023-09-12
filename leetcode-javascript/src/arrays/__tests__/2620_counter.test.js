import {createCounter} from "../2620_counter.js";

test ('counter calls increment return value starting at n', () => {
    const counter = createCounter(10)
    expect(counter()).toBe(10)
    expect(counter()).toBe(11)
    expect(counter()).toBe(12)
})
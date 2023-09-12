// https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise#basic_example

/**
 * Given a positive integer millis, write an asynchronous function that sleeps for millis milliseconds. It can resolve any value.
 *
 *
 *
 * Example 1:
 *
 * Input: millis = 100
 * Output: 100
 * Explanation: It should return a promise that resolves after 100ms.
 * let t = Date.now();
 * sleep(100).then(() => {
 *   console.log(Date.now() - t); // 100
 * });
 *
 * Example 2:
 *
 * Input: millis = 200
 * Output: 200
 * Explanation: It should return a promise that resolves after 200ms.
 *
 *
 *
 * Constraints:
 *
 *     1 <= millis <= 1000
 * */

/**
 * @param {number} millis
 */
async function sleep(millis) {
    return new Promise((resolve, reject) => {
        // the resolve function will be called after millis.
        setTimeout(resolve, millis)
    })
}

/**
 * let t = Date.now()
 * sleep(100).then(() => console.log(Date.now() - t)) // 100
 */

export { sleep }
import { sleep } from '../2161_sleep.js'

describe('test the sleep asynchronous function', () => {
        test('returns 101 after sleeping 100ms', () => {
            let start_time = Date.now()
            sleep(100).then(
                () => expect(Date.now() - start_time).toBe(101),
                () => console.log('error unhandled'),
            )
        })
    },
)
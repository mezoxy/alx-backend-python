Task 0:
=========
Write an asynchronous coroutine that takes in an integer argument (max_delay, with a default value of 10) named wait_random that waits for a random delay between 0 and max_delay (included and float value) seconds and eventually returns it.
Use the random module.

task 1:
==========
Write an asynchronous coroutine that takes in an integer argument (max_delay, with a default value of 10) named wait_random that waits for a random delay between 0 and max_delay (included and float value) seconds and eventually returns it.
Use the random module.

task 2:
==========
From the previous file, import wait_n into 2-measure_runtime.py.
Create a measure_time function with integers n and max_delay as arguments that measures the total execution time for wait_n(n, max_delay), and returns total_time / n. Your function should return a float.
Use the time module to measure an approximate elapsed time.

task 3:
==========
Import wait_random from 0-basic_async_syntax.

Write a function (do not create an async function, use the regular function syntax to do this) task_wait_random that takes an integer max_delay and returns a asyncio.Task.

task 4:
==========
Take the code from wait_n and alter it into a new function task_wait_n. The code is nearly identical to wait_n except task_wait_random is being called.


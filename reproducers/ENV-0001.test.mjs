import assert from 'node:assert/strict';
import { test } from 'node:test';
import { runInNewContext } from 'node:vm';

test('missing toSorted reproduces the error; sorting a new array preserves input', () => {
  const hostMethod = Array.prototype.toSorted;
  const result = runInNewContext(`
    Object.defineProperty(Array.prototype, 'toSorted', { value: undefined, configurable: true });
    const input = Object.freeze([
      Object.freeze({ order: 2, keep: true }),
      Object.freeze({ order: 1, keep: true }),
      Object.freeze({ order: 0, keep: false }),
    ]);
    let originalError;
    try { input.filter(item => item.keep).toSorted((a, b) => a.order - b.order); }
    catch (error) { originalError = error.message; }
    const sorted = input.filter(item => item.keep).sort((a, b) => a.order - b.order);
    let emptyError;
    try { [].filter(Boolean).toSorted(); }
    catch (error) { emptyError = error.message; }
    JSON.stringify({ originalError, emptyError, sorted: sorted.map(item => item.order), input: input.map(item => item.order) });
  `, {}, { timeout: 1000 });
  const observed = JSON.parse(result);
  assert.match(observed.originalError, /toSorted is not a function/);
  assert.match(observed.emptyError, /toSorted is not a function/);
  assert.deepEqual(observed.sorted, [1, 2]);
  assert.deepEqual(observed.input, [2, 1, 0]);
  assert.equal(Array.prototype.toSorted, hostMethod);
});

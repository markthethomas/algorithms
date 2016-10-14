import test from 'ava';

function numericMerge(a, b) {
  if (!Array.isArray(a) || !Array.isArray(b)) {
    throw new Error('We only accept arrays at this time');
  }
  const merged = [];
  let left = a[0];
  let right = b[0];
  let leftIndex = 1;
  let rightIndex = 1;

  while (left || right) {
    if ((left && !right) || left < right) {
      merged.push(left);
      left = a[leftIndex += 1];
    } else {
      merged.push(right);
      right = b[rightIndex += 1];
    }
  }

  return merged;
}

test('should merge numeric arrays', (t) => {
  const a = [2, 5, 6, 9];
  const b = [1, 2, 3, 29];
  const correctlyMerged = [1, 2, 2, 3, 5, 6, 9, 29];
  t.is(numericMerge(a, b).length, correctlyMerged.length);
});
